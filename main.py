from scripts.utils import load_config
from scripts.model_interface import call_model_api
from scripts.execute_service import execute_code_through_service
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Initialize Rich Console
console = Console()
# Setting the configuration
config = load_config()
model_config = config["model_service"]
execution_service_config = config["execution_service"]

def clean_code_block(text):
    """
    Removes code block delimiters (```python and ```).
    :param text: The text to clean.
    :return: The cleaned text.
    """
    if text.startswith("```python"):
        text = text[len("```python"):]
    if text.endswith("```"):
        text = text[:-len("```")]
    return text.strip()


def construct_prompt(user_input):
    """
    Construct a clear and concise prompt for the language model.
    :param user_input: The user's programming task.
    :return: The constructed prompt.
    :example: "Generate a Python script to calculate the factorial of a number."
    """
    code_generate_prompt = f"""
    Generate a complete Python script based on the following requirements:
    1. The script should be executable and produce output directly.
    2. Return only the code without explanations or extra text.
    3. DO NOT include any markdown or code block indicators.
    4. Make sure the code is properly formatted and indented.
    Task: {user_input}
    """
    return code_generate_prompt


def construct_debug_prompt(error_message, code, user_input):
    """
    Construct a prompt for debugging purposes.
    :param user_input: The original user input.
    :param code: The generated code.
    :param error_message: The error message from the execution service.
    :return: The constructed debug prompt.
    :example: "The task of the code: Generate a Python script to calculate the factorial of a number."
    :example: "An error occurred while running the code: NameError: name 'n' is not defined."
    :example: "Code: print(n)"
    """
    code_debug_prompt = f"""
    The task of the code: {user_input}
    An error occurred while running the code:
    Code: {code}
    Error: {error_message}
    Please check the Code according Error, and try again based on the following requirements:
    1. The script should be executable and produce output directly.
    2. Return only the code without explanations or extra text.
    3. DO NOT include any markdown or code block indicators.
    4. Make sure the code is properly formatted and indented.
    """
    return code_debug_prompt


def display_result(execution_output):
    """
    Display the execution result in a table format using rich.
    :param execution_output: The dictionary containing the execution result.
    :example: {"status": "success", "output": "42", "error": "", "timeout": false}
    """
    table = Table(title="Execution Result")
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")
    for key, value in execution_output.items():
        table.add_row(key, str(value))
    console.print(table)



def main():
    console.print(Panel("💡 Welcome to the AI Code Generator! 💻", style="bold green"))
    user_input = console.input("[bold blue]Enter your programming task: [/bold blue]")
    console.print(Panel(f"📝 [bold blue]Task: {user_input}[/bold blue]", style="blue"))
    loops = int(console.input("[bold blue]Enter the number of loops: [/bold blue]"))
    console.print(Panel(f"🔄 [bold blue]Number of Total loops: {loops}[/bold blue]", style="blue"))

    for i in range(loops):
        console.print(Panel(f"🔄 [bold blue]Starting Loop {i+1}[/bold blue]", style="blue"))
        result = process_task(user_input)

        if result["status"] == "success":
            display_result(result)
            break
        elif result["timeout"]:
            console.print("❗[bold red]Execution service timed out. Exiting...[/bold red]")
            break
        else:
            console.print(Panel("❌ [bold red]Task failed. Attempting debug...[/bold red]", style="red"))
            result = debug_task(result["error"], result["code"], user_input)

            if result["status"] == "success":
                display_result(result)
                break
            elif result["timeout"]:
                console.print("❗[bold red]Execution service timed out during debugging. Exiting...[/bold red]")
                break

    console.print(Panel("🚪 [bold yellow]Task ended.[/bold yellow]", style="yellow"))

def process_task(user_input):
    """
    Generate and execute code for the given user input.
    :param user_input: The user's programming task.
    :return: The execution result.
    """
    prompt = construct_prompt(user_input)
    console.print(Panel(f"📝 [bold blue]Prompt: {prompt}[/bold blue]", style="blue"))
    generated_code = call_model_api(prompt, **model_config)
    console.print(Panel(f"🚀 [bold blue]Generated Code: {generated_code}[/bold blue]", style="blue"))
    generated_code = clean_code_block(generated_code)

    execution_result = execute_code_through_service(generated_code, execution_service_config["url"])
    execution_result["code"] = generated_code
    return execution_result

def debug_task(error_message, code, user_input):
    """
    Generate and execute debug code based on error feedback.
    """
    debug_prompt = construct_debug_prompt(error_message, code, user_input)
    console.print(Panel(f"🔍 [bold blue]Debug Prompt: {debug_prompt}[/bold blue]", style="blue"))
    debug_code = call_model_api(debug_prompt, **model_config)
    console.print(Panel(f"🚀 [bold blue]Debug Code: {debug_code}[/bold blue]", style="blue"))
    debug_code = clean_code_block(debug_code)

    execution_result = execute_code_through_service(debug_code, execution_service_config["url"])
    execution_result["code"] = debug_code
    return execution_result


if __name__ == "__main__":
    main()
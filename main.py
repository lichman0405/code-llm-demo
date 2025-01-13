from scripts.utils import load_config
from scripts.model_interface import call_model_api
from scripts.execute_service import execute_code_through_service
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# Initialize Rich Console
console = Console()


def clean_code_block(text):
    """
    Removes code block delimiters (```python and ```).

    Parameters:
        text (str): The input text containing code block delimiters.

    Returns:
        str: The cleaned text with delimiters removed.
    """
    if text.startswith("```python"):
        text = text[len("```python"):]
    if text.endswith("```"):
        text = text[:-len("```")]
    return text.strip()


def construct_prompt(user_input):
    """
    Construct a clear and concise prompt for the language model.
    """
    base_prompt = f"""
    Generate a complete Python script based on the following requirements:
    1. The script should be executable and produce output directly.
    2. Return only the code without explanations or extra text.
    3. DO NOT include any markdown or code block indicators.
    4. Make sure the code is properly formatted and indented.
    Task: {user_input}
    """
    return base_prompt

def display_result(execution_result):
    """
    Display the execution result in a table format using rich.
    """
    table = Table(title="Execution Result")
    table.add_column("Key", style="cyan", no_wrap=True)
    table.add_column("Value", style="magenta")

    for key, value in execution_result.items():
        table.add_row(key, str(value))

    console.print(table)

def main():
    # Load configuration
    config = load_config()
    model_config = config["model_service"]
    execution_service_config = config["execution_service"]

    # Display welcome message
    console.print(Panel("💡 Welcome to the AI Code Generator! 💻", style="bold green"))

    # Get user input
    user_input = console.input("[bold blue]Enter your programming task: [/bold blue]")

    # Construct the prompt
    prompt = construct_prompt(user_input)
    console.print(Panel(f"📝 Constructed Prompt:\n{prompt}", style="bold cyan"))

    # Call the language model API
    console.print("🤖 [bold yellow]Calling the language model API...[/bold yellow]")
    generated_code = call_model_api(
        prompt=prompt,
        api_key=model_config["api_key"],
        api_base=model_config["api_base"],
        model=model_config["model"],
        temperature=0.7
    )

    generated_code = clean_code_block(generated_code)

    if generated_code:
        console.print(Panel("✅ [bold green]Generated Code:[/bold green]", style="green"))
        console.print(f"[code]{generated_code}[/code]")

        # Execute the code through the service
        console.print("⚙️ [bold yellow]Executing code through the service...[/bold yellow]")
        execution_result = execute_code_through_service(
            code=generated_code,
            service_url=execution_service_config["url"]
        )

        # Display execution results
        console.print(Panel("📊 [bold green]Execution Result:[/bold green]", style="green"))
        display_result(execution_result)
    else:
        console.print(Panel("❌ [bold red]Failed to generate code.[/bold red]", style="red"))

if __name__ == "__main__":
    main()

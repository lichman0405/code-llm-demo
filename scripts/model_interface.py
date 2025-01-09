import openai
from scripts.utils import log_to_file

def call_model_api(prompt, api_key, api_base, model):
    """
    Call the language model API using the OpenAI library.
    """
    try:
        # Configure OpenAI client
        openai.api_key = api_key
        openai.api_base = api_base

        # Call the ChatCompletion API
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract the generated content
        generated_content = response.choices[0].message.content

        # Log the result
        log_to_file("model.log", f"PROMPT:\n{prompt}\n\nRESPONSE:\n{generated_content}")
        return generated_content
    except Exception as e:
        log_to_file("error.log", f"Error calling model API: {e}")
        print(f"Error calling model API: {e}")
        return None

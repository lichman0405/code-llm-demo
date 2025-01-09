# AI Code Generator

AI Code Generator is a Python-based terminal tool that uses advanced language models to generate Python code based on user input and execute the generated code in an isolated environment. It supports flexible configuration for different language model APIs, including OpenAI and locally hosted models like Ollama.

## Features

- **Code Generation**: Dynamically generate Python scripts based on natural language descriptions.
- **Code Execution**: Run the generated scripts in an isolated environment using a pre-configured execution service.
- **Flexible API Support**: Works with OpenAI APIs or other custom APIs via flexible configuration.
- **Interactive Terminal UI**: Beautiful and intuitive terminal interaction with enhanced visual feedback using the `rich` library.
- **Logging**: Detailed logs for debugging and monitoring, including prompts, API responses, and execution results.

## Project Structure

```
project/
├── config/
│   └── config.yaml           # Configuration file for APIs and services
├── logs/                     # Directory for logs
│   └── *.log                 # Log files (model behavior, execution results, errors)
├── scripts/
│   ├── model_interface.py    # Handles language model API interactions
│   ├── execute_service.py    # Handles code execution service interactions
│   ├── utils.py              # Utility functions (logging, config loading)
├── main.py                   # Main entry point for the application
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

## Installation

### 1. Clone the Repository

```bash
git clone <repository_url>
cd project/
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

Edit the `config/config.yaml` file to set up API keys, service URLs, and other configurations.

```yaml
model_service:
  api_key: "your_api_key_here"           # API key for the language model
  api_base: "https://api.openai.com/v1"  # Base URL for OpenAI or custom API
  model: "gpt-4"                         # Model name (e.g., gpt-4, llama2-13b-chat)

execution_service:
  url: "http://192.168.100.207:22499/submit_code"  # URL of the code execution service

logging:
  directory: "logs"                      # Directory for log files
  level: "INFO"                          # Log level (e.g., INFO, DEBUG)
```

## Usage

### 1. Run the Application

```bash
python main.py
```

### 2. Enter a Task Description

When prompted, enter the task you want the AI to solve. For example:

```plaintext
Write a Python script to implement bubble sort. The script should randomly generate 5 integers, sort them using bubble sort, and print both the unsorted and sorted lists.
```

### 3. View the Results

The terminal will display:
- The constructed prompt sent to the language model.
- The generated Python script.
- The execution results (or errors, if any) in a beautifully formatted table.

## Logs

The application generates logs for debugging and monitoring:
- **Model Behavior Logs** (`logs/model.log`): Contains prompts and API responses.
- **Execution Logs** (`logs/execution.log`): Contains the submitted code and execution results.
- **Error Logs** (`logs/error.log`): Records any errors during API calls or service interactions.

## Customization

### Switching Between APIs

To use a locally hosted model like Ollama:
1. Update `api_base` in `config.yaml` to your local API URL (e.g., `http://127.0.0.1:8000/v1`).
2. Specify the model name (e.g., `llama2-13b-chat`).

### Adjusting Execution Service

Modify the `url` under `execution_service` in `config.yaml` to point to your execution service.

## Dependencies

This project requires the following Python packages:
- `openai`: For interacting with OpenAI or custom language models.
- `requests`: For making HTTP requests to APIs and services.
- `pyyaml`: For loading configuration files.
- `rich`: For enhanced terminal UI.

Install all dependencies with:

```bash
pip install -r requirements.txt
```

## Example Output

### User Input

```plaintext
Write a Python script to implement bubble sort. The script should randomly generate 5 integers, sort them using bubble sort, and print both the unsorted and sorted lists.
```

### Generated Code

```python
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Unsorted:", random_numbers)
bubble_sort(random_numbers)
print("Sorted:", random_numbers)
```

### Execution Result

```plaintext
📊 Execution Result:
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key         ┃ Value                                       ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ output      │ Unsorted: [34, 12, 67, 23, 89]              │
│             │ Sorted: [12, 23, 34, 67, 89]                │
├─────────────┼─────────────────────────────────────────────┤
│ error       │                                             │
└─────────────┴─────────────────────────────────────────────┘
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Feedback

If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request!


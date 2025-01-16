# AI Code Generator

AI Code Generator is a Python-based terminal tool that uses advanced language models to generate Python code based on user input and execute the generated code in an isolated environment. It supports flexible configuration for various language model APIs, including OpenAI and locally hosted models like Ollama. The tool also includes debugging features to refine and improve generated code based on execution errors.

---

## **Features**

### **1. Code Generation**
- Dynamically generate Python scripts based on natural language task descriptions provided by the user.

### **2. Code Execution**
- Run the generated scripts in an isolated environment using a pre-configured execution service.

### **3. Debugging Support**
- Automatically generates debugging prompts and refined code when execution errors are encountered.

### **4. Flexible API Support**
- Works seamlessly with OpenAI APIs or custom APIs via flexible configuration options.

### **5. Interactive Terminal UI**
- Provides an intuitive terminal interaction experience with enhanced visual feedback using the `rich` library.

### **6. Logging**
- Generates detailed logs for debugging and monitoring, including prompts, API responses, and execution results.

---

## **Project Structure**

```plaintext
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

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd project/
```

### **2. Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## **Configuration**

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

---

## **Usage**

### **1. Run the Application**
```bash
python main.py
```

### **2. Enter a Task Description**
When prompted, enter the task you want the AI to solve. For example:
```plaintext
Generate a Python script that calculates the sum of all prime numbers less than a given input number.
```

### **3. View the Results**
The terminal will display:
- The constructed prompt sent to the language model.
- The generated Python script.
- The execution results (or errors, if any) in a beautifully formatted table.

### **4. Debugging**
If the initial execution fails, the tool will automatically:
- Generate a debugging prompt using the error message and initial code.
- Call the language model to refine the code.
- Retry execution with the refined code.

---

## **Logs**
The application generates logs for debugging and monitoring:

- **Model Behavior Logs:** Contain prompts and API responses.
- **Execution Logs:** Contain the submitted code and execution results.
- **Error Logs:** Record any errors during API calls or service interactions.

Logs are stored in the `logs/` directory.

---

## **Customization**

### **Switching Between APIs**
To use a locally hosted model like Ollama:
- Update `api_base` in `config.yaml` to your local API URL (e.g., `http://127.0.0.1:8000/v1`).
- Specify the model name (e.g., `llama2-13b-chat`).

### **Adjusting Execution Service**
Modify the `url` under `execution_service` in `config.yaml` to point to your execution service.

---

## **Dependencies**

This project requires the following Python packages:

- `openai`: For interacting with OpenAI or custom language models.
- `requests`: For making HTTP requests to APIs and services.
- `pyyaml`: For loading configuration files.
- `rich`: For enhanced terminal UI.

Install all dependencies with:
```bash
pip install -r requirements.txt
```

---

## **Example Output**

### **User Input**
```plaintext
Generate a Python script that prints the Fibonacci sequence up to the 50th term.
```

### **Generated Code**
```python
def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

print(fibonacci_sequence(50))
```

### **Execution Result**
```plaintext
📊 Execution Result:
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Key         ┃ Value                                       ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ output      │ [0, 1, 1, 2, 3, 5, 8, ...]                 │
│ error       │                                             │
└─────────────┴─────────────────────────────────────────────┘
```

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## **Feedback**

If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request!
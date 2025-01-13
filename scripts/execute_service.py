import requests
from scripts.utils import log_to_file


def execute_code_through_service(code, service_url, timeout=10):
    """
    Submit generated code to the execution service.

    Parameters:
        code (str): The Python code to execute.
        service_url (str): The URL of the execution service.
        timeout (int): Timeout for the HTTP request, in seconds (default: 10).

    Returns:
        dict: A dictionary containing the execution result or error details.
    """
    headers = {"Content-Type": "application/json"}
    data = {"code": code}

    try:
        response = requests.post(service_url, headers=headers, json=data, timeout=timeout)

        if response.status_code == 200:
            try:
                execution_result = response.json()
                execution_result["error"] = None  # Add "error": None when no errors occur
            except ValueError:
                # Handle case where response is not valid JSON
                execution_result = {
                    "error": "Invalid JSON response from the service",
                    "details": None
                }
        else:
            execution_result = {
                "error": f"Service returned status code {response.status_code}",
                "details": None
            }

        # Log the code and execution result
        log_to_file("execution.log", f"CODE:\n{code}\n\nRESULT:\n{execution_result}")
        return execution_result

    except requests.exceptions.Timeout:
        error_message = "Unable to connect to the service: Request timed out."
        detailed_message = f"Service request timed out: {service_url}"
        log_to_file("error.log", detailed_message)
        print(f"Error: {error_message}")
        return {"error": error_message, "details": None}

    except requests.exceptions.ConnectionError as e:
        error_message = "Unable to connect to the service: Connection refused."
        detailed_message = f"Connection error: {e}"
        log_to_file("error.log", detailed_message)
        print(f"Error: {error_message}")
        return {"error": error_message, "details": None}

    except requests.exceptions.RequestException as e:
        error_message = "An error occurred while contacting the service."
        detailed_message = f"Request error: {e}"
        log_to_file("error.log", detailed_message)
        print(f"Error: {error_message}")
        return {"error": error_message, "details": None}

    except Exception as e:
        error_message = "An unexpected error occurred."
        detailed_message = f"Unexpected error: {e}"
        log_to_file("error.log", detailed_message)
        print(f"Error: {error_message}")
        return {"error": error_message, "details": None}


if __name__ == "__main__":
    # 示例代码
    sample_code = """print("Hello from the execution service!")"""

    # 服务 URL（从配置文件加载）
    service_url = "http://192.168.100.207:22499/submit_code"  # Intentionally wrong URL for testing

    # 调用执行服务
    result = execute_code_through_service(sample_code, service_url)

    # 输出结果
    print(result)

import requests
from scripts.utils import log_to_file

def execute_code_through_service(code, service_url):
    """
    Submit generated code to the execution service.
    """
    headers = {"Content-Type": "application/json"}
    data = {"code": code}
    try:
        response = requests.post(service_url, headers=headers, json=data)
        execution_result = response.json() if response.status_code == 200 else {
            "error": f"Service returned status code {response.status_code}",
            "details": response.text
        }
        log_to_file("execution.log", f"CODE:\n{code}\n\nRESULT:\n{execution_result}")
        return execution_result
    except requests.exceptions.RequestException as e:
        log_to_file("error.log", f"Error calling service: {e}")
        print(f"Failed to call the service: {e}")
        return {"error": "Failed to call the service", "details": str(e)}

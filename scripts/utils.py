import os
import yaml

def load_config():
    """Load the configuration from the YAML file."""
    with open("config/config.yaml", "r", encoding='utf-8') as file:
        return yaml.safe_load(file)

def ensure_directory(directory):
    """Ensure a directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def log_to_file(filename, content, log_dir="logs"):
    """Write content to a log file."""
    ensure_directory(log_dir)
    with open(os.path.join(log_dir, filename), "a", encoding="utf-8") as file:
        file.write(content + "\n")

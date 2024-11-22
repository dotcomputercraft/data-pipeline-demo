import json
import os


def load_config(config_path: str) -> dict:
    """Loads configuration from a JSON file."""
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file '{config_path}' does not exist.")
    with open(config_path, 'r') as file:
        return json.load(file)
        
def extract(input_file: str) -> list:
    """Extracts data from a JSON file."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")
    
    with open(input_file, 'r') as file:
        data = json.load(file)
    return data

def transform(data: list, multiplier: int) -> list:
    """Transforms the data by multiplying each number."""
    return [item * multiplier for item in data]

def load(data: list, output_file: str) -> None:
    """Loads transformed data into a JSON file."""
    with open(output_file, 'w') as file:
        json.dump(data, file)
    print(f"Data successfully loaded into '{output_file}'")
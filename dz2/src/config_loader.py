import yaml

def read_config(config_path):
    """Чтение конфигурации из YAML файла."""
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

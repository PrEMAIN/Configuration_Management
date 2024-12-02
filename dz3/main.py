import argparse
from parser import parse_config
from converter import convert_to_toml

def main():
    parser = argparse.ArgumentParser(description="Конвертер конфигурации в TOML")
    parser.add_argument("input_file", type=str, help="Путь к файлу с конфигурацией")
    args = parser.parse_args()
    
    try:
        with open(args.input_file, 'r') as file:
            config_text = file.read()
        parsed_data = parse_config(config_text)
        toml_output = convert_to_toml(parsed_data)
        print(toml_output)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()

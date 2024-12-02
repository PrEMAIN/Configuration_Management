def convert_to_toml(data, parent_key=""):
    toml_output = []
    for key, value in data.items():
        if isinstance(value, dict):
            section = f"[{key}]" if not parent_key else f"[{parent_key}.{key}]"
            toml_output.append(section)
            toml_output.append(convert_to_toml(value, key))
        else:
            toml_output.append(f"{key} = {value}")
    return '\n'.join(toml_output)

import re
import math

def parse_config(config_text, context=None):
    """Парсит конфигурационный текст и вычисляет значения."""
    if context is None:
        context = {}

    # Удаление многострочных комментариев
    config_text = re.sub(r'/\+.*?\+/', '', config_text, flags=re.DOTALL)
    
    # Проверка баланса скобок
    if config_text.count('{') != config_text.count('}'):
        raise SyntaxError("Несбалансированные фигурные скобки.")
    
    # Рекурсивный парсинг словарей
    result = {}
    stack = []
    current_dict = result
    buffer = ""

    for char in config_text:
        if char == "{":
            # Новый вложенный словарь
            stack.append(current_dict)
            new_dict = {}
            current_dict[buffer.strip()] = new_dict
            current_dict = new_dict
            buffer = ""
        elif char == "}":
            # Завершение текущего словаря
            if buffer.strip():
                key, value = parse_key_value(buffer.strip(), context)
                current_dict[key] = value
            if stack:
                current_dict = stack.pop()
            buffer = ""
        elif char == ",":
            # Завершение пары ключ-значение
            if buffer.strip():
                key, value = parse_key_value(buffer.strip(), context)
                current_dict[key] = value
            buffer = ""
        else:
            buffer += char

    return result

def parse_key_value(line, context):
    """Парсит строку ключ: значение и учитывает вычисляемые выражения."""
    try:
        key, value = map(str.strip, line.split(":"))
    except ValueError:
        raise SyntaxError(f"Некорректная строка: {line}")
    
    if not re.match(r'^[_a-zA-Zа-яА-ЯёЁ0-9]+$', key):
        raise SyntaxError(f"Некорректное имя: {key}")
    
    # Вычисляем значение
    evaluated_value = parse_value(value, context)
    context[key] = evaluated_value  # Сохраняем переменную в контексте
    return key, evaluated_value

def parse_value(value, context):
    """Парсит значение, включая поддержку выражений."""
    if value.isdigit():
        return int(value)
    elif value.startswith('{') and value.endswith('}'):
        return parse_config(value, context)
    elif value.startswith('^[') and value.endswith(']'):
        expression = value[2:-1].strip()
        return evaluate_expression(expression, context)
    else:
        return value  # Для строковых значений

def evaluate_expression(expression, context):
    """Вычисляет выражение с учётом контекста."""
    try:
        # Замена переменных на их значения
        for key, val in context.items():
            expression = expression.replace(key, str(val))
        return eval(expression, {"__builtins__": None, "abs": abs, "math": math})
    except Exception as e:
        raise ValueError(f"Ошибка вычисления выражения '{expression}': {e}")

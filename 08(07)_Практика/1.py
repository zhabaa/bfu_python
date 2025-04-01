import os
import json
from jsonschema import validate, ValidationError
from termcolor import colored


DIR_PATH = 'examples'


def validate_file(file_path, schema_path):
    try:
        with open(schema_path, 'r') as schema_file:
            schema = json.load(schema_file)

        with open(file_path, 'r') as data_file:
            data = json.load(data_file)

        validate(instance=data, schema=schema)

        print(f"Файл {colored(file_path, 'yellow')} валиден по схеме.")
        return True

    except ValidationError as e:
        print(f"Файл {colored(file_path, 'yellow')} НЕ валиден по схеме. Ошибка:")
        print(f"Сообщение: {e.message}")
        print(f"Путь к ошибке: {e.json_path}")
        print(f"Контекст ошибки: {e.context}")
        return False

    except json.JSONDecodeError as e:
        print(f"Ошибка при чтении JSON файла {colored(file_path, 'yellow')}: {e}")
        return False

    except Exception as e:
        print(f"Неожиданная ошибка при обработке файла {colored(file_path, 'yellow')}: {e}")
        return False


print(colored("Проверка исходного файла:", 'green'))
validate_file(
    os.path.join(DIR_PATH, "ex_1.json"),
    os.path.join(DIR_PATH, "ex_1.schema.json")
)

print(colored("\nПроверка файла с ошибками:", 'green'))
validate_file(
    os.path.join(DIR_PATH, "ex_1_invalid.json"),
    os.path.join(DIR_PATH, "ex_1.schema.json")
)
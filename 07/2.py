import os
import json
from termcolor import colored

DIR_PATH = "examples"


def process_user_data(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        user_phones = {user["name"]: user["phoneNumber"] for user in data}

        print(colored("Словарь пользователей (имя: телефон):", "green"))

        for name, phone in user_phones.items():
            print(f"{name}: {phone}")

        return user_phones

    except FileNotFoundError:
        print(f"{colored("Ошибка", "red")}: файл {colored(file_path, 'yellow')} не найден")

    except json.JSONDecodeError:
        print(f"{colored("Ошибка", "red")}: файл {colored(file_path, 'yellow')} содержит некорректный JSON")

    except KeyError as e:
        print(f"{colored("Ошибка", "red")}: в данных отсутствует обязательное поле {e}")

    except Exception as e:
        print(f"{colored("Неожиданная шибка", "red")}: {e}")


def main():
    user_phones = process_user_data(f"{DIR_PATH}/ex_2.json")

    if user_phones:
        with open(f"{DIR_PATH}/user_phones.json", "w", encoding="utf-8") as out_file:
            json.dump(user_phones, out_file, ensure_ascii=False, indent=2)

        print(f"\nРезультат сохранен в файл {colored(f"{DIR_PATH}/user_phones.json", 'yellow')}")


if __name__ == "__main__":
    main()

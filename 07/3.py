import json
from termcolor import colored

DIR_PATH = 'examples'


def add_invoice(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        if 'invoices' not in data:
            data['invoices'] = []
        
        new_invoice = {
            "id": len(data['invoices']) + 1,
            "total": 350.50,
            "items": [
                {
                    "name": "item 4",
                    "quantity": 3,
                    "price": 100.00
                },
                {
                    "name": "item 5",
                    "quantity": 1,
                    "price": 50.50
                }
            ]
        }
        
        data['invoices'].append(new_invoice)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        print(f"{colored("Новый invoice успешно добавлен.", 'green')} Результат сохранен в {colored(output_file, 'yellow')}")
        return True
    
    except FileNotFoundError:
        print(f"{colored("Ошибка", "red")}: файл {colored(input_file, 'yellow')} не найден")
        return False

    except json.JSONDecodeError:
        print(f"{colored("Ошибка", "red")}: файл {colored(input_file, 'yellow')} содержит некорректный JSON")
        return False

    except Exception as e:
        print(f"{colored("Неожиданная шибка", "red")}: {e}")
        return False


if __name__ == "__main__":
    add_invoice(f"{DIR_PATH}/ex_3.json", f"{DIR_PATH}/ex_3_updated.json")
import argparse
import csv
import json


def load_json(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def write_csv(data: dict, output_file: str) -> None:
    root_key = list(data.keys())[0]
    headers = data[root_key][0].keys()
    json_data = data[root_key]

    with open(output_file, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(headers)

        for item in json_data:
            writer.writerow(item.values())


def json2csv(json_file: str) -> None:
    data = load_json(json_file)

    root_key = list(data.keys())[0]
    output_file = f"{root_key}.csv"

    write_csv(data, output_file)


def main():
    parser = argparse.ArgumentParser(description="Конвертирует json файл в csv")
    parser.add_argument("--filename", type=str, required=True, help="Путь к json")

    args = parser.parse_args()

    json2csv(args.filename)


if __name__ == "__main__":
    main()

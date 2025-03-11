import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', type=str, help="Путь к папке копирования")
    args = parser.parse_args()
    
    missing_files_path = Path(f"{args.dirpath}/missing_files.txt") 

    if not missing_files_path.exists():
        print(f"[err]: '{missing_files_path}' не найден.")
        return

    target_dir = Path(args.dirpath)
    target_dir.mkdir(exist_ok=True)

    with open(missing_files_path, "r", encoding="utf-8") as file:
        missing_files = file.read().splitlines()

    for file_name in missing_files:
        file_path = target_dir / file_name
        if not file_path.exists():
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")
            print(f"[+] Создан файл: {file_path}")
        else:
            print(f"[!] Файл уже существует: {file_path}")

if __name__ == "__main__":
    main()
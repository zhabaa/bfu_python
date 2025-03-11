import argparse
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dirpath', type=str, default='.', help="Путь к папке (по умолчанию текущая папка)")
    parser.add_argument('--files', nargs='*', default=[], help="Список файлов для проверки")
    args = parser.parse_args()

    dirpath = Path(args.dirpath)

    if not dirpath.is_dir():
        print(f"Ошибка: Папка '{dirpath}' не существует.")
        return

    if not args.files:
        files_in_dir = list(dirpath.iterdir())
        total_files = len(files_in_dir)
        total_size = sum(f.stat().st_size for f in files_in_dir if f.is_file())
        print(f"Общая информация о папке '{dirpath}':")
        print(f"Количество файлов: {total_files}")
        print(f"Общий размер файлов: {total_size} байт")
        return

    existing_files = []
    missing_files = []

    for file_name in args.files:
        file_path = dirpath / file_name
        if file_path.exists() and file_path.is_file():
            existing_files.append(file_name)
        else:
            missing_files.append(file_name)

    print("[!] Файлы, присутствующие в папке:")
    for file in existing_files:
        print(file)

    print("\n[!] Файлы, отсутствующие в папке:")
    for file in missing_files:
        print(file)

    if existing_files:
        with open(dirpath / "existing_files.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(existing_files))

    if missing_files:
        with open(dirpath / "missing_files.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(missing_files))

    print("\n[!] Списки файлов сохранены в 'existing_files.txt' и 'missing_files.txt'.")

if __name__ == "__main__":
    main()
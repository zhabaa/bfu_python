import argparse
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path', type=str, nargs='?', default='.')
    args = parser.parse_args()

    folder_path = Path(args.path)

    if not folder_path.is_dir():
        print(f"[err] '{folder_path}' не существует.")
        return

    smol_files = [f for f in folder_path.iterdir() if f.is_file() and f.stat().st_size < 2 ** 11]

    if smol_files:
        print("[!] Найденные файлы меньше 2К:")
        for file in smol_files:
            print(file.name)
    else:
        print("[-] Нет файлов меньше 2К")
        
    smol_folder = folder_path / 'small'
    smol_folder.mkdir(exist_ok=True)

    for file in smol_files:
        shutil.copy(file, smol_folder / file.name)

    print(f"[!] Файлы скопированы в папку '{smol_folder}'.")

if __name__ == "__main__":
    main()
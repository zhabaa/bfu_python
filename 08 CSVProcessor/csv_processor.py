import os
import csv
import random
import logging
from typing import List, Dict, Union

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

logger = logging.getLogger(__name__)


class CSVProcessor:
    def __init__(self) -> None:
        self.file_path: str = str()
        self.data: List[Dict[str, Union[str, int, float]]] = list()
        self.headers: List[str] = list()
        self.rows: int = None
        self.cols: int = None
    
    def _check_data(self) -> bool:
        """
        Проверка наличия данных
        """
        
        if not self.data:
            logger.info("Нет данных для отображения")
            return False
        
        return True
    
    def _write_file(self, output_path: str, filename: str) -> None:
      with open(output_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(filename)

    def _detect_type(self, value: str) -> str:
        """Определяет тип данных значения"""
        try:
            int(value)
            return "int"
        except ValueError:
            try:
                float(value)
                return "float"
            except ValueError:
                return "str"

    def _select_rows(self, output_type: str, rows: int) -> list:
        """
        Выбирает строки в зависимости от типа вывода
        """
        
        match output_type:
            case "top":
                return self.data[:rows]
            case "bottom":
                return self.data[-rows:]
            case "random":
                return random.sample(self.data, min(rows, len(self.data)))
            case _:
                logger.info(f"Неизвестный тип вывода: {output_type}. Используется значение по умолчанию.")
                return self.data[:rows]

    def _validate_row_count(self, requested: int, available: int) -> None:
        """
        Проверяет количество строк
        """
        
        if available < requested:
            logger.info(f"Внимание: запрошено {requested} строк, доступно {available}")

    def _calculate_column_widths(self, rows: list) -> dict:
        """
        Вычисляет ширину для каждой колонки
        """
        
        widths = {header: len(header) for header in self.headers}
        
        for row in rows:
            for header in self.headers:
                cell_value = str(row.get(header, ""))
                widths[header] = max(widths[header], len(cell_value)) + 1
        
        return widths

    def _print_output(self, rows: list, col_widths: dict, separator: str) -> None:
        """
        Форматирует и выводит данные
        """

        headers = [f"{header:<{col_widths[header]}}" for header in self.headers]
        header_line = separator.join(headers)

        print(header_line)
        print("-" * len(header_line))

        for row in rows:
            cells = [f"{str(row.get(header, '')):<{col_widths[header]}}" for header in self.headers]
            print(separator.join(cells))

    def load_data(self, filepath: str) -> None:
        """
        Загрузка данных

        :param file_path: Путь к CSV файлу
        """

        self.file_path = filepath

        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.headers = reader.fieldnames or []
            self.data = [row for row in reader]

        self.rows = len(self.data)
        self.cols = len(self.headers)

    def show(self, output_type: str = "top", rows: int = 5, separator: str = ",") -> None:
        """
        Вывод данных
        
        :param output_type: 'top', 'bottom', 'random' (по умолчанию 'top')
        :param rows: количество строк для вывода (по умолчанию 5)
        :param separator: разделитель колонок (по умолчанию ',')
        """
        if not self._check_data():
            return

        rows_to_show = self._select_rows(output_type, rows)
        col_widths = self._calculate_column_widths(rows_to_show)
        self._validate_row_count(rows, len(rows_to_show))
        
        self._print_output(rows_to_show, col_widths, separator)

    def info(self) -> None:
        """
        Выводит статистику данных

        :output: Поле, Заполненость, Тип данных
        """

        if not self._check_data(): return

        field_lenght = len(max(self.headers, key=len))

        print(f"Размерность файла: {self.rows}x{self.cols}")
        print(f"{'Поле':<{field_lenght}} {'Заполненость':<12} {'Тип':<10}")
        print("-" * (field_lenght + 12 + 10))

        for header in self.headers:
            non_empty = 0
            types = set()

            for row in self.data:
                value = row.get(header, "")
                if not value: continue

                non_empty += 1
                types.add(self._detect_type(value))

            main_type = "str" if not types else next(iter(types))
            print(f"{header:<{field_lenght}} {non_empty:<12} {main_type:<10}")

    def del_nan(self) -> None:
        """
        Удаляет строки с пустыми значениями
        """

        if not self._check_data(): return

        self.data = [row for row in self.data if all(row.get(header, "") != "" for header in self.headers)]
        removed = self.rows - len(self.data)

        logger.info(f"Удалено {removed} строк с пустыми значениями. Осталось {len(self.data)} строк.")

    def make_ds(self) -> None:
        """
        Разделяет данные и сохраняет их в директорию workdata
        
        /train.csv - 70% обучение

        /test.csv - 30% тестирование
        """

        if not self._check_data(): return

        base_dir = "workdata"
        os.makedirs(base_dir, exist_ok=True)

        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))

        train_data = self.data[:split_idx]
        test_data = self.data[split_idx:]

        train_path = os.path.join(base_dir, "train.csv")
        test_path = os.path.join(base_dir, "test.csv")

        self._write_file(train_path, train_data)
        self._write_file(test_path, test_data)

        print(f"Данные успешно разделены и сохранены:")
        print(f"Обучающая выборка: {len(train_data)} строк -> {train_path}")
        print(f"Тестовая выборка: {len(test_data)} строк -> {test_path}")

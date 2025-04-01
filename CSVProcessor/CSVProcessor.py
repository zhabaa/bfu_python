import os
import csv
import random
import logging
from typing import List, Dict, Union, Optional

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

logger = logging.getLogger(__name__)


class CSVProcessor:
    def __init__(self, file_path: str):
        """
        :param file_path: Путь к CSV файлу
        """

        self.file_path = file_path
        self.data: List[Dict[str, Union[str, int, float]]] = []
        self.headers: List[str] = []
        self._load_data()

    def _load_data(self) -> None:
        with open(self.file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            self.headers = reader.fieldnames or []
            self.data = [row for row in reader]

    def show(self, output_type: str = "top", rows: int = 5, separator: str = ",") -> None:
        """
        Вывод данных

        :param output_type: 'top', 'bottom' или 'random' - откуда брать строки
        :param rows: количество строк для вывода
        :param separator: разделитель между колонками
        """

        if not self.data:
            logger.info("Нет данных для отображения")
            return

        match output_type:
            case "top":
                rows_to_show = self.data[:rows]
            case "bottom":
                rows_to_show = self.data[-rows:]
            case "random":
                rows_to_show = random.sample(self.data, min(rows, len(self.data)))
            case _:
                logger.info(
                    f"Неизвестный тип вывода: {output_type}. Используется 'top'"
                )
                rows_to_show = self.data[:rows]

        if len(rows_to_show) < rows:
            logger.info(f"Внимание: запрошено {rows} строк, но доступно только {len(rows_to_show)}")

        col_widths = {header: len(header) for header in self.headers}

        for row in rows_to_show:
            for header in self.headers:
                col_widths[header] = max(
                    col_widths[header], len(str(row.get(header, "")))
                )

        header_line = separator.join([f"{header:<{col_widths[header]}}" for header in self.headers])

        print(header_line)
        print("-" * len(header_line))

        for row in rows_to_show:
            row_line = separator.join([f"{str(row.get(header, '')):<{col_widths[header]}}" for header in self.headers])
            print(row_line)

    def info(self) -> None:
        """Выводит статистику о данных"""

        if not self.data:
            logger.info("Нет данных для анализа")
            return

        rows = len(self.data)
        cols = len(self.headers)

        print(f"{rows}x{cols}")

        print("\nСтатистика по колонкам:")
        print(f"{'Поле':<15} {'Заполнено':<10} {'Тип':<10}")
        print("-" * 35)

        for header in self.headers:
            non_empty = 0
            types = set()

            for row in self.data:
                value = row.get(header, "")

                if value != "":
                    non_empty += 1

                    try:
                        int(value)
                        types.add("int")

                    except ValueError:
                        try:
                            float(value)
                            types.add("float")

                        except ValueError:
                            types.add("str")

            main_type = "str" if not types else next(iter(types))
            print(f"{header:<15} {non_empty:<10} {main_type:<10}")

    def del_nan(self) -> None:
        """Удаляет строки с пустыми значениями"""

        if not self.data:
            logger.info("Нет данных для обработки")
            return

        initial_count = len(self.data)
        self.data = [
            row
            for row in self.data
            if all(row.get(header, "") != "" for header in self.headers)
        ]
        removed = initial_count - len(self.data)
        logger.info(
            f"Удалено {removed} строк с пустыми значениями. Осталось {len(self.data)} строк."
        )

    def make_ds(self) -> None:
        """
        Разделяет данные на обучающую и тестовую выборки (70%/30%)
        и сохраняет их в папки workdata/Learning и workdata/Testing
        """

        if not self.data:
            logger.info("Нет данных для разделения")
            return

        base_dir = "workdata"
        learning_dir = os.path.join(base_dir, "Learning")
        testing_dir = os.path.join(base_dir, "Testing")

        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)

        random.shuffle(self.data)
        split_idx = int(0.7 * len(self.data))
        train_data = self.data[:split_idx]
        test_data = self.data[split_idx:]

        train_path = os.path.join(learning_dir, "train.csv")
        with open(train_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(train_data)

        test_path = os.path.join(testing_dir, "test.csv")
        with open(test_path, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(test_data)

        print(f"Данные успешно разделены и сохранены:")
        print(f"Обучающая выборка: {len(train_data)} строк -> {train_path}")
        print(f"Тестовая выборка: {len(test_data)} строк -> {test_path}")

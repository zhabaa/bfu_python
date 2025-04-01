from CSVProcessor import CSVProcessor

csv_file = CSVProcessor(file_path='test.csv')
csv_file._load_data()


print('\n' * 2)
print("Показываем первые 5 строк ===")
csv_file.show()
print('\n' * 2)
    
print("Показываем 3 случайные строки ===")
csv_file.show(output_type='random', rows=3)
print('\n' * 2)

print("Выводим информацию о данных")
csv_file.info()
print('\n' * 2)

print("Удаляем строки с пустыми значениями ===")
csv_file.del_nan()
print('\n' * 2)

print("Разделяем данные на обучающую и тестовую выборки ===")
csv_file.make_ds()
print('\n' * 2)
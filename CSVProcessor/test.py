import csv_processor

processor = csv_processor.CSVProcessor()
processor.load_data("test.csv")

processor.info()
# processor.del_nan()
# processor.make_ds()
print('\n')
processor.show(output_type='top', rows=1, separator=';')
print('\n')
processor.show(output_type='bottom', rows=3, separator='|')
print('\n')
processor.show(output_type='random', rows=5, separator='-')
print('\n')
processor.show()


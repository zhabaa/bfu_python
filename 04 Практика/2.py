input_dict = {"Hello": "Hi", "Bye": "Goodbye", "List": "Array"}

value = input()

for key, val in input_dict.items():
    if val == value:
        print(key)

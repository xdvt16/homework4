my_string = input("Любая строка: ")
print(f'Количество символов введённого текста: {len(my_string.replace(" ", ""))}')  # Без учёта пробелов.
print(f'Строка в верхнем регистре: {my_string.upper()}')
print(f'Строка в нижнем регистре: {my_string.lower()}')
print(f'Строка, где удалены все пробелы: {my_string.replace(" ", "")}')
print(f'Первый символ строки: {my_string[0]}')
print(f'Псоледний символ строки: {my_string[-1]}')

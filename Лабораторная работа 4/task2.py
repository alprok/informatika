# TODO импортировать необходимые молули
import json # Импортируем модуль для работы с файлами json
import csv # Импортируем модуль для работы с файлами csv

INPUT_FILENAME = "C:\Course Python английский\Работа с источниками данных\Лабораторная работа\Конвертер из CSV в JSON формат\input.csv" # Путь к файлу
OUTPUT_FILENAME = "output.json" # :)

def task(csv_filename, delimiter=','): # Создаём функцию принимающую путь и разделитель
    ...  # TODO считать содержимое csv файла
    with open(csv_filename, 'r', encoding = 'utf-8') as csv_file: # Открываем файл для чтения и сохраним его в переменную csv_file
        reader = csv.DictReader(csv_file, delimiter = delimiter) # Преобразование строк в словари

        data = [row for row in reader] # Составление списка из получившихся словарей

    json_string = json.dumps(data, ensure_ascii = False, indent = 4) # Составления json строк из получившегося списка словарей
    print(json_string, end='') # Вывод на печать

if __name__ == "__main__": # Проверка запуска в этом файле
    task(INPUT_FILENAME) # Вызов функции
# TODO решите задачу

import json # Импортируем модуль для работы с файлами json

def task(json_file): # Создадим функцию
    with open(json_file, 'r', encoding = 'utf-8') as file: # Откроем наш файл для чтения и сохраним его в переменной file
        data = json.load(file) # Считываем данные из файла json

    total_sum = 0 # Зададим перемнную для суммы

    for item in data: # Введём цикл для прогона всех элементов файла
        score = item.get('score') # Получаем значение по ключу
        weight = item.get('weight') # Получаем значение по ключу
        total_sum += score * weight # Считаем сумму

    return round(total_sum, 3) # Возвращаем сумму округлённую до 3 знаков
if __name__ == "__main__": # Проверка запуска в этом файле
    file_path = r"C:\Course Python английский\Работа с источниками данных\Лабораторная работа\Найти сумму произведений из списка словарей\input.json" # Путь к файлу
    result = task(file_path) # Присвоим функции файл
    print(result) # Вывод на печать

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
def spisok(sp, it): # Введём функцию
    if it in sp: # Отбор товаров, которые есть в списке
        return sp.index(it) # Возвращение индексов этих товаров
    else:
        return None # Возвращения пустого числа если товара нет

for find_item in ['банан', 'груша', 'персик']:
    index_item = spisok(items_list, find_item) # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
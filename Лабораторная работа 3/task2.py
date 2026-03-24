participants_first_group = "Иванов,Петров,Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"
def find_common_participants(gr1, gr2, razd=','): # Введём функцию для нахождения общих участников
    grup1 = gr1.split(razd) # Разбиение первой групы по отдельным именам через разделитель
    grup2 = gr2.split(razd) # Разбиение второй групы по отдельным именам через разделитель
    common = set(grup1) & set(grup2) # Нахождение общих участников в двух грапах
    return sorted(common) # Возвращение имён участников, находящихся в обоих командах, сортированные по алфавиту
rez = find_common_participants(participants_first_group, participants_second_group) # Присвоение перемнной значения функции
print(rez) # Вывод на печать

# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
import random

#base_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def new_list(base_list):
    my_list = []
    j = 1
    while j < len(base_list):
        i = base_list[j]
        if i > base_list[j-1]:
            my_list.append(i)
        j += 1
    return my_list


base_list = [random.randint(1, 200) for i in range(1, 10)]
print(base_list)
print(new_list(base_list))
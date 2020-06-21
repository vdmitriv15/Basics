# а) итератор, генерирующий целые числа, начиная с указанного

import itertools


def iter_num():
    for i in itertools.count(3):
        if i > 11:
            break
        else:
            print(i)


iter_num()

print('***************************')
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.


def iter_list(my_list):
    new_list = []
    j = 0
    for el in itertools.cycle(my_list):
        if j > 15:
            break
        new_list.append(el)
        j += 1
    return new_list


print(iter_list([1, 2, 3]))

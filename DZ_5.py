# Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
# чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
# чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
# программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.


def list_sum(my_list):
    my_list_integer = []
    for i in my_list:
        try:
            el = int(i)
            my_list_integer.append(el)
        except ValueError:
            print('Ошибка ввода данных! Вводите только числа')
            my_list.remove(i)
    result = sum(my_list_integer)
    return result


def inp_list():
    my_list = []
    while True:
        my_list_inp = input("введите строку чисел, разделенных пробелом ").split()
        my_list.extend(my_list_inp)
        if "EXIT" in my_list:
            my_list = my_list[:-1]
            result = list_sum(my_list)
            print(my_list)
            print(result)
            break
        print(my_list)
        result = list_sum(my_list)
        print(result)


inp_list()


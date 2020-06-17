# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.


def my_division(d_1, d_2):
    try:
        result = int(d_1) / int(d_2)
    except ZeroDivisionError:
        print('Ошибка! Деление на "0"')
    else:
        return result


d_1 = input("делимое ")
d_2 = input("делитель ")
print(my_division(d_1, d_2))

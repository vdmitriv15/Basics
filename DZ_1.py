# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
import numpy


def get_str_matrix(matrix):
    return str(matrix).replace('[', ' ').replace(']', ' ')


class Matrix:
    def __init__(self, my_matrix):
        self.my_matrix = my_matrix

    def __str__(self):
        return str(self.my_matrix).replace('[', ' ').replace(']', '\n').replace(',', ' ')

    def __add__(self, other):
        return numpy.array(self.my_matrix) + numpy.array(other.my_matrix)

    # def get_matrix(self):
    #     return numpy.array(self.my_matrix)


mt_1 = Matrix([[1, 2, 11, 2], [1, 2, 1, 6], [1, 5, 1, 3]])
print(mt_1)
mt_2 = Matrix([[4, 2, 1, 1], [2, -3, 3, 1], [1, 1, 5, 1]])
print(mt_2)
mt_3 = mt_1 + mt_2
# print(mt_3)
print(get_str_matrix(mt_3))



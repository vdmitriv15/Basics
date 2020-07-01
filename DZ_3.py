# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.


class Cell:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return '*' * self.number

    def __add__(self, other):
        return '*' * (self.number + other.number)

    def __sub__(self, other):
        if self.number >= other.number:
            return '*' * (self.number - other.number)
        else:
            return '*' * (other.number - self.number)

    def __mul__(self, other):
        return '*' * (self.number * other.number)

    def __truediv__(self, other):
        try:
            return '*' * (self.number // other.number)
        except ZeroDivisionError:
            return f"ZeroDivisionError"

    def make_order(self, num_in_row):
        for i in range(0, self.number//2):
            if num_in_row <= self.number:
                print('*' * num_in_row)
                self.number -= num_in_row
            else:
                print('*' * self.number)
                break


cell_1 = Cell(15)
print("1.")
print(cell_1)
print("2.")
cell_2 = Cell(5)
print(cell_2)
print("sum")
print(cell_1 + cell_2)
print("difference")
print(cell_1 - cell_2)
print("multiplication")
print(cell_1 * cell_2)
print("division")
print(cell_1 / cell_2)
print("method make_order")
cell_1.make_order(7)



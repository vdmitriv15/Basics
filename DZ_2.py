# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

from abc import ABC, abstractmethod


class Clothe(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothe):
    def __init__(self, size):
        self.size = size

    def consumption(self):
        material = self.__size / 6.5 + 0.5
        return material

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        size_chart = [40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60]
        for i in range(0, len(size_chart)):
            if size <= size_chart[0]:
                self.__size = size_chart[0]
            elif size_chart[i-1] < size <= size_chart[i]:
                self.__size = size_chart[i]
            else:
                self.__size = size


class Costume(Clothe):
    def __init__(self, rise):
        self.rise = rise

    def consumption(self):
        material = 2 * self.rise + 0.3
        return material

    @property
    def rise(self):
        return self.__rise

    @rise.setter
    def rise(self, rise):
        rise_chart = [164, 170, 176, 182, 188]
        for i in range(0, len(rise_chart)):
            if rise <= rise_chart[0]:
                self.__rise = rise_chart[0]
            elif rise_chart[i - 1] < rise <= rise_chart[i]:
                self.__rise = rise_chart[i]
            else:
                self.__rise = rise


my_1 = Coat(47)
print(f"you size is {my_1.size}")
print(f"{my_1.consumption():.2f} sm of material for coat")
print("..................")
my_2 = Costume(197)
print(f"you rise is {my_2.rise} for")
print(f"{my_2.consumption():.2f} sm of material for costume")
print("..................")
print(f"{my_1.consumption() + my_2.consumption():.2f} sm")
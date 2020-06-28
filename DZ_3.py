# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, first_name, last_name, position, wage, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": self.wage, "bonus": self.bonus}


class Position(Worker):
    def get_full_name(self):
        print(f"{self.first_name} {self.last_name}")

    def get_income(self):
        print(f"Income - {sum(self._income.values())}")


worker_1 = Position("Ivan", "Petrov", "developer", 50000, 20000)
worker_1.get_full_name()
worker_1.get_income()
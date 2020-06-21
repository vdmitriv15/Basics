# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.

from sys import argv


def salary_func(number_of_hours, rate_per_hour, bonus):
    salary = int(number_of_hours) * int(rate_per_hour) + int(bonus)
    return salary


script_name, number_of_hours, rate_per_hour, bonus = argv
print("Имя скрипта: ", script_name)
print("Выработка в часах: ", number_of_hours)
print("Ставка в час: ", rate_per_hour)
print("Премия: ", bonus)
print(f"Заработная плата: {salary_func(number_of_hours, rate_per_hour, bonus)}")




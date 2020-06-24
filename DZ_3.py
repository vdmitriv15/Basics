# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников

all_salary = 0
j = 0
with open("text_3.txt", "r", encoding="utf-8") as f:
    rate = f.readlines()
    for i in rate:
        name, value = i.split()
        salary = float(value)
        if salary < 20000:
            print(name, value)
        all_salary += salary
        j += 1
average_salary = all_salary / j
print(f"средняя зарплата {average_salary}")


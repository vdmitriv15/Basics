# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("text_5.txt", "w+", encoding="utf-8") as base_f:
    base_f.write(input("введите числа через пробел: "))
    base_f.seek(0)
    try:
        num_list = [int(i) for i in base_f.read().split()]
        result = sum(num_list)
        print(f"сумма чисел {result}")
    except ValueError:
        print("Ошибка ввода")


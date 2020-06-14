# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list.

while True:
    month = input("введите месяц в виде целого числа от 1 до 12: ")

    winter = ["12", "1", "2"]
    spring = ["3", "4", "5"]
    summer = ["6", "7", "8"]
    fall = ["9", "10", "11"]

    if month in winter:
        print("зима")
        break
    elif month in spring:
        print("весна")
        break
    elif month in summer:
        print("лето")
        break
    elif month in fall:
        print("осень")
        break
    else:
        print("некоректный ввод")


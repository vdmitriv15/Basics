# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def my_client(first_name, last_name, year_of_birth, city, email, phone):
    """записал результат ввиде словаря"""
    client = {
        'имя': first_name,
        'фамилия': last_name,
        'год рождения': year_of_birth,
        'город проживания': city,
        'email': email,
        'телефон': phone
    }
    return client


print(my_client(first_name='Ivan', last_name='Petrov', year_of_birth=1976, city='Moskow', email='dghfj@gmail.com', phone=356777543))

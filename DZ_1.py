# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — 7 секунд.  Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
import time
from colorama import Back


class TrafficLight:

    __color = "Red", "Yellow", "Green"

    def running(self):
        count = 0
        while count < 5:
            print(Back.RED + self.__color[0])
            time.sleep(7)
            print(Back.YELLOW + self.__color[1])
            time.sleep(2)
            print(Back.GREEN + self.__color[2])
            time.sleep(7)
            print(Back.YELLOW + self.__color[1])
            time.sleep(2)
            count += 1


traffic = TrafficLight()
traffic.running()
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда)
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.color} {self.name} went")

    def stop(self):
        print(f"{self.color} {self.name} stopped")

    def show_speed(self):
        print(f"speed = {self.speed}")

    def turn(self, direction):
        print(f"{self.color} {self.name} turn {direction}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"speed = {self.speed}. WARNING! OVER SPEED!")
            Car.stop(self)
        else:
            Car.show_speed(self)


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"speed = {self.speed}. WARNING! OVER SPEED!")
            Car.stop(self)
        else:
            Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, is_spec_signal_on):
        # super().__init__(self, speed, color, name, is_police) # не понимаю почему эта строчка не работает!!!!!
        Car.__init__(self, speed, color, name, is_police)  # а эта работает
        self.is_spec_signal_on = is_spec_signal_on

    def show_speed(self):
        if self.is_spec_signal_on:
            print("It doesn't matter!!!")
        else:
            Car.show_speed(self)


auto_town_car = TownCar(60, "green", "town car", False)
auto_town_car.go()
auto_town_car.turn("left")
auto_town_car.show_speed()

auto_work_car = WorkCar(50, "white", "work car", False)
auto_work_car.go()
auto_work_car.turn("right")
auto_work_car.show_speed()

auto_police_car = PoliceCar(speed=100, color="blue/white", name="police car", is_police=True, is_spec_signal_on=True)
auto_police_car.go()
auto_police_car.turn("left")
auto_police_car.show_speed()
auto_police_car.stop()

auto_sport_car = SportCar(90, "orange", "sport car", False)
auto_sport_car.go()
auto_sport_car.turn("right")
auto_sport_car.show_speed()
auto_sport_car.stop()

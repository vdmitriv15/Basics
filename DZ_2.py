# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, _length, _width, _weight_per_one_meter=25, _thickness=5):
        self._length = _length
        self._width = _width
        self._weight_per_one_meter = _weight_per_one_meter
        self._thickness = _thickness

    def asphalt_weight(self):
        weight = self._length * self._width * self._weight_per_one_meter * self._thickness
        print(f"потребуется {weight/1000} т. асфальта")


example = Road(20, 5000)
example.asphalt_weight()

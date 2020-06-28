# Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title


class Pen(Stationery):
    def draw(self):
        print(f"work with {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"work with {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"work with {self.title}")


title = input("Choose pen/pencil/handle ").lower()
if title == "pen":
    tool = Pen(title)
    tool.draw()
elif title == "pencil":
    tool = Pencil(title)
    tool.draw()
elif title == "handle":
    tool = Handle(title)
    tool.draw()
else:
    print("Wrong input")

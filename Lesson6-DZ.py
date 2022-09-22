# 1. Создать класс TrafficLight (светофор).
#
#     определить у него один атрибут color (цвет) и метод running (запуск);
#     атрибут реализовать как приватный;
#     в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#     продолжительность первого состояния (красный) составляет 7 секунд,
#     второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#     переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#     проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов.
# При его нарушении выводить соответствующее сообщение и завершать скрипт.

from itertools import cycle
from time import sleep


class TrafficLight:
    _color = ''
    # Между зелёным и красным обязательно должен быть желтый. Безопасность на дорогах важнее условия задачи :)
    __traffic_light_cycle = [('red', 7), ('yellow', 2), ('green', 5), ('yellow', 2)]

    def Running(self):
        i = 0

        for color, pause in cycle(self.__traffic_light_cycle):
            if i > 10  * len(self.__traffic_light_cycle):  # Принудительный выход из цикла
                break

            self.__TrafficLightSwitching(color)
            print(f'{self._color} traffic light is on')
            sleep(pause)
            i += 1

    # Игрался с присвоением значений атрибутам через защищённый метод
    def __TrafficLightSwitching(self, color):
        self._color = color
        pass


a = TrafficLight()

a.Running()



# 2. Реализовать класс Road (дорога).
#
#     определить атрибуты: length (длина), width (ширина);
#     значения атрибутов должны передаваться при создании экземпляра класса;
#     атрибуты сделать защищёнными;
#     определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#     использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
#     толщиной в 1 см*число см толщины полотна;
#     проверить работу метода.
#
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.


class Road:
    __density = 25

    def __init__(self, length, width):
        self.__length = int(length)
        self.__width = int(width)

    def CalculateMass(self, thickness = 1):
        mass = self.__width * self.__length * thickness * self.__density
        return f'Необходимое количество асфальта: {mass / 1000} тонн'


b = Road(5000, 20)

print(b.CalculateMass(5))
print(b.CalculateMass())


# 3. Реализовать базовый класс Worker (работник).
#
#     определить атрибуты: name, surname, position (должность), income (доход);
#     последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
#     {"wage": wage, "bonus": bonus};
#     создать класс Position (должность) на базе класса Worker;
#     в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
#     (get_total_income);
#     проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
#     проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    __income = {'wage': 130000, 'bonus': 60000}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def _getIncome(self):
        return self.__income


class Position(Worker):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)

    def GetFullName(self):
        return f'{self.first_name} {self.last_name}'

    def GetTotalIncome(self):
        wage = self._getIncome().get('wage')
        bonus = self._getIncome().get('bonus')
        income = wage + bonus
        return f'{income}'


p = Position('Dmitriy', 'Matrenin')
print(p.GetFullName())
print(p.GetTotalIncome())


# 4. Реализуйте базовый класс Car.
#
#     у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#     А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
#     повернула (куда);
#     опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#     добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#     для классов TownCar и WorkCar переопределите метод show_speed.
#     При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль поехал'

    def stop(self):
        return f'Автомобиль остановился'

    def turn(self, direction):
        return f'Автомобиль повернул на{direction}'

    def show_speed(self):
        return f'Автомобиль движется со скоростью {self.speed} км/ч'


class TownCar(Car):
    __max_speed = 60

    def __init__(self, name, speed, color):
        super(TownCar, self).__init__(name, speed, color)

    def show_speed(self):
        if self.speed > self.__max_speed:
            return f'Автомобиль движется с превышением скорости на {self.speed - self.__max_speed} км/ч'
        else:
            return super(TownCar, self).show_speed()


class SportCar(Car):
    def __init__(self, name, speed, color):
        super(SportCar, self).__init__(name, speed, color)

    def turn(self, direction):
        super(SportCar, self).turn(direction)


class WorkCar(Car):
    __max_speed = 40

    def __init__(self, name, speed, color):
        super(WorkCar, self).__init__(name, speed, color)

    def show_speed(self):
        if self.speed > self.__max_speed:
            return f'Автомобиль движется с превышением скорости на {self.speed - self.__max_speed} км/ч'
        else:
            return super(TownCar, self).show_speed()


class PoliceCar(Car):
    def __init__(self, name, speed, color):
        super(PoliceCar, self).__init__(name, speed, color, True)


tc = TownCar('LADA', 75, 'white')
sc = SportCar('Ferrary', 120, 'red')
wc = WorkCar('MAN', 35, 'cиний')
pc = PoliceCar('Жигуль', 45, 'Белая с синей полосой')

print(tc.name, tc.speed, tc.color, tc.is_police)
print(sc.name, sc.speed, sc.color, sc.is_police)
print(wc.name, wc.speed, wc.color, wc.is_police)
print(pc.name, pc.speed, pc.color, pc.is_police)

print(tc.go())
print(tc.turn('лево'))
print(tc.turn('право'))
print(tc.show_speed())
print(tc.stop())


# 5. Реализовать класс Stationery (канцелярская принадлежность).
#
#     определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#     создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#     в каждом классе реализовать переопределение метода draw.
#     Для каждого класса метод должен выводить уникальное сообщение;
#     создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = 'канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self):
        self.title = 'ручка'

    def draw(self):
        print(f'Рисует {self.title}')


class Pencil(Stationery):
    def __init__(self):
        self.title = 'карандаш'

    def draw(self):
        print(f'Рисует {self.title}')


class Handle(Stationery):
    def __init__(self):
        self.title = 'маркер'

    def draw(self):
        print(f'Рисует {self.title}')


pen = Pen()
pencil = Pencil()
handle = Handle()

pen.draw()
pencil.draw()
handle.draw()
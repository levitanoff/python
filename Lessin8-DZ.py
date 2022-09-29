# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
#    формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
#    Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
#    Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
#    (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt

class Date:
    day = None
    month = None
    year = None

    def __init__(self, day, month, year):
        try:
            if not self.validate_date(day, month, year):
                raise DateError('Указана некорректная дата')
        except DateError as err:
            print(err)
        else:
            self.day = day
            self.month = month
            self.year = year

    def __str__(self):
        return f'Day:\t{self.day}\nMonth:\t{self.month}\nYear:\t{self.year}'

    @classmethod
    def parse_date(cls, date):
        day, month, year = map(int, date.split('-'))
        return cls(day, month, year)

    @staticmethod
    def validate_date(day, month, year):
        if 1 < day > 31:
            return False

        if 1 < month > 12:
            return False

        if 1970 <= year > 2048:
            return False

        return True


d1 = Date.parse_date('29-09-2022')
d2 = Date.parse_date('35-09-2022')
print(d1)
print(d2)

print(Date.validate_date(29, 9, 2023))
print(Date.validate_date(35, 9, 2023))

# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
#    Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя
#    программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class MyZeroDividionError(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = int(input('Введите делимое: '))

divider = int(input('Введите делитель:'))

try:
    if divider == 0:
        raise MyZeroDividionError('На ноль делить нельзя!')
except MyZeroDividionError as err:
    print(err)
else:
    print(dividend / divider)

# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие
#    только чисел. Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и
#    заполнять список необходимо только числами. Класс-исключение должен контролировать типы данных
#    элементов списка.
#
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам
# не остановит работу скрипта, введя, например, команду «stop». При этом скрипт завершается,
# сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна
# завершаться.


class MyException(Exception):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return f'Введёное значение "{self.num}" не является числом!'


li = []

while True:
    try:
        el = input('Введите число или слово stop для завершения: ').strip()

        if el == 'stop':
            break
        if not el.isdigit():
            raise MyException(el)
    except MyException as err:
        print(err)
    else:
        li.append(el)

print(li)

# 4. Начните работу над проектом «Склад оргтехники».
#    Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
#    классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определите параметры, общие для приведённых типов.
#    В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 4. Начните работу над проектом «Склад оргтехники».
#    Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для
#    классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
#    В базовом классе определите параметры, общие для приведённых типов.
#    В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием.
#    Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в определённое
#    подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
#    а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием.
#    Реализуйте механизм валидации вводимых пользователем данных.
#    Например, для указания количества принтеров, отправленных на склад,
#    нельзя использовать строковый тип данных.
#
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


class Stock:
    def __init__(self):
        self.equipments = {}

    def to_stock(self, *items):
        for item in items:
            if isinstance(item[1], int):
                self.equipments[item[0]] = item[1]

    def get_equipments(self):
        print('Склад')
        for item in self.equipments.items():
            print(f'Остаток {item[0].name}: {item[1]}')

        print('==============================')


class Equipment:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f'Name: {self.name}, Model: {self.model}'


class Printer(Equipment):
    def __init__(self, name, model, print_speed):
        super().__init__(name, model)
        self.print_speed = print_speed
        self.type = 'Printer'


class Scaner(Equipment):
    def __init__(self, name, model, scan_speed):
        super().__init__(name, model)
        self.scan_speed = scan_speed
        self.type = 'Scaner'


class Xerox(Equipment):
    def __init__(self, name, model, copy_speed):
        super().__init__(name, model)
        self.copy_speed = copy_speed
        self.type = 'Xerox'


class Division:
    def __init__(self, name):
        self.equipments = {}
        self.name = name

    def to_division(self, *items):
        for item in items:
            if isinstance(item[1], int):
                self.equipments[item[0]] = item[1]

    def get_equipments(self):
        print(self.name)
        for item in self.equipments.items():
            print(f'Остаток {item[0].name}: {item[1]}')

        print('==============================')


stock = Stock()
div1 = Division('Отдел маркетинга')
div2 = Division('Отдел продаж')

s1 = Scaner('Scan1', 's-2190', 20)
p1 = Printer('Printer', 'P-1234', 40)
x1 = Xerox('Xerox', 'X-4321', 10)

stock.to_stock((s1, 20), (p1, 40), (x1, 10))
div1.to_division((s1, 2), (p1, 4), (x1, 3))
div2.to_division((s1, 4), (p1, 3), (x1, 5))

stock.get_equipments()
div1.get_equipments()
div1.get_equipments()


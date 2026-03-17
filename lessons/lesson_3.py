# Принципы ООП
# Инкапсуляция
# _одно_подчёркивание: атрибут считается защищённым (protected) и не должен изменяться вне класса
# __два_подчёркивания: атрибут считается приватным (private), и его имя искажается, чтобы избежать случайного
#    переопределения в дочерних классах

class Car:
    # инициализатор (конструктор)
    def __init__(self, color, model, speed=0):
        self.color = color
        self.model = model
        self.speed = speed
        self.__fined = False    # оштрафован
        self.__max_speed = 100

    def _test(self):
        print(f"Test car color: {self.color}, {self.__fined}.")

    def __test_2(self):
        print(f"Test private method: {self.__max_speed}.")

    def drive_to(self, destination):
        if not self.__fined:
            print(f"Машина {self.model} едет в {destination}, max speed: {self.__max_speed}")
        else:
            print("Машина оштрафована.")
        self.__test_2()

    def change_color(self, new_color):
        self.color = new_color

    def fine(self):
        self.__fined = True
        print("Машина оштрафована.")

    def pay_fine(self):
        self.__fined = False
        print("Штраф оплачен.")

    # геттер - getter - чтобы получить приватный объект
    def get_max_speed(self):
        return self.__max_speed

    # сеттер - setter - чтобы установить новое значение
    def set_max_speed(self, new_speed):
        if new_speed <= 0:
            raise ValueError(f"wrong value {new_speed} for max_speed")
        self.__max_speed = new_speed

    def set_fined(self, value):
        self.__fined = value

    # геттер
    @property
    def max_speed(self):
        return self.__max_speed

    # сеттер
    @max_speed.setter
    def max_speed(self, value):
        print(f" в сеттере {value}")
        if value <= 0:
            raise ValueError(f"wrong value {value} for max_speed")      # вызывает ошибку
            # print(f"wrong value {value} for max_speed")
            # return        # return предотвращает дальнейшие действия функции
        self.__max_speed = value


car_mustang = Car(color="black", model="Ford Mustang")
car_mustang._test()                 # вызов защищённого атрибута - можно, но не следует
print(car_mustang.color)
car_mustang.drive_to('Karakol')
# print(car_mustang._Car__max_speed)  # вызов приватного атрибута - нельзя оставлять такой код, это просто для проверок
# print(car_mustang.__max_speed)     # ошибка - доступ к приватному атрибуту: вне класса не существует
# car_mustang.__test_2()
# car_mustang.__max_speed = 50      # так делать не правильно: переменная не изменится; может привести к ошибкам
car_mustang.drive_to('Karakol')
# задание:
car_mustang.fine()                  # сделать метод, чтобы штрафовать машину
car_mustang.drive_to('Karakol')     # не едет, т.к. оштрафовали
print("----")
car_mustang.pay_fine()              # чтобы снимать штраф
car_mustang.drive_to('Karakol')
print("--- max speed ---")
print(car_mustang.get_max_speed())
car_mustang.set_max_speed(101)
print(car_mustang.get_max_speed())

print(car_mustang.max_speed)
car_mustang.max_speed = -100
print(car_mustang.max_speed)

# Основы ООП - объектно-ориентированное программирование
# GIT - система контроля версий
# Базы данных - SQL, сохранение данных

class Car:
    # инициализатор (конструктор)
    def __init__(self, color, model):
        self.color = color
        self.model = model

    def drive_to(self, destination):
        print(f"Машина {self.model} едет в {destination}.")

    def change_color(self, new_color):
        self.color = new_color

# self Python обрабатывает сам, это ссылка на верх класса
# нам нужно лишь смотреть на остальные объекты в классе


# Инициализируем/создаём функцию
car1 = Car(color='black', model='Ford Mustang')
car2 = Car(color='red', model='Subaru Forester')
print("Car 1:", car1.color, car1.model)
print("Car 2:", car2.color, car2.model)
# print(type("kjsfjsfj"))     # <class 'str'>
# print(type(12345))          # <class 'int'>
# print(type(car1))           # <class '__main__.Car'>
car1.drive_to("Бишкек")
car1.color = 'red'
print("Car 1:", car1.color, car1.model)
car1.change_color("white")
print("Car 1:", car1.color, car1.model)
car1.max_speed = 240            # задаём уникальный атрибут/свойство объекту
print("Car 1:", car1.color, car1.model)
# print(car2.max_speed)           # AttributeError - мы не задавали такое свойство

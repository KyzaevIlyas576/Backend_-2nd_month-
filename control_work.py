class Animal:
    def __init__(self, name="", age=0):
        self.__name = str()
        self.__age = int()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age


    def make_sound(self):
        print(f"Вы слышите звук: ")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__()      # на всякий случай
        self.name = name
        self.age = age


    def make_sound(self):
        super().make_sound()
        print(f"Собака {self.name} (возраст: {self.age}) лает.")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age


    def make_sound(self):
        super().make_sound()
        print(f"Кошка {self.name} (возраст: {self.age}) мяукает.")


kitty = Cat(name="", age=0)
kitty.name = "Шарик"
kitty.age = 2
kitty.make_sound()

puppy = Dog(name="", age=0)
puppy.name = "Барбос"
puppy.age = 3
puppy.make_sound()

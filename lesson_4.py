# Абстракция
from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def test(self):
        pass
# Абстрактный класс - как шаблон для других классов

# чтобы создать наследственный шаблон, нужно добавить туда все абстрактные методы из родителя
class Dog(Animal):
    def make_sound(self):   # реализация абстрактного метода
        print("гав гав")

    def test(self):
        print("тест: собака")

puppy = Dog()
puppy.make_sound()
puppy.test()

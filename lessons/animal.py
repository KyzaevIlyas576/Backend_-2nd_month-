class Animal:
    def move(self):
        print("Животное двигается")


class Swimming(Animal):
    def move(self):
        super().move()
        print("плавает")

class Flying(Animal):
    def move(self):
        super().move()
        print("летает")

class Duck(Flying, Swimming):
    def move(self):
        super().move()
        print("утка плавает и летает")


duck = Duck()
duck.move()
# MRO - method resolution order (Порядок разрешения метода)
print(Duck.mro())   # Duck -> Flying (1-й родитель) -> Swimming (2-й родитель) -> Animal (если у родителей нет)

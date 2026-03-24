class Distance:
    conversion = {
        'cm': 0.01,
        'dm': 0.1,
        'm': 1,
        'km': 1000
    }

    # инициализация
    def __init__(self, value, unit):
        self.value = value  # значения
        self.unit = unit    # ед. измерения
        if unit not in self.conversion:
            raise ValueError("Неизвестная единица измерения.")

    # строковое представление
    def __str__(self):
        return f"{self.value} {self.unit}"

    # в метры
    def to_meters(self):
        return self.value * self.conversion[self.unit]

    # из метров
    def from_meters(self, meters):
        return meters / self.conversion[self.unit]

    # сложение
    def __add__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно складывать только объекты Distance.")

        # переводим слагаемые в метры и складываем
        total_meters = self.to_meters() + other.to_meters()

        # переводим сумму в единицы первого объекта
        new_value = self.from_meters(total_meters)

        return Distance(new_value, self.unit)

    # доп. задание №1 - вычитание
    def __sub__(self, other):
        if not isinstance(other, Distance):
            raise TypeError("Можно вычитать только объекты Distance.")


        total_meters = self.to_meters() - other.to_meters()

        # доп. задание №2 - проверка на отрицательное значение
        if total_meters < 0:
            raise ValueError("Результат не должен быть отрицательным.")

        new_value = self.from_meters(total_meters)
        return Distance(new_value, self.unit)

    # доп. задание №3 - сравнение
    def __eq__(self, other):    # равно
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() == other.to_meters()

    def __ne__(self, other):    # не равно
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() != other.to_meters()

    def __lt__(self, other):    # меньше, чем
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() < other.to_meters()

    def __le__(self, other):    # меньше или равно
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() <= other.to_meters()

    def __gt__(self, other):    # больше, чем
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() > other.to_meters()

    def __ge__(self, other):    # больше или равно
        if not isinstance(other, Distance):
            return NotImplemented
        return self.to_meters() >= other.to_meters()


# Экземпляры
dist1 = Distance(1, 'cm')
dist2 = Distance(2, 'm')
dist3 = Distance(3, 'km')

print(dist1)
print(dist2)
print(dist3)
print()

# Сложение
dist4 = dist1 + dist2
print(dist4.__str__())

dist5 = dist3 + dist4
print(dist5.__str__())

# Вычитание
dist6 = dist5 - dist1
print(dist6.__str__())
print()

# Сравнение
print(dist6 < dist4)
print(dist4 >= dist6)
print(dist5 == dist1)
print(dist2 <= dist3)
print(dist4 > dist5)

dist_a = Distance(100, 'm')
dist_b = Distance(100, 'km')
print(dist_a != dist_b)
# dist_c = Distance(-100, 'abc')

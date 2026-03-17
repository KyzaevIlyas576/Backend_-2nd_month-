class Distance:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f'{self.value} {self.unit}'

    def sum(self):
        pass

    def conversion(self):
        if self.unit == 'km':
            return self.value / 1.60934


dist1 = Distance(1, 'cm')
dist2 = Distance(2, 'm')
dist3 = Distance(3, 'km')

print(dist1.__str__())
# 1) Создать файл homework_1.py и в нём записать класс Person, для создания объектов. Экземпляры класса Person должны
# иметь name(имя), birth_date(дата рождения), occupation(профессия), higher_education(высшее образование - True/False).


class Person:
    def __init__(self, name, birth_date, occupation, higher_education, gender=""):
        self.name = name
        self.gender = gender.lower()
        self.birth_date = int(birth_date)
        self.occupation = occupation
        self.higher_education = bool(higher_education)
        if higher_education:
            self.higher_education = "есть"
        elif not higher_education:
            self.higher_education = "нет"

    def introduce(self):
        return (f"Меня зовут {self.name}, я {'родилась' if self.gender == 'ж' else 'родился'} в {self.birth_date},"
                f" по профессии {self.occupation}, высшее образование - {self.higher_education}.")
        # return print(f"Меня зовут {self.name}, я {'родилась' if self.gender == 'ж' else 'родился'} в {self.birth_date},"
        #         f" по профессии {self.occupation}, высшее образование - {self.higher_education}.")


# 2) создайте несколько экземпляров класса (2-3 штуки), распечатайте атрибуты каждого экземпляра
person1 = Person(name='Лара Крофт', gender='Ж', birth_date=1968, occupation='путешественница', higher_education=True)
person2 = Person(name='Кызаев Ильяс', gender='М', birth_date=2004, occupation='студент', higher_education=False)
person3 = Person(name="Сергей Есенин", gender='М', birth_date=1987, occupation="писатель и бармен",
                 higher_education=False)

print(f"Человек 1: {person1.name}, {person1.gender}, {person1.birth_date}, {person1.occupation}, "
      f"{person1.higher_education}")
print(f"Человек 2: {person2.name}, {person2.gender}, {person2.birth_date}, {person2.occupation}, "
      f"{person2.higher_education}")
print(f"Человек 3: {person3.name}, {person3.gender}, {person3.birth_date}, {person3.occupation}, "
      f"{person3.higher_education}")
print()     # пустая строка


# 3) так же добавьте метод introduce, в котором экземпляр будет представляться
# (например: меня зовут …, я родился …, по профессии …, высшего образования нет)
print(person1.introduce())
print(person2.introduce())
print(person3.introduce())
# А можно сделать return print() в методе, тогда будет не print(Person.introduce()), а просто Person.introduce().

# Это домашнее задание можно отправить файлом, не через GitHub.

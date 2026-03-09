class Person:
    def __init__(self, name, birth_date, gender="Неизвестно"):
        self.name = name
        self.gender = gender.title()
        self.birth_date = int(birth_date)
        self.__occupation = str()
        self.__higher_education = bool()


    def introduce(self):
        print(f"Меня зовут {self.name}, я {'родилась' if self.gender == 'Ж' else 'родился'} в {self.birth_date},"
                f" по профессии - {self.occupation}, высшее образование - {self.higher_education}.")


    @property
    def occupation(self):
        return self.__occupation

    @occupation.setter
    def occupation(self, occupation):
        self.__occupation = occupation


    @property
    def higher_education(self):
        return self.__higher_education


    @higher_education.setter
    def higher_education(self, higher_education):
        self.__higher_education = "есть" if higher_education else "нет"


class Classmate(Person):
    def __init__(self, name, birth_date, gender, occupation, higher_education, group_name=""):
        super().__init__(name, birth_date, gender)
        self.occupation =  occupation
        self.higher_education = higher_education
        self.group_name = group_name

    def introduce(self):
        print(
            f"{'Мою однокурсницу' if self.gender == 'Ж' else 'Моего однокурсника'} зовут {self.name}, "
            f"{'она родилась' if self.gender == 'Ж' else 'он родился'} в {self.birth_date}, "
            f"по профессии - {self.occupation}, высшее образование - {self.higher_education}. "
            f"{'Её' if self.gender == 'Ж' else 'Его'} группа - {self.group_name}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, gender, hobby=""):
        super().__init__(name, birth_date, gender)
        self.occupation =  occupation
        self.higher_education = higher_education
        self.hobby = hobby

    def introduce(self):
        print(
            f"{'Мою подругу' if self.gender == 'Ж' else 'Моего друга'} зовут {self.name}, "
            f"{'она родилась' if self.gender == 'Ж' else 'он родился'} в {self.birth_date}, "
            f"по профессии - {self.occupation}, высшее образование - {self.higher_education}. "
            f"{'Её' if self.gender == 'Ж' else 'Его'} хобби - {self.hobby}.")


me = Person(name='Кызаев Ильяс', gender='М', birth_date=2004)
me.occupation = 'студент'
me.higher_education = True

classmate1 = Classmate(name='Бексултан', gender='М', birth_date='2005', occupation='студент', higher_education=False,
                       group_name="ПИ-1/1")
classmate2 = Classmate(name='Мухаммед', gender='М', birth_date='2006', occupation='студент', higher_education=False,
                       group_name="ПИ-2/1")
classmate3 = Classmate(name='Айсалкын', gender='Ж', birth_date='2005', occupation='студент', higher_education=False,
                       group_name="ПИ-2/1")

friend1 = Friend(name="Рамиль", gender="М", birth_date="2006", occupation = "студент", higher_education = False,
                 hobby='футбол')
friend2 = Friend(name="Азирет", gender="М", birth_date="2005", occupation = "воспитатель детсада",
                 higher_education = False, hobby='аниме')
friend3 = Friend(name="Даша", gender="Ж", birth_date="2005", occupation = "студент", higher_education = False,
                 hobby='аниме')


me.introduce()

print("\n", "Однокурсники:")
classmate1.introduce()
classmate2.introduce()
classmate3.introduce()

print("\n", "Мои (остальные) друзья:")
friend1.introduce()
friend2.introduce()
friend3.introduce()
print()


people = [me, classmate1, classmate2, classmate3, friend1, friend2, friend3]
print("Доп. задание 1:")
for p in people:
    p.introduce()
print()


class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, gender, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, gender, hobby)
        self.shared_memory = shared_memory


    def introduce(self):
        super().introduce()
        print(f"Наше общее воспоминание: {self.shared_memory}.")

print("Доп. задание 2:")
best_friend = BestFriend(name="Нурдин", gender="М", birth_date="2005", occupation="б. военный", higher_education=False,
     hobby='мирмикипинг (муравьи)', shared_memory='мы ходили с Эдуардом (ещё одним лучшим другом) в кино на Mortal '
                                                     'Kombat; также я навещал их в Карагачёвой роще')
best_friend.introduce()

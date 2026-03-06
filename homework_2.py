# 1. Создайте файл `homework_2.py`
# 2. В этот файл скопируйте **класс** `Person` (только сам класс, без объектов) и добавьте в него метод `introduce()`,
# в котором бы распечатывалось некое сообщение с именем, профессией и т.д.

class Person:
    def __init__(self, name, birth_date, occupation, higher_education, gender="Неизвестно"):
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
        print(f"Меня зовут {self.name}, я {'родилась' if self.gender == 'ж' else 'родился'} в {self.birth_date},"
                f" по профессии - {self.occupation}, высшее образование - {self.higher_education}.")

# 3. Создайте два класса-наследника:
#     - `Classmate` (одноклассник/одногруппник)
#     - `Friend` (друг)
# 4. Добавьте каждому классу **уникальный атрибут**:
#     - `Classmate` — `group_name` (название группы/класса)
#     - `Friend` — `hobby` (хобби)

class Classmate(Person):
    def __init__(self, name, birth_date, occupation, higher_education, gender, group_name=""):
        super().__init__(name, birth_date, occupation, higher_education, gender)
        self.group_name = group_name

    def introduce(self):
        print(
            f"{'Мою однокурсницу' if self.gender == 'ж' else 'Моего однокурсника'} зовут {self.name}, "
            f"{'она родилась' if self.gender == 'ж' else 'он родился'} в {self.birth_date}, "
            f"по профессии - {self.occupation}, высшее образование - {self.higher_education}. "
            f"{'Её' if self.gender == 'ж' else 'Его'} группа - {self.group_name}.")


class Friend(Person):
    def __init__(self, name, birth_date, occupation, higher_education, gender, hobby=""):
        super().__init__(name, birth_date, occupation, higher_education, gender)
        self.hobby = hobby

    def introduce(self):
        print (
            f"{'Мою подругу' if self.gender == 'ж' else 'Моего друга'} зовут {self.name}, "
            f"{'она родилась' if self.gender == 'ж' else 'он родился'} в {self.birth_date}, "
            f"по профессии - {self.occupation}, высшее образование - {self.higher_education}. "
            f"{'Её' if self.gender == 'ж' else 'Его'} хобби - {self.hobby}.")

# 5. В каждом классе-наследнике **переопределите** метод `introduce()`
# (он должен работать немного иначе, чем у `Person`).
# Пусть метод `introduce()` выводит **дополнительную** информацию(атрибуты) для объекта каждого класса
# 6. Создайте:
#     - 2 объекта `Classmate`
#     - 2 объекта `Friend`
# 7. Вызовите метод `introduce()` у каждого объекта

me = Person(name='Кызаев Ильяс', gender='М', birth_date=2004, occupation='студент', higher_education=False)

classmate1 = Classmate(name='Бексултан', gender='М', birth_date='2005', occupation='студент', higher_education=False,
                       group_name="ПИ-1/1")
classmate2 = Classmate(name='Мухаммед', gender='М', birth_date='2006', occupation='студент', higher_education=False,
                       group_name="ПИ-2/1")
classmate3 = Classmate(name='Айсалкын', gender='Ж', birth_date='2005', occupation='студент', higher_education=False,
                       group_name="ПИ-2/1")

friend1 = Friend(name="Рамиль", gender="М", birth_date="2006", occupation="студент", higher_education=False,
                 hobby='футбол')
friend2 = Friend(name="Азирет", gender="М", birth_date="2005", occupation="воспитатель детсада", higher_education=False,
                 hobby='аниме')
friend3 = Friend(name="Даша", gender="Ж", birth_date="2005", occupation="студент", higher_education=False,
                 hobby='аниме')


# Т.к. в методе introduce() - return print(), то можно написать так.
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


# 8. Сделайте коммит, и выполните команду git push, чтобы ваши изменения загрузились на гитхаб.
# Доп. команды есть в презентации., если git push не работает, обращаетесь к ментору.


# **Доп. задание 1:**
# Создайте несколько разных объектов (`Classmate`, `Friend`, `Person`). Поместите их все в один список.
# Затем напишите цикл, который проходит по этому списку и для каждого объекта вызывает метод `introduce()`.

people = [me, classmate1, classmate2, classmate3, friend1, friend2, friend3]
print("Доп. задание 1:")
for p in people:
    p.introduce()
print()


# **Доп. задание 2 :**
# Создайте ещё один класс-наследник `BestFriend`, который наследуется от класса `Friend`.
# Добавьте ему уникальный атрибут, например, `shared_memory` (общее воспоминание). Переопределите метод `introduce()`
# так, чтобы он сначала вызывал родительский метод `introduce()` из класса `Friend`, а затем допечатывал информацию из
# своего уникального атрибута(т.е. shared_memory).

class BestFriend(Friend):
    def __init__(self, name, birth_date, occupation, higher_education, gender, hobby, shared_memory):
        super().__init__(name, birth_date, occupation, higher_education, gender, hobby)
        self.shared_memory = shared_memory


    def introduce(self):
        super().introduce()
        return print(f"Наше общее воспоминание: {self.shared_memory}.")

print("Доп. задание 2:")
best_friend = BestFriend(name="Нурдин", gender="М", birth_date="2005", occupation="б. военный", higher_education=False,
     hobby='мирмикипинг (муравьи)', shared_memory='мы ходили с Эдуардом (ещё одним лучшим другом) в кино на '
                                                  'Mortal Kombat; также я навещал их в Карагачёвой роще')
best_friend.introduce()

class Contact:
    def __init__(self, name, phone_number, id):
        self.name = name
        self.phone_number = phone_number
        self.id = id


    @classmethod
    def validate_phone_number(cls, phone_number):
        if phone_number.isdigit():
            if len(phone_number) != 10:
                return False
            else:
                return True
        else:
            raise ValueError("В номере должны быть только цифры!")


class ContactList:
    all_contacts = []
    last_id = 0


    @classmethod
    def add_contact(cls, name, phone_number):
        if Contact.validate_phone_number(phone_number):                 #1 - проверка номера
            cls.last_id += 1                                                # доп. задание - увеличение last_id
            new_contact = Contact(name, phone_number, cls.last_id)       #2 - создание нового контакта
            cls.all_contacts.append(new_contact)                        #3 - добавление нового контакта
        else:
            raise ValueError(f"В номере цифр: {len(phone_number)}. Должно быть 10.")


    @classmethod
    def remove_contact(cls, id):
        for contact in cls.all_contacts:
            if contact.id == id:
                cls.all_contacts.remove(contact)
                return

        raise ValueError("Нет такого контакта.")


ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")
# ContactList.add_contact("John Doe", "5551234")    # ошибка - цифр не 10

print(ContactList.last_id) # 2

ContactList.remove_contact(1)

for contact in ContactList.all_contacts:
    print(f"{contact.name}\t - \t{contact.phone_number}\t - \tID: {contact.id}")

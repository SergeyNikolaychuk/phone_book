from os import mkdir

try:
    mkdir("data")
except FileExistsError:
    pass

DATAFILE_PATH = "data\\phone_book.data"


class Contact:
    def __init__(self,
                 name: str,
                 surname: str,
                 otche: str,
                 phone_number: str,
                 id: str = None):
        self.name = name
        self.surname = surname
        self.otche = otche
        self.phone_number = phone_number
        self.id = id

    def __repr__(self):
        return f"<{self.id}> {self.name} {self.surname} {self.otche} {self.phone_number}"


# 1 command возвращает список всех контактов
def get_all_data() -> list:
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            contacts_list = []
            for line in datafile:
                contacts_list.append(line[:-1])
        if contacts_list:
            return contacts_list
        return ["Телефонная книга пуста"]
    except FileNotFoundError:
        return ["Телефонная книга пуста"]


# 2 command возвращает статус
def add_contact(contact: Contact) -> str:
    # надо организовать упарвление айдишниками
    contact.id = "1"
    with open(DATAFILE_PATH, 'a', encoding="utf-8") as datafile:
        datafile.write(f"{str(contact)}\n")
    return "Контакт добавлен"


# 3 command возвращает список контактов
def search(find: str) -> list:
    find = find.lower()
    contacts_list = []
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            for line in datafile:
                if find in line.lower():
                    contacts_list.append(line[:-1])
        if contacts_list:
            contacts_list.insert(0, "Найдены следующие контакты:")
            return contacts_list
        return ["Контакт не найден"]
    except FileNotFoundError:
        return ["Телефонная книга пуста"]


# 4 command возвращает статус
def change_contact(id: str, what: str, change: str) -> str:
    return f"<{id=}> <{what=}> Контакт изменён"


# 5 command возвращает статус
def del_contact(id: str) -> str:
    target_contact = None
    contacts_list = []
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            for line in datafile:
                contact_fields = line.split()
                if id != contact_fields[0][1:-1]:
                    contacts_list.append(line)
                else:
                    target_contact = line[:-1]
    except FileNotFoundError:
        return "Телефонная книга пуста"

    if (not target_contact) and (not contacts_list):
        return "Телефонная книга пуста"

    if target_contact:
        with open(DATAFILE_PATH, "w", encoding="utf-8") as datafile:
            for contact in contacts_list:
                datafile.write(contact)
        return f"{target_contact} удалён"
    else:
        return "Контакта с таким id нет"


def get_contact_by_id(id: str) -> list:
    target_contact = None
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            for line in datafile:
                contact_fields = line.split()
                if id == contact_fields[0][1:-1]:
                    target_contact = line[:-1]
                    break
        if target_contact:
            return [target_contact]
        else:
            return ["Контакта с таким id нет"]
    except FileNotFoundError:
        return ["Телефонная книга пуста"]
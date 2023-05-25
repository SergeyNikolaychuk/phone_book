from os import mkdir

try:
    mkdir("data")
except FileExistsError:
    pass

DATAFILE_PATH = "data\\phone_book.data"
FREE_IDS = "data\\free_ids"
LAST_ID = "data\\last_id"


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
            contacts_list.insert(0, "Все контакты:")
            return contacts_list
        return ["Телефонная книга пуста"]
    except FileNotFoundError:
        return ["Телефонная книга пуста"]


# 2 command возвращает статус
def add_contact(contact: Contact) -> str:
    contact.id = get_last_free_id()
    if not contact.id:
        contact.id = get_last_id()
        set_last_id(int(contact.id) + 1)
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
    target_index = None
    target_contact = None
    contacts_list = []
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            i = 0
            for line in datafile:
                contact_fields = line.split()
                if id != contact_fields[0][1:-1]:
                    contacts_list.append(line)
                else:
                    target_index = i
                    target_contact = line[:-1]
                i += 1
    except FileNotFoundError:
        return "Телефонная книга пуста"

    if (not target_contact) and (not contacts_list):
        return "Телефонная книга пуста"

    if target_contact:
        id, name, surname, otche, phone_number = target_contact.split()
        contact_obj = Contact(name=name, surname=surname, otche=otche, phone_number=phone_number, id=id[1:-1])

        if what == "1":
            contact_obj.name = change
        elif what == "2":
            contact_obj.surname = change
        elif what == "3":
            contact_obj.otche = change
        elif what == "4":
            contact_obj.phone_number = change

        contacts_list.insert(target_index, f"{str(contact_obj)}\n")

        with open(DATAFILE_PATH, "w", encoding="utf-8") as datafile:
            for contact in contacts_list:
                datafile.write(contact)
        return f"Контакт изменён, теперь он такой:\n{contact_obj}"
    else:
        return "Контакта с таким id нет"


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
        add_free_id(id)
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


def get_last_id() -> int:
    try:
        with open(LAST_ID) as last_id_file:
            last_id = last_id_file.read()
        if last_id:
            return int(last_id)
        else:
            return 1
    except FileNotFoundError:
        with open(LAST_ID, 'w') as last_id_file:
            last_id_file.write("1")
        return 1


def set_last_id(id: int) -> None:
    with open(LAST_ID, 'w') as last_id_file:
        last_id_file.write(str(id))


def get_free_ids() -> list:
    try:
        with open(FREE_IDS) as free_ids_file:
            free_ids_list = free_ids_file.read().split()
        return free_ids_list
    except FileNotFoundError:
        with open(FREE_IDS, 'w') as free_ids_file:
            pass
        return []


def get_last_free_id() -> int:
    free_ids = get_free_ids()
    if free_ids:
        last_free_id = free_ids.pop()
    else:
        last_free_id = 0
    with open(FREE_IDS, 'w') as free_ids_file:
        free_ids_file.write(" ".join(free_ids))
    return last_free_id


def add_free_id(id: str) -> None:
    with open(FREE_IDS, 'a') as free_ids_file:
        free_ids_file.write(f"{id} ")
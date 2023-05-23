from os import mkdir

try:
    mkdir("data")
except FileExistsError:
    pass

DATAFILE_PATH = "data\\phone_book.data"


# 1 command
def get_all_data() -> list:
    try:
        with open(DATAFILE_PATH, encoding="utf-8") as datafile:
            contacts_list = []
            for line in datafile:
                contacts_list.append(line[:-1])
        return contacts_list
    except FileNotFoundError:
        return ["Your phonebook now is empty"]


# 2 command
def add_contact(contact: str) -> str:
    with open(DATAFILE_PATH, 'a', encoding="utf-8") as datafile:
        datafile.write(f"{contact}\n")
    return "contact was added"
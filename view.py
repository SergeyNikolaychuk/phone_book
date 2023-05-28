def show_help():
    print('Здравствуйте!\n'
          'Наша телефонная книжка обладает следующими функциями\n'
          '1 - Показать телефонную книжку\n'
          '2 - Добавить новый номер\n'
          '3 - Найти человека из книжки\n'
          '4 - Изменить данные контакта\n'
          '5 - Удалить контакт\n'
          '6 - Показать меню\n'
          '7 - Выйти из телефонной книжки')


def show_contacts(date: list):
    for i in date:
        print(i)


def show_status(status: str):
    print(status)


def show_menu():
    print('1 - Показать телефонную книжку\n'
          '2 - Добавить новый номер\n'
          '3 - Найти человека из книжки\n'
          '4 - Изменить данные контакта\n'
          '5 - Удалить контакт\n'
          '6 - Показать меню\n'
          '7 - Выйти из телефонной книжки')


def change_help():
    print('Что бы вы хотели изменить?\n'
          '1 - Имя\n'
          '2 - Фамилия\n'
          '3 - Отчество\n'
          '4 - Номер телефона\n')
    
def mistake():
    print('Увы такой команды нет\n'
          'Введите цифру в рамках меню')
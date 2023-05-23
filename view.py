def show_help():
   print('Здравствуйте!\n'
         'Наша телефонная книжка обладает следующими функциями\n'
         '1 - Показать телефонную книжку\n'
         '2 - Добавить новый номер\n'
         '3 - Найти человека из книжки\n'
         '4 - Изменить номер телефона\n'
         '5 - Удалить номер телефона')


def show_contacts(date: list):
   print('Список контактов')
   for i in date:
    print(i)

def show_status(status: str):
   print(status)


# def error():
#   if name == 
#   print('Произошла ошибка')

# def success(res):
#    print('')


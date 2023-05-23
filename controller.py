import view, model


def start():
    view.show_help()
    while True:
        command = input('Введите команду: ')
        if command == '1':
            data = model.get_all_data()
            view.show_contacts(data)
        elif command == '2':
            name = input('Введите имя контакта: ')
            syrname = input('Введите фамилию контакта: ')
            number_phone = input('Введите номер телефона: ')
            contact =  f"{name} {syrname} {number_phone}"
            status = model.add_contact(contact)
            view.show_status(status)
        elif command == '4':
            break
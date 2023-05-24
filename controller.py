import view, model


def start():
    view.show_help()
    while True:
        command = input('Введите команду: ')
        if command == '1':
            data = model.get_all_data()
            view.show_contacts(data)
        elif command == '2'    
            name = input('Введите имя контакта: ').replace(" ", "")
            surname = input('Введите фамилию контакта: ').replace(" ", "")
            otche = input('Введите отчество конткта: ').replace(" ", "")
            phone_number = input('Введите номер телефона: ').replace(" ", "")
            contact = model.Contact(name=name, surname=surname, otche=otche, phone_number=phone_number)
            status = model.add_contact(contact)
            view.show_status(status)
        elif command == '3':
            find = input('Введите что искать:')
            result = model.search(find)
            view.show_contacts(result) 
        elif command == '4':
            id = input('Введите id контакта')
            view.show_contacts(model.get_contact_by_id(id))
            view.change_help()
            what = input('Введите цифру')
            status = model.change_contact(id, what)
            view.show_status(status)
        elif command == '5': 
            id = input('Введите id контакта')
            status = model.del_contact(id)
            view.show_status(status)          
        elif command == '6': 
            view.show_menu()   
        elif command == '7': 
            break
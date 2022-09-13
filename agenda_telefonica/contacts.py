#-*- coding: utf-8 -*-

import csv

class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    def _save(self):
        with open('contacts.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(('name','phone','email'))

            for contact in self._contacts:
                writer.writerow((contact.name, contact.phone, contact.email))

    def update(self, name, new_name, new_phone, new_email):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                if new_name != '':
                    contact.name = new_name
                if new_phone != '':
                    contact.phone = new_phone
                if new_email != '':
                    contact.email = new_email
            print('*** Contacto Actualizado con exito ****')
            break
        else:
            self._not_found()

    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                break
        else:
            self._not_found()

    def _not_found(self):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('¡NO ENCONTRADO!')
        print('--- * --- * --- * --- * --- * --- * --- * ---')

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * ---')
        print('Nombre: {}'.format(contact.name))
        print('Teléfono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- * ---')

def run():
    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader = csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    while True:
        command = str(raw_input('''
            ¿Que deseas hacer?

            [a]ñadir contacto
            [ac]tualizar contacto
            [b]uscar contacto
            [e]liminar contacto
            [l]istar contactos
            [s]alir
            '''))
        if command == 'a':
            print('añadir contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            phone = str(raw_input('Escribe el telefono del contacto: '))
            email = str(raw_input('Escribe el correo del contacto: '))
            contact_book.add(name,phone,email)
        elif command == 'ac':
            print('actualizar contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            new_name = str(raw_input('Escribe el nombre del contacto: '))
            new_phone = str(raw_input('Escribe el telefono del contacto: '))
            new_email = str(raw_input('Escribe el correo del contacto: '))
            contact_book.update(name, new_name, new_phone, new_email)
        elif command == 'b':
            print('buscar contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.search(name)
        elif command == 'e':
            print('eliminar contacto')
            name = str(raw_input('Escribe el nombre del contacto: '))
            contact_book.delete(name)
        elif command == 'l':
            print('listar contactos')
            contact_book.show_all()
        elif command == 's':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()

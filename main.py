from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit(): # Перевірка числа на 10 знаків
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def find_phone(self, phone): # Пошук телефона за нумером
        number_found = [num for num in self.phones if num.value == phone]
        return number_found[0] if number_found else None
    
    def remove_phone(self, phone): # Видаляємо нумер телефону
        self.phones = [num for num in self.phones if num.value != phone]
        str(f'Number phone {phone} has been delete')
    
    def edit_phone(self, old_phone, new_phone): # Заміна старого нумера на новий
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return
        raise ValueError(f'Phone number {old_phone} not found')
    
    def add_phone(self, phone): # Додавання нумеру
        self.phones.append(Phone(phone))
        str(f'Number phone {phone} has been add')
        

    def __str__(self): # Виводить контакт
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record): # Додавання контакту, ім'я це ключ
        self.data[record.name.value] = record
        str(f'Contact {record} has been add')
    
    def find(self, name): # Пошук контакта
        if name in self.data:
            return self.data[name]
        else:
            str(f'Name {name} is not found')
    
    def delete(self, name): # Видалення контакта
        if name in self.data:
            del self.data[name]
            str(f'The contact {name} has been deleted')
            

if __name__ == "__main__":
    address_book = AddressBook()
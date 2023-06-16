import csv

data = 'info_book.txt'

def creating_info_book():
    file = 'info_book.txt'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'.\n')

def load_info_book():
    info_book = []
    with open(data, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        for row in reader:
            info_book.append(row)
    return info_book

def save_info_book(info_book):
    with open(data, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerows(info_book)

def print_info_book(info_book):
    for record in info_book:
        print('Фамилия:', record[0])
        print('Имя:', record[1])
        print('Отчество:', record[2])
        print('Номер телефона:', record[3])
        print('------------------------------')

def search_info_book(info_book, find):
    results = []
    for record in info_book:
        if find.lower() in record[0].lower() or find.lower() in record[1].lower() or find.lower() in record[2].lower():
            results.append(record)
    return results

def add_record(info_book):
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    middle_name = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_record = [last_name, first_name, middle_name, phone_number]
    info_book.append(new_record)
    save_info_book(info_book)
    print('Запись добавлена успешно.')

def menu():
    info_book = load_info_book()
    while True:
        print('==== Телефонный справочник ====')
        print('1. Вывести все записи')
        print('2. Поиск записей')
        print('3. Добавить запись')
        print('0. Выйти')
        choice = input('Введите номер действия: ')
        print()
        if choice == '1':
            print_info_book(info_book)
        elif choice == '2':
            find = input('Введите фамилию, имя или отчество для поиска: ')
            results = search_info_book(info_book, find)
            if results:
                print('Результаты поиска:')
                print_info_book(results)
            else:
                print('Нет совпадений.')
        elif choice == '3':
            add_record(info_book)
        elif choice == '0':
            break
        else:
            print('Неверный выбор. Пожалуйста, повторите.')

menu()

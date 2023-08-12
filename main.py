import json
import datetime


# Функция для чтения заметок из файла
def read_notes():
    try:
        with open('data.json', 'r') as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []
    return notes


# Функция для записи заметок в файл
def save_notes():
    with open('data.json', 'w') as file:
        json.dump(notes, file, indent=4)


# Функция для добавления новой заметки
def add_note():
    title = input("Enter a header for the note: ")
    body = input("Enter note body: ")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {'id': len(notes) + 1, 'title': title, 'body': body, 'creation_date': current_time,
            'last_modified_date': current_time}
    notes.append(note)
    save_notes()
    print("\nNote added successfully\n")


# Функция для редактирования существующей заметки
def edit_note():
    id = int(input("Enter note ID: "))
    for note in notes:
        if note['id'] == id:
            title = input("Enter a new note header: ")
            body = input("Enter a new note body: ")
            note['title'] = title
            note['body'] = body
            note['last_modified_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes()
            print("Note successfully edited")
    return print("Note with specified ID not found !")


# Функция для удаления заметки
def delete_note():
    id = int(input("Enter note ID: "))
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
            save_notes()
            print("Note successfully deleted")
    return print("Note with specified ID not found !")


# Функция для вывода списка заметок
def list_notes():
    filter_date_str = input("Enter a date to filter (yyyy-mm-dd): ")
    filter_date = datetime.datetime.strptime(filter_date_str, "%Y-%m-%d").date()
    for note in notes:
        creation_date = datetime.datetime.strptime(note['creation_date'], "%Y-%m-%d %H:%M:%S").date()
        if creation_date >= filter_date:
            print()
            print(f"ID: {note['id']}")
            print(f"Header: {note['title']}")
            print(f"Body: {note['body']}")
            print(f"Creation Date: {note['creation_date']}")
            print(f"Last Modified Date: {note['last_modified_date']}")
            print()
        else:
            print('Date entered incorrectly!')


# Загрузка заметок из файла
notes = read_notes()
# Цикл для работы с командами пользователя
while True:
    print('-' * 25)
    print("Available commands:")
    print('-' * 16)
    print("1. List of notes")
    print("2. Add note")
    print("3. Edit note")
    print("4. Delete note")
    print("5. Exit")
    print('-' * 16)
    command = input("Enter command number: ")
    if command == '1':
        list_notes()
    elif command == '2':
        add_note()
    elif command == '3':
        edit_note()
    elif command == '4':
        delete_note()
    elif command == '5':
        print("Exiting the application")
        break
    else:
        print('-' * 25)
        print("Invalid command. Re-enter.")

import datetime

print("Hello, World!")


def get_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            day, month, year = map(int, date_str.split('-'))
            return datetime.date(year, month, day)
        except ValueError:
            print("Неверный формат даты. Используйте DD-MM-YYYY")


def add_note():
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    while True:
        status = input("Введите статус заметки (новая, в процессе, выполнено): ").lower()
        if status in ["новая", "в процессе", "выполнено"]:
            break
        else:
            print("Неверный статус. Выберите из списка: новая, в процессе, выполнено")
    creation_date = get_date_input("Введите дату создания (DD-MM-YYYY): ")
    deadline = get_date_input("Введите дедлайн (DD-MM-YYYY): ")

    return {
        "user_name": user_name,
        "title": title,
        "description": description,
        "status": status,
        "creation_date": creation_date.strftime("%d-%m-%Y"),
        "deadline": deadline.strftime("%d-%m-%Y")
    }


print("Добро пожаловать в \"Менеджер заметок\"!")

notes = []
while True:
    notes.append(add_note())
    another_note = input("Хотите добавить ещё одну заметку? (да/нет): ").lower()
    if another_note != "да":
        break


print("\nСписок заметок:")
for i, note in enumerate(notes):
    print(f"\n{i+1}. Имя: {note['user_name']}")
    print(f"   Заголовок: {note['title']}")
    print(f"   Описание: {note['description']}")
    print(f"   Статус: {note['status']}")
    print(f"   Дата создания: {note['creation_date']}")
    print(f"   Дедлайн: {note['deadline']}")



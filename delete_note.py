print("Hello, World")

notes = []


def add_note():
    """Добавляет новую заметку в список."""
    user_name = input("Введите имя пользователя: ")
    title = input("Введите заголовок заметки: ")
    description = input("Введите описание заметки: ")
    notes.append({"user_name": user_name, "title": title, "description": description})
    print("Заметка добавлена!")


def show_notes(notes1):
    """Отображает список заметок."""
    if not notes1:
        print("Список заметок пуст.")
        return
    for i, note in enumerate(notes1):
        print(f"{i+1}. Имя: {note['user_name']}, Заголовок: {note['title']}, Описание: {note['description']}")


def delete_note(notes2):
    """Удаляет заметку из списка."""
    show_notes(notes2)
    if not notes2:
        print("Список заметок пуст. Нечего удалять.")
        return notes2

    while True:
        try:
            note_number = int(input("Введите номер заметки для удаления (или 0 для отмены): "))
            if note_number == 0:
                return notes2
            note_index = note_number - 1
            if 0 <= note_index < len(notes2):
                deleted_note = notes2.pop(note_index)
                print(f"Заметка '{deleted_note['title']}' удалена.")
                return notes2
            else:
                print("Неверный номер заметки. Попробуйте еще раз.")
        except ValueError:
            print("Неверный формат ввода. Введите число.")
        except Exception as e:
            print(f"Произошла неизвестная ошибка: {e}")
            return notes2


def main():
    """Основная функция программы."""
    while True:
        action = input("Выберите действие (добавить/удалить/показать/выход): ").lower()
        if action == "добавить":
            add_note()
        elif action == "удалить":
            delete_note(notes)
        elif action == "показать":
            show_notes(notes)
        elif action == "выход":
            break
        else:
            print("Неизвестное действие. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()



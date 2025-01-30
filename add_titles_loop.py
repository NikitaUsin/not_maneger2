print("Hello, World!")


def add_unique_titles():
    """
    Позволяет  добавлять заголовки выводит их список.
    """

    titles = []  # Список для хранения добавленных заголовков
    title_number = 1  # Счетчик заголовков

    while True:
        title = input(f"Введите заголовок заметки {title_number} (или пустую строку для завершения): ")
        if not title:  # Проверяем, ввел ли пользователь пустую строку
            break  # Завершаем цикл, если введена пустая строка

        if title not in titles:  # Проверяем, есть ли уже такой заголовок в списке
            titles.append(title)  # Добавляем заголовок в список
            title_number += 1  # Увеличиваем счетчик
        else:
            print("Такой заголовок уже существует. Введите другой.")

    if titles:  # Проверяем, что был хотя бы один заголовок
        print("\nСписок добавленных заголовков:")
        for index, title in enumerate(titles, start=1):  # выводим заголовки с порядковыми номерами
            print(f"{index}. {title}")
    else:
        print("\nВы не добавили ни одного заголовка.")


if __name__ == "__main__":
    add_unique_titles()


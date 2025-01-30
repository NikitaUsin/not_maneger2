import datetime

print('Hello, World!')


def is_deadline_passed(deadline_str):
    try:
        deadline1 = datetime.datetime.strptime(deadline_str, "%Y-%m-%d")  # Измененный формат
        today = datetime.date.today()  # Получаем сегодняшнюю дату
        return today > deadline1.date()  # Сравниваем даты
    except ValueError:
        print("Неправильный формат даты! Используй YYYY-MM-DD")
        return None  # возвращаем None если дата неверная


deadline = "2024-05-21"  # Измененный формат даты
result = is_deadline_passed(deadline)

if result is None:
    print("Ошибка ввода даты")
elif result:
    print("Дедлайн пропущен!")
else:
    print("Дедлайн еще не наступил.")


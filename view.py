import datetime


def get_mode() -> int:
    """
    Формирование шапки меню
    :return: номер выбранного пункта
    """
    print("=" * 20)
    print("Выберите необходимое действие: ")
    print("1. Создать Заметку")
    print("2. Вывести список всех Заметок")
    print("3. Найти Заметку по датам")
    print("4. Найти и вывести Заметку на экран")
    print("5. Редактировать Заметку")
    print("6. Удалить Заметку")
    print("7. Закончить работу")
    print("=" * 20 + "\n")
    return int(input("Введите номер необходимого действия: "))


def get_add_new_note():
    """
    ввод новой заметки
    :return: возвращает новую заметку в ввиде списка словарей, где ключ это название поля
    """
    print("Введите данные: ")
    new_note = []
    temp = {}
    temp["id_note"] = "temp"
    temp["title_note"] = input("Введите заголовок: ")
    temp["text_note"] = input("Введите текст: ")
    temp["date_note"] = datetime.datetime.now()
    new_note.append(temp)
    return new_note


def print_to_screen(notes_arr: list):
    """
    Распечатка всех заметок из заданного списка, отсортированного от более новой заметке к более старым
    :param notes_arr:
    """
    sorted_notes_arr = sorted(notes_arr, key=lambda x: x["date_note"], reverse = True)
    for note in sorted_notes_arr[:]:
        print("ID    - " + note["id"])
        print("Title - " + note["title_note"])
        print("Text  - " + note["text_note"])
        print("Date  - " + note["date_note"])
        print()


def input_message(prompt) -> str:
    return input(prompt + ": ")


def put_message(promt):
    print(promt)
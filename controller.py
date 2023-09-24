import datetime
import sys

import view as view
import file_work as fw


def start_notes():
    """
    метод формирующий логику меню.
    """
    while True:
        mode = view.get_mode()
        if mode == 1:
            view.put_message("\nВносим Заметку:")
            data_new_note = view.get_add_new_note()
            fw.append_to_csv(fw.get_last_id(), data_new_note)
            view.put_message("Заметка добавлена")

        elif mode == 2:
            data_notes = fw.read_csv()
            view.put_message("\nСписок всех Заметок: \n")
            view.print_to_screen(data_notes)

        elif mode == 3:
            view.put_message("\nИщем Заметки по датам:")
            start_date = datetime.datetime.strptime(view.input_message("\nВведите начальную дату (дд/мм/гггг )"), "%d/%m/%Y")
            end_date = datetime.datetime.strptime(view.input_message("\nВведите конечную дату (дд/мм/гггг )"), "%d/%m/%Y")
            view.put_message("\nНайденные по датам Заметки: \n")
            view.print_to_screen(find_notes_by_dates(start_date, end_date))

        elif mode == 4:
            view.put_message("\nИщем Заметку и выводим ее на экран:\n")
            find_note(view.input_message("Введите искомое"))

        elif mode == 5:
            view.put_message("Редактируем Заметку:\n")
            old_id = view.input_message("Введите ID")
            new_note = view.get_add_new_note()
            fw.replacement_note(new_note, old_id)
            view.put_message("Данные сохранены")

        elif mode  == 6:
            view.put_message("Удаляем Записку:\n")
            del_id = view.input_message("Введите ID")
            new_note = find_note_by_id(del_id)
            new_note[0]["title_note"] = "Note deleted"
            new_note[0]["text_note"] = "null"
            fw.replacement_note(new_note, del_id)
            view.put_message("Данные удалены")

        elif mode == 7:
            view.put_message('Всего хорошего!\n')
            sys.exit()
        print('\nДальше?\n')


def find_note(find_data):
    """
    Поиск заметки по названию или содержанию
    :param find_data: зданое название или содержание заметки

    """
    # notes_data = fw.read_csv_to_arr()
    notes_data = fw.read_csv()
    found_list = []
    for note in notes_data:
        if find_data == note["title_note"] or find_data == note["text_note"]:
            found_list.append(note)
    if found_list > []:
        view.put_message('\nНайденные записки ():\n')
        view.print_to_screen(found_list)
    else:
        view.put_message('Искомое не найдено')


def find_note_by_id(num_id) -> list:
    """
    Находит в файле заметку по заданному ID
    :param num_id: задный ID заметки
    :return: возвращает заметку в виде списка
    """
    notes_data = fw.read_csv()
    found_list = []
    for note in notes_data:
        if num_id == note["id"]:
            found_list.append(note)
    return found_list


def find_notes_by_dates(date1, date2) -> list:
    """
    Находит заметки созданных в диапазоне дат date1 и date2
    :param date1: начальная дата
    :param date2: конечная дата
    :return:
    """
    notes_data = fw.read_csv()
    found_list = []
    for note in notes_data:
        date_note = datetime.datetime.strptime(note["date_note"], '%Y-%m-%d %H:%M:%S.%f')
        if date1.date() <= date_note.date() <= date2.date():
            found_list.append(note)
    return found_list
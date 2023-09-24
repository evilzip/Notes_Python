import csv
import datetime


def get_last_id() -> int:
    """
    Функция считает сколько записей уже есть в файле database.csv
    :return: возвращает количество записей в файле database.csv
    """
    with open('database.csv', 'r') as file:
        count_notes = 0
        csv_reader = csv.reader(file)
        for row in csv_reader:
            count_notes += 1
    return count_notes


def append_to_csv(last_id, data_new_note):
    """
    Добавляет новую "заметку" в файл заметок
    :param last_id: номер последней заметке
    :param data_new_note: данные новой заметки
    """
    notes = read_csv()
    temp = {}
    temp["id"] = last_id + 1
    temp["title_note"] = data_new_note[0]["title_note"]
    temp["text_note"] = data_new_note[0]["text_note"]
    temp["date_note"] = datetime.datetime.now()
    notes.append(temp)
    write_csv(notes)


def read_csv() -> list[dict]:
    """
    Метод "читает" файл заметок и формирует список из словарей, в которых содержится информация из каждой заметки

    :return: список словарей
    """
    notes = []
    with open('database.csv', 'r', encoding='utf-8') as fin:
        csv_reader = csv.reader(fin, delimiter=";")
        for row in csv_reader:
            temp = {}
            temp["id"] = row[0]
            temp["title_note"] = row[1]
            temp["text_note"] = row[2]
            temp["date_note"] = row[3]
            notes.append(temp)
    return notes


def write_csv(notes: list):
    """
    Зписывает заметку в файл
    :param notes: заметка представленная в виде списка
    """
    with open('database.csv', 'w', encoding='utf-8', newline="") as fout:
        csv_writer = csv.writer(fout, delimiter=";")
        for note in notes:
            csv_writer.writerow(note.values())



def replacement_note(new_note, id_note):
    """
    Змена полей заметки, которую нужно изменитить. выбор нужно займетки происходит по ID
    :param new_note: список новых значений полей заметки
    :param id_note: ID заметки которую нужно изменить
    """
    full_data = read_csv()
    for note in full_data:
        if note["id"] == id_note:
            note["title_note"] = new_note[0]["title_note"]
            note["text_note"] = new_note[0]["text_note"]
            note["date_note"] = datetime.datetime.now()
            break
    write_csv(full_data)

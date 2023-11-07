from os import system
from sys import exit
from time import sleep

from utils.Note import Note
from constants import SLEEP_TIME, MAX_TITLE_LENGTH, MAX_CONTENT_LENGTH


if __name__ == "__main__":
    note = Note()
    while True:

        # Чистим консоль
        system("cls||clear")

        # Печатаем меню
        print("Менеджер заметок")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Поиск заметок")
        print("4. Удалить заметку")
        print("5. Выход")

        # Получаем данные от пользователя
        choice = input("Выберите действие: ")

        # Проверяем число ли передал пользователь, если да - переводим в int
        if not choice.isdigit():
            print("Нужно выбрать число (пример: 1)\n")
            sleep(SLEEP_TIME)
            continue
        else:
            choice = int(choice)

        # Обрабаываем каждый возможный выбор пользователя
        if choice == 1:
            # Получаем заголовок от пользователя
            title = input("Введите заголовок заметки: ")

            # Проверяем длину заголовка и выше ли она допустимой
            if len(title) > MAX_TITLE_LENGTH:
                print("Слишком большой заголовок.")
                print("Максимальная длина:", MAX_TITLE_LENGTH, "символов.")
                sleep(SLEEP_TIME)
                continue

            # Получаем контент от пользователя
            content = input("Введите контент заметки: ")

            # Проверяем длину контена и выше ли она допустимой
            if len(content) > MAX_CONTENT_LENGTH:
                print("Слишком больщой контент.")
                print("Максимальная длина:", MAX_CONTENT_LENGTH, "символов.")
                sleep(SLEEP_TIME)
                continue

            # Добавляем заметку используя функцию add с класа Note
            note.add(title, content)
            print("Заметка успешно добавлена!")
            sleep(SLEEP_TIME)
            continue
        elif choice == 2:

            # Получаем с базы данных список с кортежами
            # Внутри которого есть id и title заметки
            titles_with_ids = note.get_titles_with_ids()

            # Проверяем есть ли что-то в базе данных
            if len(titles_with_ids) == 0:
                print("Нету заметок в базе данных!")
                sleep(SLEEP_TIME)
                continue

            for item_cortege in titles_with_ids:
                print(f"[{item_cortege[0]}] {item_cortege[1]}")

            note_id = input("Выберите ID заметки, которую хотите посмотреть: ")

            if not note_id.isdigit():
                print("Нужно выбрать число.")
                sleep(SLEEP_TIME)
                continue
            else:
                note_id = int(note_id)

            # Кортеж с даными заметки
            note_cortege = note.get_note_by_id(note_id)

            # Проверяем была ли она в базе данных
            if note_cortege is None:
                print("Не существует такого ID.")
                sleep(SLEEP_TIME)
                continue

            print(f"ID: {note_cortege[0]}")
            print(f"Заголовок: {note_cortege[1]}")
            print(f"Контент: {note_cortege[2]}\n")

            input("Нажмите Enter чтобы попасть в меню")
            continue
        elif choice == 3:
            # Получаем слово или фразу для поиска
            search_phrase = input("Введите фразу для поиска: ")

            # Получаем список заметок с ключевым словом
            notes_list = note.find(search_phrase)

            # Проверяем нашлись ли такие заметки
            if len(notes_list) == 0:
                print("Не нашёл таких заметок.")
                sleep(SLEEP_TIME)
                continue

            for note_cortege in notes_list:
                print(f"ID: {note_cortege[0]}")
                print(f"Заголовок: {note_cortege[1]}")
                print(f"Контент: {note_cortege[2]}\n\n")
            input("Нажмите Enter чтобы попасть в меню")
            continue
        elif choice == 4:
            # Получаем с базы данных список с кортежами
            # Внутри которого есть id и title заметки
            titles_with_ids = note.get_titles_with_ids()

            # Проверяем есть ли что-то в базе данных
            if len(titles_with_ids) == 0:
                print("Нету заметок в базе данных!")
                sleep(SLEEP_TIME)
                continue

            for item_cortege in titles_with_ids:
                print(f"[{item_cortege[0]}] {item_cortege[1]}")

            note_id = input("Выберите ID заметки, которую хотите удалить: ")

            if not note_id.isdigit():
                print("Нужно выбрать число.")
                sleep(SLEEP_TIME)
                continue
            else:
                note_id = int(note_id)

            note.remove(note_id)
            print("Заметка успешно удалена!")
            sleep(SLEEP_TIME)
            continue
        elif choice == 5:
            note.close()
            exit(0)
        else:
            print("Нету такого действия.")
            sleep(SLEEP_TIME)
            continue

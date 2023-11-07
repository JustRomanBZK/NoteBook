from sqlite3 import connect


class Note:
    def __init__(self):
        """
        Инициализация класса Note создаст базу данных или
        подключится к существующей
        """
        self.connection = connect("notes.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                content TEXT
            )
        ''')
        self.connection.commit()

    def add(self, title: str, content: str):
        """
        Функция add добавляет в базу данных новую заметку.
        title -> Заголовок заметки (строка).
        content -> Контент заметки (строка)
        """
        self.cursor.execute(
            "INSERT INTO notes (title, content) "
            "VALUES (?, ?)",
            (title, content)
        )
        self.connection.commit()

    def get_titles_with_ids(self):
        """
        Возвращает список кортежей с идентификаторами и
        заголовками заметок.
        """
        self.cursor.execute("SELECT id, title FROM notes")
        titles_with_ids = self.cursor.fetchall()
        return titles_with_ids

    def get_note_by_id(self, id: int):
        """
        Получает заметку по идентификатору и
        возвращает кортеж (ID, Заголовок, Контент).
        """
        self.cursor.execute(
            "SELECT id, title, content FROM notes "
            "WHERE id = ?",
            (id,)
        )
        note = self.cursor.fetchone()
        return note

    def find(self, keyword: str):
        """
        Ищет фразу в заголовке и контенте заметок и
        возвращает список кортежей заметок, в которых найдена фраза.
        """
        self.cursor.execute(
            "SELECT id, title, content FROM notes "
            "WHERE title LIKE ? OR content LIKE ?",
            (f"%{keyword}%", f"%{keyword}%")
        )
        notes = self.cursor.fetchall()
        return notes

    def remove(self, id: int):
        """Удаляет заметку из базы данных по ID."""
        query = "DELETE FROM notes WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()

    def close(self):
        """Закрывает соединение с базой данных."""
        self.connection.close()

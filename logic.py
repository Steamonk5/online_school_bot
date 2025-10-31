import sqlite3
import random
from config import DATABASE

class DBManager:
    def __init__(self, db_file=DATABASE):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file, check_same_thread=False)
        self.conn.execute('''CREATE TABLE IF NOT EXISTS schedule (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            grade INTEGER NOT NULL,
                            day TEXT NOT NULL,
                            subject TEXT NOT NULL,
                            time TEXT NOT NULL
                            )''')
        self.conn.commit()

    def get_random_lesson(self, day, grade):
        cursor = self.conn.cursor()
        cursor.execute("SELECT subject, time FROM schedule WHERE day=? AND grade=?", (day, grade))
        rows = cursor.fetchall()
        if not rows:
            return "⚠️ Для этого дня/класса уроков не найдено."
        lesson = random.choice(rows)
        return f"🎯 {lesson[0]} — {day} в {lesson[1]}"

    def add_lesson(self, grade, day, subject, time):
        self.conn.execute(
            "INSERT INTO schedule (grade, day, subject, time) VALUES (?, ?, ?, ?)",
            (grade, day, subject, time)
        )
        self.conn.commit()
        return f"✅ Урок добавлен: {subject} для класса {grade} в {day} в {time}"

    def edit_lesson(self, lesson_id, grade=None, day=None, subject=None, time=None):
        cursor = self.conn.cursor()
        cursor.execute("SELECT grade, day, subject, time FROM schedule WHERE id=?", (lesson_id,))
        row = cursor.fetchone()
        if not row:
            return "⚠️ Урок не найден."
        new_values = (
            grade if grade is not None else row[0],
            day if day is not None else row[1],
            subject if subject is not None else row[2],
            time if time is not None else row[3],
            lesson_id
        )
        cursor.execute("UPDATE schedule SET grade=?, day=?, subject=?, time=? WHERE id=?", new_values)
        self.conn.commit()
        return f"✅ Урок ID {lesson_id} обновлён."

    def delete_lesson(self, lesson_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM schedule WHERE id=?", (lesson_id,))
        self.conn.commit()
        return f"✅ Урок ID {lesson_id} удалён"

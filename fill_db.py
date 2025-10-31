from logic import DBManager

db = DBManager()

lessons = {
    9: {
        'Понедельник': [('Math', '10:00'), ('English', '11:00')],
        'Вторник': [('Biology', '10:00'), ('History', '11:00')],
        'Среда': [('Computer Science', '10:00'), ('Literature', '11:00')],
        'Четверг': [('Physics', '10:00'), ('Art', '11:00')],
        'Пятница': [('Geography', '10:00'), ('Physical Education', '11:00')],
    },
    10: {
        'Понедельник': [('Math', '10:00'), ('Chemistry', '11:00')],
        'Вторник': [('Biology', '10:00'), ('English', '11:00')],
        'Среда': [('History', '10:00'), ('Computer Science', '11:00')],
        'Четверг': [('Physics', '10:00'), ('Literature', '11:00')],
        'Пятница': [('Geography', '10:00'), ('Art', '11:00')],
    },
    11: {
        'Понедельник': [('Math', '10:00'), ('Physics', '11:00')],
        'Вторник': [('Chemistry', '10:00'), ('Biology', '11:00')],
        'Среда': [('History', '10:00'), ('English', '11:00')],
        'Четверг': [('Computer Science', '10:00'), ('Literature', '11:00')],
        'Пятница': [('Geography', '10:00'), ('Physical Education', '11:00')],
    },
}

for grade, days in lessons.items():
    for day, subjects in days.items():
        for subject, time in subjects:
            db.add_lesson(grade, day, subject, time)

print("✅ Database filled with all lessons.")

import os
import csv
import mysql.connector as mysql
import dotenv

dotenv.load_dotenv()

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

cursor = db.cursor()

cursor.execute('''
    SELECT s.name,
    s.second_name,
    g.title as group_title,
    b.title as books_title,
    sub.title as subject_title,
    l.title as lesson_title,
    m.value as mark_value
    FROM students s
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN `groups` g ON s.group_id = g.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON l.id = m.lesson_id
    JOIN subjects sub ON sub.id = l.subject_id
    WHERE s.second_name = 'Ivanov'
''')

data = cursor.fetchall()

db_data = []

for row in data:
    new_row = []
    for value in row:
        new_row.append(str(value))
    db_data.append(new_row)

with open('..\\..\\eugene_okulik\\Lesson_16\\hw_data\\data.csv') as csvfile:
    filedata = csv.reader(csvfile, delimiter=',')
    for row in filedata:
        if row not in db_data:
            print(row)

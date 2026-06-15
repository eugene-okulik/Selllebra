import mysql.connector as mysql

db = mysql.connect(
    user="st-onl",
    passwd="AVNS_tegPDkI5BlB2lW5eASC",
    host="db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com",
    port=25060,
    database="st-onl"
)

cursor = db.cursor()

cursor.execute("INSERT INTO students (name, second_name) "
               "VALUES (%s, %s)", ('John', 'Galt'))
stud_id = cursor.lastrowid

query_book = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values_b = [
    ('Book one', stud_id),
    ('Book two', stud_id),
    ('Book three', stud_id),
    ('Book four', stud_id)
]
cursor.executemany(query_book, values_b)

cursor.execute("INSERT INTO `groups` (title, start_date, end_date) "
               "VALUES (%s, %s, %s)",
               ('Private', 'april', 'july')
               )
gr_id = cursor.lastrowid
cursor.execute("UPDATE students SET group_id = %s WHERE id = %s",
               (gr_id, stud_id)
               )

subjects_titles = ['Private subject', 'Private subject_hard']
subjects_ids = []

for title in subjects_titles:
    cursor.execute("INSERT INTO subjects (title) VALUES (%s)", [title])
    subjects_ids.append(cursor.lastrowid)

lessons_data = [
    ('Lesson_one_for_Private_subject', subjects_ids[0]),
    ('Lesson_two_for_Private_subject', subjects_ids[0]),
    ('Lesson_one_for_Private subject_hard', subjects_ids[1]),
    ('Lesson_two_for_Private subject_hard', subjects_ids[1])
]
lessons_ids = []

for title, sub_id in lessons_data:
    cursor.execute("INSERT INTO lessons (title, subject_id) VALUES (%s, %s)",
                   (title, sub_id))
    lessons_ids.append(cursor.lastrowid)

query_marks = ("INSERT INTO marks (value, lesson_id, student_id) "
               "VALUES (%s, %s, %s)")
values_m = [
    (5, lessons_ids[0], stud_id),
    (6, lessons_ids[1], stud_id),
    (7, lessons_ids[2], stud_id),
    (8, lessons_ids[3], stud_id)
]
cursor.executemany(query_marks, values_m)

cursor.execute("SELECT m.value FROM marks m WHERE student_id = %s",
               (stud_id,)
               )
marks_data = cursor.fetchall()
print(marks_data)
cursor.execute("SELECT b.title FROM books b WHERE taken_by_student_id = %s",
               (stud_id,)
               )
books_data = cursor.fetchall()
print(books_data)
cursor.execute('''
    SELECT s.name,
    s.second_name,
    g.title as group_name,
    b.title as books_taken,
    sub.title as subject,
    l.title as lesson,
    m.value as mark
    FROM students s
    JOIN books b ON s.id = b.taken_by_student_id
    JOIN `groups` g ON s.group_id = g.id
    JOIN marks m ON m.student_id = s.id
    JOIN lessons l ON l.id = m.lesson_id
    JOIN subjects sub ON sub.id = l.subject_id
    WHERE s.id = %s
''', (stud_id,))

data = cursor.fetchall()
print(data)

db.commit()

db.close()

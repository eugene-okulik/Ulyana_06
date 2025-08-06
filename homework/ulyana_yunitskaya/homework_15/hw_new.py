import pymysql


db = pymysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl',
    ssl={"ssl": {}}
)

cursor = db.cursor()

new_student = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
values = ('Ivan', 'Potapov', None)
cursor.execute(new_student, values)

new_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
values_book = [
    ('The Prince and the Pauper', 20914),
    ('Mary Poppins', 20914)
]
cursor.executemany(new_books, values_book)

new_groups = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values_groups = ('class_1', 'may 2025', 'oct 2025')
cursor.execute(new_groups, values_groups)

update_stud_group = "UPDATE students SET group_id = %s WHERE id = %s"
values_upd = (5487, 20914)
cursor.execute(update_stud_group, values_upd)

new_subjects = "INSERT INTO subjects (title) VALUES (%s)"
values_subjects = [
    ('history elementary',),
    ('math easy',)
]
cursor.executemany(new_subjects, values_subjects)

new_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
values_lessons = [
    ('hist less 1', 11620),
    ('hist less 2', 11620),
    ('math less 1', 11621),
    ('math less 2', 11621)
]
cursor.executemany(new_lessons, values_lessons)

new_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
values_marks = [
    (4, 11672, 20914),
    (5, 11673, 20914),
    (4, 11674, 20914),
    (5, 11675, 20914)
]
cursor.executemany(new_marks, values_marks)

cursor.execute("SELECT * FROM marks m WHERE m.student_id = %s", (20914,))
result = cursor.fetchall()
print(result)

cursor.execute("SELECT * FROM books b WHERE b.taken_by_student_id = %s", (20914,))
result2 = cursor.fetchall()
print(result2)

query = '''
    SELECT 
        s.id AS student_id,
        s.name,
        s.second_name,
        g.title AS group_title,
        b.title AS book_title,
        m.value AS mark_value,
        l.title AS lesson_title,
        sub.title AS subject_title
    FROM students s
    LEFT JOIN `groups` g ON s.group_id = g.id
    LEFT JOIN books b ON s.id = b.taken_by_student_id
    LEFT JOIN marks m ON s.id = m.student_id
    LEFT JOIN lessons l ON m.lesson_id = l.id
    LEFT JOIN subjects sub ON l.subject_id = sub.id
    WHERE s.id = %s
'''

student_id = 20914

cursor_1 = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor_1.execute(query, (student_id,))
results_all = cursor_1.fetchall()
print(results_all)

db.commit()

db.close()

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
values = ('Mary', 'Ivanchenko', None)
cursor.execute(new_student, values)

student_check_id = cursor.lastrowid

new_books = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book_titles = ['The Prince and the Pauper', 'Mary Poppins']
book_ids = []
for title in book_titles:
    cursor.execute(new_books, (title, student_check_id))
    book_ids.append(cursor.lastrowid)

new_group = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
values_group = ('class_1', '2025-05-01', '2025-10-31')
cursor.execute(new_group, values_group)
group_id = cursor.lastrowid

update_student_group = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(update_student_group, (group_id, student_check_id))

new_subject = "INSERT INTO subjects (title) VALUES (%s)"
subject_titles = ['history elementary', 'math easy']
subject_ids = []
for title in subject_titles:
    cursor.execute(new_subject, (title,))
    subject_ids.append(cursor.lastrowid)

new_lessons = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_titles = [
    ('hist less 1', subject_ids[0]),
    ('hist less 2', subject_ids[0]),
    ('math less 1', subject_ids[1]),
    ('math less 2', subject_ids[1])
]
lesson_ids = []
for title, subject_id in lesson_titles:
    cursor.execute(new_lessons, (title, subject_id))
    lesson_ids.append(cursor.lastrowid)

new_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_values = [
    (4, lesson_ids[0], student_check_id),
    (5, lesson_ids[1], student_check_id),
    (4, lesson_ids[2], student_check_id),
    (5, lesson_ids[3], student_check_id)
]
cursor.executemany(new_marks, marks_values)

cursor.execute("SELECT * FROM marks WHERE student_id = %s", (student_check_id,))
print(cursor.fetchall())

cursor.execute("SELECT * FROM books WHERE taken_by_student_id = %s", (student_check_id,))
print(cursor.fetchall())

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

cursor_1 = db.cursor(cursor=pymysql.cursors.DictCursor)
cursor_1.execute(query, (student_check_id,))
print(cursor_1.fetchall())

db.commit()

db.close()

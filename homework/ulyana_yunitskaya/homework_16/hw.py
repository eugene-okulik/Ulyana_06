import csv
import os
import dotenv
import pymysql


dotenv.load_dotenv()

db = pymysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=int(os.getenv('DB_PORT')),
    database=os.getenv('DB_NAME'),
    ssl={"ssl": {}}
)

cursor = db.cursor()

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_file = os.path.join(homework_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

missing_rows = []

with open(eugene_file, newline='', encoding='utf-8') as eugene_csv:
    file_csv = csv.DictReader(eugene_csv)
    for row in file_csv:
        query = """
        SELECT s.id
        FROM students s
        LEFT JOIN `groups` g ON s.group_id = g.id
        LEFT JOIN books b ON s.id = b.taken_by_student_id
        LEFT JOIN marks m ON s.id = m.student_id
        LEFT JOIN lessons l ON m.lesson_id = l.id
        LEFT JOIN subjects sub ON l.subject_id = sub.id
        WHERE s.name = %s
          AND s.second_name = %s
          AND g.title = %s
          AND b.title = %s
          AND sub.title = %s
          AND l.title = %s
          AND m.value = %s
        """
        cursor.execute(query, (
            row['name'],
            row['second_name'],
            row['group_title'],
            row['book_title'],
            row['subject_title'],
            row['lesson_title'],
            row['mark_value']
        ))
        if cursor.fetchone() is None:
            missing_rows.append(row)

for name in missing_rows:
    print("Missing data:", name)

db.close()

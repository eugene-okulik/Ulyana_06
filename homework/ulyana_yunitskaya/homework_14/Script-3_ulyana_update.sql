INSERT INTO students (name, second_name, group_id) VALUES ('Ivan', 'Potapov', NULL)

INSERT INTO books (title, taken_by_student_id) VALUES ('The Prince and the Pauper', 20852), 
                                                      ('Mary Poppins', 20852)
                                                      
INSERT INTO `groups` (title, start_date, end_date) VALUES ('class_1', 'may 2025', 'oct 2025')

UPDATE students SET group_id = 5461 WHERE id = 20852

INSERT INTO subjects (title) VALUES ('history elementary'), ('math easy')

INSERT INTO lessons (title, subject_id) VALUES ('hist less 1', 11585),
                                               ('hist less 2', 11585),
                                               ('math less 1', 11586),
                                               ('math less 2', 11586)
                                               
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 11620, 20852),
                                                        (5, 11621, 20852),
                                                        (4, 11622, 20852),
                                                        (5, 11623, 20852)

SELECT * FROM marks m WHERE m.student_id = 20852

SELECT * FROM books b WHERE b.taken_by_student_id = 20852

SELECT s.id, s.name, s.second_name, g.title, b.title, m.value,l.title, sub.title 
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 20852;                                               
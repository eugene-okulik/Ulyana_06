INSERT INTO students (name, second_name, group_id) VALUES ('Ivan', 'Potapov', 5460)

INSERT INTO books (title, taken_by_student_id) VALUES ('The Prince and the Pauper', 20851), 
                                                      ('Mary Poppins', 20851)
                                                      
INSERT INTO `groups` (title, start_date, end_date) VALUES ('class_1', 'may 2025', 'oct 2025')

INSERT INTO subjects (title) VALUES ('history elementary'), ('math easy')

INSERT INTO lessons (title, subject_id) VALUES ('hist less 1', 11581),
                                               ('hist less 2', 11581),
                                               ('math less 1', 11582),
                                               ('math less 2', 11582)
                                               
INSERT INTO marks (value, lesson_id, student_id) VALUES (4, 11612, 20851),
                                                        (5, 11613, 20851),
                                                        (4, 11614, 20851),
                                                        (5, 11615, 20851)
                                                        
SELECT * FROM marks m WHERE m.student_id = 20851

SELECT * FROM books b WHERE b.taken_by_student_id = 20851

SELECT s.id, s.name, s.second_name, g.title, b.title, m.value,l.title, sub.title 
FROM students s
LEFT JOIN `groups` g ON s.group_id = g.id
LEFT JOIN books b ON s.id = b.taken_by_student_id
LEFT JOIN marks m ON s.id = m.student_id
LEFT JOIN lessons l ON m.lesson_id = l.id
LEFT JOIN subjects sub ON l.subject_id = sub.id
WHERE s.id = 20851;

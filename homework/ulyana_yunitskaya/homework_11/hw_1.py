class Book:
    page_material = 'paper'
    text_presence = True

    def __init__(self, book_title, author, number_of_pages, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_pages = number_of_pages
        self.isbn = isbn
        self.reserved = reserved

    def print_info(self):
        if self.reserved:
            print(f'Name: {self.book_title}, Author: {self.author}, Pages: {self.number_of_pages}, '
                  f'Material: {self.page_material}, reserved')
        else:
            print(f'Name: {self.book_title}, Author: {self.author}, Pages: {self.number_of_pages}, '
                  f'Material: {self.page_material}')


book_one = Book('The Idiot', 'Dostoevsky', 500,
                5698, True)
book_two = Book('A Hero of Our Time', 'Lermontov', 140,
                4988, False)
book_three = Book('The Government Inspector', 'Gogol', 210,
                  6988, False)
book_four = Book('Woe from Wit', 'Griboyedov', 174,
                 6918, False)
book_five = Book('War and Peace', 'Tolstoy', 236,
                 5478, False)


book_one.print_info()
book_two.print_info()
book_three.print_info()
book_four.print_info()
book_five.print_info()


class SchoolBooks(Book):

    def __init__(self, book_title, author, number_of_pages, isbn, reserved, subject, school_class, tasks):
        super().__init__(book_title, author, number_of_pages, isbn, reserved)
        self.subject = subject
        self.school_class = school_class
        self.tasks = tasks

    def info_tasks(self):
        if self.reserved:
            print(f'Name: {self.book_title}, Author: {self.author}, Pages: {self.number_of_pages}, '
                  f'Subject: {self.subject}, School_class: {self.school_class}, reserved')
        else:
            print(f'Name: {self.book_title}, Author: {self.author}, Pages: {self.number_of_pages}, '
                  f'Subject: {self.subject}, School_class: {self.school_class}')


school_book_one = SchoolBooks('Algebra', 'Ivanov', 120, 6498,
                              False, 'Mathematics', '5a', True)
school_book_two = SchoolBooks('Countries and Continents', 'Petrov', 118,
                              8988, False, 'Geography', '8d', False)
school_book_three = SchoolBooks('History of Belarus', 'Sergeev', 60,
                                1688, True, 'History', '10c', False)


school_book_one.info_tasks()
school_book_two.info_tasks()
school_book_three.info_tasks()

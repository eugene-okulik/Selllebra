class Book:
    pages_material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved


class School_book(Book):
    def __init__(self, title, author, pages, isbn, is_reserved,
                 subject, level, has_tasks):
        super().__init__(title, author, pages, isbn, is_reserved)
        self.subject = subject
        self.level = level
        self.has_tasks = has_tasks


book_1 = School_book("Солярис", "Лем",
                     456, 1122334455667, "зарезервирована",
                     "литература", 11, True
                     )
book_2 = School_book("Римская империя", "Карлов",
                     678, 2233445566778, "не зарезервирована",
                     "история", 10, True
                     )
book_3 = School_book("Геометрия от А до Я", "Парлович",
                     567, 3344556677889, "не зарезервирована",
                     "математика", 9, True
                     )
book_4 = School_book("Народные песни", "Викорский",
                     345, 4455667788990, "не зарезервирована",
                     "пение", 11, True
                     )
book_5 = School_book("Букашки", "Букавко",
                     100, 5566778899001, "не зарезервирована",
                     "рисование", 1, True)


def school_book_print(book):
    if book.is_reserved == "зарезервирована":
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, предмет: {book.subject}, '
            f'{book.is_reserved}'
        )
    else:
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, предмет: {book.subject}'
        )


school_book_print(book_1)
school_book_print(book_2)
school_book_print(book_3)
school_book_print(book_4)
school_book_print(book_5)

from Selllebra.homework.selllebra_homeworks.homework_11.homework_11_1 \
    import (Book)


class SchoolBook(Book):
    def __init__(self, title, author, pages, isbn, subject, level):
        super().__init__(title, author, pages, isbn)
        self.subject = subject
        self.level = level
        self.has_tasks = True


book_1 = SchoolBook("Солярис", "Лем",
                    456, 1122334455667,
                    "литература", 11
                    )
book_2 = SchoolBook("Римская империя", "Карлов",
                    678, 2233445566778,
                    "история", 10
                    )
book_3 = SchoolBook("Геометрия от А до Я", "Парлович",
                    567, 3344556677889,
                    "математика", 9
                    )
book_4 = SchoolBook("Народные песни", "Викорский",
                    345, 4455667788990,
                    "пение", 11
                    )
book_5 = SchoolBook("Букашки", "Букавко",
                    100, 5566778899001,
                    "рисование", 1
                    )


book_5.is_reserved = True


def school_book_print(book):
    if book.is_reserved is True:
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, предмет: {book.subject}, '
            f'класс: {book.level}, зарезервирована'
        )
    else:
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, предмет: {book.subject}, '
            f'класс: {book.level}'
        )


school_book_print(book_1)
school_book_print(book_2)
school_book_print(book_3)
school_book_print(book_4)
school_book_print(book_5)

class Book:
    pages_material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn, is_reserved):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = is_reserved


book_1 = Book("Солярис", "Лем",
              456, 1122334455667, "зарезервирована")
book_2 = Book("Маленький принц", "Экзюпери",
              678, 2233445566778, "не зарезервирована")
book_3 = Book("1984", "Оруэлл",
              567, 3344556677889, "не зарезервирована")
book_4 = Book("Преступление и наказание", "Достоевский",
              345, 4455667788990, "не зарезервирована")
book_5 = Book("Идиот", "Достоевский",
              500, 5566778899001, "не зарезервирована")


def book_print(book):
    if book.is_reserved == "зарезервирована":
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, материал: {book.pages_material}, '
            f'{book.is_reserved}'
        )
    else:
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, материал: {book.pages_material}'
        )


book_print(book_1)
book_print(book_2)
book_print(book_3)
book_print(book_4)
book_print(book_5)

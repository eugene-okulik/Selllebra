class Book:
    pages_material = "бумага"
    has_text = True

    def __init__(self, title, author, pages, isbn):
        self.title = title
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.is_reserved = False


book_1 = Book("Солярис", "Лем",
              456, 1122334455667)
book_2 = Book("Маленький принц", "Экзюпери",
              678, 2233445566778)
book_3 = Book("1984", "Оруэлл",
              567, 3344556677889)
book_4 = Book("Преступление и наказание", "Достоевский",
              345, 4455667788990)
book_5 = Book("Идиот", "Достоевский",
              500, 5566778899001)

book_1.is_reserved = True


def book_print(book):
    if book.is_reserved is True:
        print(
            f'Название: {book.title}, Автор: {book.author}, '
            f'страниц: {book.pages}, материал: {book.pages_material}, '
            f'зарезервирована'
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

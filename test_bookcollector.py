from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # 1 test: BooksCollector.add_new_book() method for book longer than 40 characters in title
    # ER: it shouldn't be added
    def test_add_new_book_booktitle_more_than40_char_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Странная история доктора Джекила и мистера Хайда')
        assert len(collector.books_genre) == 0

    # 2 test: BookCollector.add_new_book() method for second entry of the same book
    # ER: it shouldn't be added
    def test_add_new_book_already_added_to_dict_secondary_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Клуб убийств по четвергам')
        collector.add_new_book('Клуб убийств по четвергам')
        assert len(collector.books_genre) == 1

    books = [
        ['Дюна', 'Фантастика'],
        ['Кладбище домашних животных', 'Ужасы'],
        ['Клуб убийств по четвергам', 'Детективы'],
        ['Простоквашино', 'Мультфильмы'],
        ['Комедии', 'Комедии']
    ]

    # 3 test:
    # ER:
    @pytest.mark.parametrize('title, genre', books)
    def test_set_book_genre_five_genres_all_set(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.books_genre[title] == genre

    # 4 test:
    # ER:
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        title = 'invalid_book'
        genre = 'invalid_genre'
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.books_genre[title] == ''

    # 5 test:
    # ER:
    def test_set_book_genre_book_not_added_to_dict_not_set(self):
        collector = BooksCollector()
        collector.set_book_genre('Клуб убийств по четвергам', 'Детективы')
        assert len(collector.books_genre) == 0

    # 6 test:
    # ER:
    @pytest.mark.parametrize('title, genre', books)
    def test_get_book_genre_all_genres_returned(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    #TODO: решить как проверять этот метод и не имать мозги

    # many_books_with_genres = [
    #     [
    #             ['fiction_book1','Фантастика'],
    #             ['fiction_book2','Фантастика'],
    #             ['fiction_book3','Фантастика']
    #     ],
    #     [
    #             ['horror_book1','Ужасы'],
    #             ['horror_book2','Ужасы']
    #     ],
    #     [
    #             ['detective_book1','Детективы'],
    #             ['detective_book2','Детективы'],
    #             ['detective_book3','Детективы'],
    #             ['detective_book4','Детективы']
    #     ],
    #     [
    #             ['cartoon_book1','Мультфильмы'],
    #     ],
    #     [
    #             ['comedy_book1','Комедии'],
    #             ['comedy_book2','Комедии']
    #     ]
    #
    # ]
    # 7 test:
    # ER:
    def test_get_books_with_specific_genre_all_genres_returned(self, books_with_genres, genres):
        collector = BooksCollector()
        for book in books_with_genres:
            collector.add_new_book(book[0])
            collector.set_book_genre(name=book[0], genre=book[1])
        for genre in genres:
            assert (len(collector.get_books_with_specific_genre(genre))
                    == len(list(filter(lambda x:genre in x, books_with_genres))))

    # 8 test:
    # ER:
    def test_get_books_genre_all_genres_returned(self):
        collector = BooksCollector()
        collector.add_new_book('book1')
        collector.add_new_book('book2')
        collector.add_new_book('book3')
        assert len(collector.get_books_genre()) == len(collector.books_genre)



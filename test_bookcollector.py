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

    # 7 test:
    # ER:
    def test_get_books_with_specific_genre_all_genres_returned(self, books_with_genres, genres):
        collector = BooksCollector()
        for book in books_with_genres:
            collector.add_new_book(book[0])
            collector.set_book_genre(name=book[0], genre=book[1])
        for genre in genres:
            collection_length_actual = len(collector.get_books_with_specific_genre(genre))
            collection_length_expected = len(list(filter(lambda x:genre in x, books_with_genres)))
            assert collection_length_actual == collection_length_expected

    # 8 test:
    # ER:
    def test_get_books_genre_all_books_returned(self):
        collector = BooksCollector()
        collector.add_new_book('book1')
        collector.add_new_book('book2')
        collector.add_new_book('book3')
        assert len(collector.get_books_genre()) == len(collector.books_genre)

    kids_books = [
        ['kids_book1','Фантастика'],
        ['kids_book2','Мультфильмы'],
        ['kids_book3','Комедии'],
    ]
    # 9 test:
    # ER:
    @pytest.mark.parametrize('title, genre', kids_books)
    def test_get_books_for_children_kids_only_return_all(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert title in collector.get_books_for_children()

    not_kids_books = [
        ['not_kids_book1', 'Ужасы'],
        ['not_kids_book2', 'Детективы']
    ]

    # 10 test:
    # ER:
    @pytest.mark.parametrize('title, genre', not_kids_books)
    def test_get_books_for_children_not_kids_books_not_return(self, title, genre):
        collector = BooksCollector()
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert title not in collector.get_books_for_children()

    # test 11:
    # ER:
    def test_add_book_in_favorites_new_book_added(self):
        collector = BooksCollector()
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert collector.favorites == ['favorite_book1']

    # test 12:
    # ER:
    def test_add_book_in_favorites_present_book_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert len(collector.favorites) == 1

    # test 13:
    # ER:
    def test_add_book_in_favorites_missing_book_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('favorite_book1')
        assert collector.favorites == []

    # test 14:
    # ER:
    def test_delete_book_from_favorites_present_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        collector.delete_book_from_favorites('favorite_book1')
        assert collector.favorites == []

    # test 15:
    # ER:
    def test_get_list_of_favorites_books_books_present_returned(self):
        collector = BooksCollector()
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert collector.get_list_of_favorites_books() == collector.favorites
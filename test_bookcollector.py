from main import BooksCollector
import pytest

from test_data import BooksCollectorData as bcd

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # test 1: BooksCollector.add_new_book() method for book longer than 40 characters in title
    # ER: it shouldn't be added
    @pytest.mark.parametrize('title', bcd.too_long_titles)
    def test_add_new_book_booktitle_more_than40_char_not_added(self, collector, title):
        collector.add_new_book(title)
        assert len(collector.books_genre) == 0
    # new test 1.1: BooksCollector.add_new_book() method for book shorter than 40 characters in title
    #
    @pytest.mark.parametrize('title', bcd.long_enough_titles)
    def test_add_new_book_booktitle_less_than_41_char_added(self, collector, title):
        collector.add_new_book(title)
        assert len(collector.books_genre) == 1

    # test 2: BookCollector.add_new_book() method for second entry of the same book
    # ER: it shouldn't be added
    def test_add_new_book_already_added_to_dict_secondary_not_added(self, collector):
        collector.add_new_book('Клуб убийств по четвергам')
        collector.add_new_book('Клуб убийств по четвергам')
        assert len(collector.books_genre) == 1

    # test 3: set a book per valid genre
    # ER: every valid genre is set for the book
    @pytest.mark.parametrize('title, genre', bcd.books)
    def test_set_book_genre_valid_genre_all_set(self, title, genre, collector):
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.books_genre[title] == genre

    # test 4: set invalid (not present in BookCollector.genre) for the book
    # ER: genre is NOT set and is left empty
    @pytest.mark.parametrize('title, genre', bcd.invalid_genres)
    def test_set_book_genre_invalid_genre_not_set(self, collector, title, genre):
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.books_genre[title] == ''

    # test 5: set genre for non-existent book
    # ER: nothing happens
    def test_set_book_genre_book_not_added_to_dict_not_set(self, collector):
        collector.set_book_genre('Клуб убийств по четвергам', 'Детективы')
        assert len(collector.books_genre) == 0

    # test 6: get valid genre for existent book by title
    # ER: genre is correctly returned as specified in BookCollector.books_genre
    @pytest.mark.parametrize('title, genre', bcd.books)
    def test_get_book_genre_valid_genres_returned(self, title, genre, collector):
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert collector.get_book_genre(title) == genre

    # test 7: filter existent books by valid genre
    # ER: only books with specified genres are returned from the dict of books with different genres
    @pytest.mark.parametrize('genre', bcd.genres)
    def test_get_books_with_specific_genre_valid_genres_returned(self, books_with_genres, genre, collector):
        for book in books_with_genres:
            collector.add_new_book(book[0])
            collector.set_book_genre(name=book[0], genre=book[1])
        actual_collection = collector.get_books_with_specific_genre(genre)
        expected_collection = list(map(lambda x:x[0], filter(lambda x:genre in x, books_with_genres)))
        assert actual_collection == expected_collection

    # test 8: get dict of books with books present
    # ER: dict is returned
    def test_get_books_genre_all_books_returned(self, collector):
        collector.add_new_book('book1')
        collector.add_new_book('book2')
        collector.add_new_book('book3')
        assert collector.get_books_genre() == collector.books_genre

    # test 9: get books with kid-safe genres
    # ER: kid-safe books are returned
    @pytest.mark.parametrize('title, genre', bcd.kids_books)
    def test_get_books_for_children_kids_only_return_all(self, title, genre, collector):
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert title in collector.get_books_for_children()

    # test 10: filter books that are not kid-safe
    # ER: nothing is returned
    @pytest.mark.parametrize('title, genre', bcd.not_kids_books)
    def test_get_books_for_children_not_kids_books_not_return(self, title, genre, collector):
        collector.add_new_book(title)
        collector.set_book_genre(title, genre)
        assert title not in collector.get_books_for_children()

    # test 11: existent books is added to favorites
    # ER: book is in favorites
    def test_add_book_in_favorites_new_book_added(self, collector):
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert collector.favorites == ['favorite_book1']

    # test 12: double entries of the same book in favorites
    # ER: book entries are not doubled in favorites
    def test_add_book_in_favorites_present_book_not_added(self, collector):
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert len(collector.favorites) == 1

    # test 13: add non-existent book to favorites
    # ER: nothing is added
    def test_add_book_in_favorites_missing_book_not_added(self, collector):
        collector.add_book_in_favorites('favorite_book1')
        assert collector.favorites == []

    # test 14: present in favorites book is deleted
    # ER: book is deleted
    def test_delete_book_from_favorites_present_book_deleted(self, collector):
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        collector.delete_book_from_favorites('favorite_book1')
        assert collector.favorites == []

    # test 15: get list of favorites
    # ER: correct list is returned
    def test_get_list_of_favorites_books_books_present_returned(self, collector):
        collector.add_new_book('favorite_book1')
        collector.add_book_in_favorites('favorite_book1')
        assert collector.get_list_of_favorites_books() == collector.favorites

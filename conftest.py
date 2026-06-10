import pytest

@pytest.fixture(scope='session')
def books_with_genres():
    return [
        ['fiction_book1','Фантастика'],
        ['fiction_book2','Фантастика'],
        ['fiction_book3','Фантастика'],
        ['horror_book1','Ужасы'],
        ['horror_book2','Ужасы'],
        ['detective_book1','Детективы'],
        ['detective_book2','Детективы'],
        ['detective_book3','Детективы'],
        ['detective_book4','Детективы'],
        ['cartoon_book1','Мультфильмы'],
        ['comedy_book1','Комедии'],
        ['comedy_book2','Комедии']
    ]

@pytest.fixture(scope='session')
def genres():
    return ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

from main import BooksCollector

import pytest


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        assert 'Пикник на обочине' in collector.get_books_genre()

    @pytest.mark.parametrize(
        'incorrect_name',
        ['', 'Неважно, как медленно ты идёшь, пока ты не останавливаешься']
    )
    def test_add_new_book_long_or_empty_name(self, incorrect_name):
        collector = BooksCollector()
        collector.add_new_book(incorrect_name)
        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_available_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')
        assert collector.get_book_genre('Пикник на обочине') == "Фантастика"

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Ревизор', 'Комедии'),
            ('Пикник на обочине', 'Фантастика'),
        ]
    )
    def test_set_book_genre_no_added_books(self, name, genre):
        collector = BooksCollector()
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) is None

    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Пикник на обочине', 'Роман'),
            ('Ревизор', 'Пьеса')
        ]
    )
    def test_set_book_genre_not_available_genres(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ''

    def test_get_book_genre_for_different_books(self):
        books = {
            'Пикник на обочине': 'Фантастика',
            'Ревизор': 'Комедии',
            'Русалочка': 'Мультфильмы'
        }
        collector = BooksCollector()
        for name, genre in books.items():
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)
            assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Пикник на обочине', 'Фантастика'],
            ['Ревизор', 'Комедии'],
            ['Шерлок Холмс', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre_returns_correct_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert name in collector.get_books_with_specific_genre(genre)

    def test_get_books_genre_returns_correct_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.set_book_genre('Пикник на обочине', 'Фантастика')

        collector.add_new_book('Шерлок Холмс')
        correct_books_genres = {
            'Пикник на обочине': 'Фантастика',
            'Шерлок Холмс': ''
            }
        assert collector.get_books_genre() == correct_books_genres

    def test_get_books_for_children_not_include_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.add_new_book('Русалочка')
        collector.set_book_genre('Русалочка', 'Мультфильмы')
        books_for_children = ['Русалочка']
        assert collector.get_books_for_children() == books_for_children

    @pytest.mark.parametrize('name',['Ревизор', 'Пикник на обочине', 'Русалочка'])
    def test_add_book_in_favorites_add_new_book(self,name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert name in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.add_book_in_favorites('Пикник на обочине')
        collector.delete_book_from_favorites('Пикник на обочине')
        assert 'Пикник на обочине' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_no_duplicates(self):
        collector = BooksCollector()
        collector.add_new_book('Пикник на обочине')
        collector.add_book_in_favorites('Пикник на обочине')
        collector.add_book_in_favorites('Пикник на обочине')
        favorites_books = collector.get_list_of_favorites_books()
        assert len(favorites_books) == 1


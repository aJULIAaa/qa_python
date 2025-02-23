# Тесты для BooksCollector

## Описание тестов

- **test_add_new_book_add_one_book:** проверяет успешное добавление новой книги.
- **test_add_new_book_long_or_empty_name:** проверяет, что книги с пустым или слишком длинным названием не добавляются.
- **test_set_book_genre_available_genre:** проверяет установку корректного жанра для книги.
- **test_set_book_genre_no_added_book_and_invalid_genre:** проверяет, что жанр не устанавливается для несуществующих книг или при указании несуществующего жанра.
- **test_get_book_genre_different_genre:** проверяет получение корректного жанра книги по ее имени.
- **test_get_books_with_specific_genre_returns_correct_books:** проверяет, что метод возвращает книги с заданным жанром.
- **test_get_books_genre_returns_correct_genres:** проверяет, что метод возвращает правильный словарь книг и их жанров.
- **test_get_books_for_children_not_include_age_rating:** проверяет, что книги с возрастным ограничением не включаются в список книг для детей.
- **test_add_book_in_favorites_add_new_book:** проверяет успешное добавление книги в избранное.
- **test_delete_book_from_favorites_removes_book:** проверяет удаление книги из избранного списка.
- **test_get_list_of_favorites_books_no_duplicates:** проверяет, что одна и та же книга не добавляется в избранное повторно.
# qa_python
## Methods covered in tests:

for the purposes of the easier reading sometimes a term of 'existent/existing book' can be met -
existing book is one that has been added to BookCollector.books_genre and vice versa

### .add_new_book()

- **test_add_new_book_add_two_books** - tests the flow of adding two books in BookCollector's object
- **test_add_new_book_booktitle_more_than40_char_not_added** - tests that book longer than 40 characters
cannot be added to the dict BookCollector.books_genre
- **test_add_new_book_already_added_to_dict_secondary_not_added** - tests that second entries of the same book
are not duplicated in BookCollector.books_genre dict

### .set_book_genre()

- **test_set_book_genre_five_genres_all_set** - checks that all five genres from BookCollector.genre
cah be set for the existent book
- **test_set_book_genre_invalid_genre_not_set** - checks that genres not mentioned in BookCollector.genre cannot be set
- **test_set_book_genre_book_not_added_to_dict_not_set** - checks that genres can only be set for the book
that has been added to BookCollector.books_genre

### .get_book_genre()

- **test_get_book_genre_all_genres_returned** - checks that book's genre is returned when specifying existent book title

### .get_books_with_specific_genre()

- **test_get_books_with_specific_genre_all_genres_returned** - checks that from the list of books
only those with selected genre are returned

### .get_books_genre()

-**test_get_books_genre_all_books_returned** - checks that BookCollector.books_genre is returned with correct values

### .get_books_for_children()

- **test_get_books_for_children_kids_only_return_all** - checks that books with kid-safe genres are returned
- **test_get_books_for_children_not_kids_books_not_return** - check that books with not-kid-safe genres are not returned

### .add_book_in_favorites()

- **test_add_book_in_favorites_new_book_added** - checks that a new existent book  can be added to favorites
- **test_add_book_in_favorites_present_book_not_added** - checks that the same book is not added to favorites twice
- **test_add_book_in_favorites_missing_book_not_added** - checks that not existing book is not added to favorites

### .delete_book_from_favorites()

- **test_delete_book_from_favorites_present_book_deleted** - checks that existent book in favorites can be deleted

### .get_list_of_favorites_books()

- **test_get_list_of_favorites_books_books_present_returned** - checks that correct values from BookCollector.favorites
are returned when there books added to it

## Examples of the tests that haven't been covered:

- **test_get_books_with_specific_genre_invalid_genres_not_returned** - should check that specifying invalid genre
doesn't break or return anything
- **test_get_books_with_specific_genre_empty_genre_nothing_returned** - should check that when specifying an empty string
books which have no genre specified are not returned and nothing is returned
- **test_delete_book_from_favorites_not_present_book_nothing_happens** - should check that trying to delete
an existing book that is not present in favorites doesn't break anything
- **test_delete_book_from_favorites_not_existent_book_nothing_happens** - should check that trying to delete a non-existent book
from favorites doesn't break anything
- **test_get_list_of_favorites_books_no_books_empty_list_returned** - should check that when nothing is added to favorites
OR everything was deleted(separate in two cases) - an empty list is returned
- etc.
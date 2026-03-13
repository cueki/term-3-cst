"""This module contains the Book class."""

from library_item import LibraryItem


class Book(LibraryItem):
    """
    Represents a single book in a library which is identified through
    its call number.
    """

    ITEM_TYPE = "Book"
    EXTRA_FIELDS = (("author", "Enter Author Name: ", str),)

    def __init__(self, call_num, title, num_copies, **kwargs):
        """
        Initialize a Book.
        :param call_num: a string, unique identifier
        :param title: a string
        :param num_copies: an int, positive integer
        :param kwargs: must include 'author' (a string)
        """
        super().__init__(call_num, title, num_copies, **kwargs)
        self._author = kwargs["author"]

    def get_author(self):
        """
        Returns the author of the book.
        :return: a string
        """
        return self._author

    def __str__(self):
        return (
            f"---- Book: {self.get_title()} ----\n"
            f"Call Number: {self.call_number}\n"
            f"Number of Copies: {self._num_copies}\n"
            f"Author: {self._author}"
        )

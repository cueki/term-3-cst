"""This module contains the abstract base class for all library items."""

from abc import ABC, abstractmethod


class LibraryItem(ABC):
    """
    Abstract base class representing a library item.
    All library items (Books, DVDs, Journals) must inherit from this class.
    """

    def __init__(self, call_num, title, num_copies):
        """
        Initialize a library item.
        :param call_num: a string, unique identifier
        :param title: a string
        :param num_copies: an int, positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies

    def get_title(self):
        """
        Returns the title of the item.
        :return: a string in title case
        """
        return self._title.title()

    def increment_number_of_copies(self):
        """Increment the number of copies by 1."""
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """Decrement the number of copies by 1."""
        self._num_copies -= 1

    def get_num_copies(self):
        """
        Returns the number of available copies.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self):
        """
        Read-only property for the call number.
        :return: a string
        """
        return self._call_num

    def check_availability(self):
        """
        Returns True if the item is available, False otherwise.
        :return: a Boolean
        """
        return self._num_copies > 0

    @abstractmethod
    def __str__(self):
        """
        Abstract method for string representation.
        """
        pass

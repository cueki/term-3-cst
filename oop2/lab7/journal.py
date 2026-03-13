"""This module contains the Journal class."""

from library_item import LibraryItem


class Journal(LibraryItem):
    """
    Represents a scientific journal in a library which is identified through
    its call number.
    """

    ITEM_TYPE = "Journal"
    EXTRA_FIELDS = (
        ("author", "Enter Author Name: ", str),
        ("issue_number", "Enter Issue Number: ", str),
        ("publisher", "Enter Publisher: ", str),
    )

    def __init__(self, call_num, title, num_copies, **kwargs):
        """
        Initialize a Journal.
        :param call_num: a string, unique identifier
        :param title: a string
        :param num_copies: an int, positive integer
        :param kwargs: must include 'author', 'issue_number', 'publisher'
        """
        super().__init__(call_num, title, num_copies, **kwargs)
        self._author = kwargs["author"]
        self._issue_number = kwargs["issue_number"]
        self._publisher = kwargs["publisher"]

    def get_author(self):
        """
        Returns the author of the journal.
        :return: a string
        """
        return self._author

    def get_issue_number(self):
        """
        Returns the issue number of the journal.
        :return: a string or int
        """
        return self._issue_number

    def get_publisher(self):
        """
        Returns the publisher of the journal.
        :return: a string
        """
        return self._publisher

    def __str__(self):
        return (
            f"---- Journal: {self.get_title()} ----\n"
            f"Call Number: {self.call_number}\n"
            f"Number of Copies: {self._num_copies}\n"
            f"Author: {self._author}\n"
            f"Issue Number: {self._issue_number}\n"
            f"Publisher: {self._publisher}"
        )

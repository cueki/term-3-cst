"""This module contains the DVD class."""

from library_item import LibraryItem


class DVD(LibraryItem):
    """
    Represents a DVD in a library which is identified through
    its call number.
    """

    ITEM_TYPE = "DVD"
    EXTRA_FIELDS = (
        ("release_date", "Enter Release Date (e.g., 2023-01-15): ", str),
        ("region_code", "Enter Region Code (e.g., 1 for North America): ", int),
    )

    def __init__(self, call_num, title, num_copies, **kwargs):
        """
        Initialize a DVD.
        :param call_num: a string, unique identifier
        :param title: a string
        :param num_copies: an int, positive integer
        :param kwargs: must include 'release_date' (str) and 'region_code' (int)
        """
        super().__init__(call_num, title, num_copies, **kwargs)
        self._release_date = kwargs["release_date"]
        self._region_code = kwargs["region_code"]

    def get_release_date(self):
        """
        Returns the release date of the DVD.
        :return: a string
        """
        return self._release_date

    def get_region_code(self):
        """
        Returns the region code of the DVD.
        :return: an int
        """
        return self._region_code

    def __str__(self):
        return (
            f"---- DVD: {self.get_title()} ----\n"
            f"Call Number: {self.call_number}\n"
            f"Number of Copies: {self._num_copies}\n"
            f"Release Date: {self._release_date}\n"
            f"Region Code: {self._region_code}"
        )

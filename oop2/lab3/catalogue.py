"""This module contains the Catalogue class for managing library items."""

import difflib
from library_item_generator import LibraryItemGenerator


class Catalogue:
    """
    The Catalogue maintains a collection of library items and provides
    methods for searching, adding, and removing items.

    The Library class depends on Catalogue but is decoupled from the
    implementation details of how items are stored and searched.
    """

    def __init__(self, item_list=None):
        """
        Initialize the catalogue with an optional list of items.
        :param item_list: a sequence of LibraryItem objects, or None
        """
        self._item_list = item_list if item_list is not None else []

    def find_items(self, title):
        """
        Find items with the same or similar title using fuzzy matching.
        :param title: a string
        :return: a list of matching titles
        """
        title_list = [item.get_title() for item in self._item_list]
        results = difflib.get_close_matches(title, title_list, cutoff=0.5)
        return results

    def retrieve_item_by_call_number(self, call_number):
        """
        Retrieve an item by its call number.
        :param call_number: a string, unique identifier
        :return: LibraryItem if found, None otherwise
        """
        for item in self._item_list:
            if item.call_number == call_number:
                return item
        return None

    def add_item(self):
        """
        Add a new item to the catalogue using LibraryItemGenerator.
        Redirects to the generator, creates an item, and adds it to the list.
        :return: True if item was added successfully, False otherwise
        """
        new_item = LibraryItemGenerator.create_item()

        if new_item is None:
            return False

        existing_item = self.retrieve_item_by_call_number(new_item.call_number)
        if existing_item:
            print(
                f"Could not add item with call number "
                f"{new_item.call_number}. It already exists."
            )
            return False

        self._item_list.append(new_item)
        print("Item added successfully! Item details:")
        print(new_item)
        return True

    def remove_item(self, call_number):
        """
        Remove an item from the catalogue by call number.
        :param call_number: a string, unique identifier
        :return: True if removed successfully, False otherwise
        """
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(
                f"Successfully removed {found_item.get_title()} with "
                f"call number: {call_number}"
            )
            return True
        else:
            print(f"Item with call number: {call_number} not found.")
            return False

    def display_all_items(self):
        """
        Display all items in the catalogue.
        """
        print("Library Items")
        print("--------------", end="\n\n")
        for item in self._item_list:
            print(item)
            print()

    def get_item_count(self):
        """
        Returns the number of items in the catalogue.
        :return: an int
        """
        return len(self._item_list)

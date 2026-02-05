"""This module contains the LibraryItemGenerator factory class."""

from book import Book
from dvd import DVD
from journal import Journal


class LibraryItemGenerator:
    """
    Factory class responsible for generating library items.
    Provides a list of available item types and handles user input
    to create the appropriate item type.
    """

    @staticmethod
    def get_item_types():
        """
        Returns a list of available library item types.
        :return: a list of strings
        """
        return ["Book", "DVD", "Journal"]

    @staticmethod
    def create_item():
        """
        Prompts the user to select an item type and enter item details,
        then creates and returns the appropriate library item.
        :return: a LibraryItem subclass instance, or None if cancelled
        """
        print("\nAvailable item types:")
        item_types = LibraryItemGenerator.get_item_types()
        for i, item_type in enumerate(item_types, 1):
            print(f"{i}. {item_type}")
        print(f"{len(item_types) + 1}. Cancel")

        try:
            choice = int(input("Select item type: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return None

        if choice < 1 or choice > len(item_types) + 1:
            print("Invalid choice.")
            return None

        if choice == len(item_types) + 1:
            print("Cancelled.")
            return None

        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        try:
            num_copies = int(input("Enter number of copies (positive number): "))
        except ValueError:
            print("Invalid number of copies.")
            return None

        if choice == 1:  # Book
            author = input("Enter Author Name: ")
            return Book(call_number, title, num_copies, author)

        elif choice == 2:  # DVD
            release_date = input("Enter Release Date (e.g., 2023-01-15): ")
            try:
                region_code = int(
                    input("Enter Region Code (e.g., 1 for North America): ")
                )
            except ValueError:
                print("Invalid region code.")
                return None
            return DVD(call_number, title, num_copies, release_date, region_code)

        elif choice == 3:  # Journal
            author = input("Enter Author Name: ")
            issue_number = input("Enter Issue Number: ")
            publisher = input("Enter Publisher: ")
            return Journal(
                call_number, title, num_copies, author, issue_number, publisher
            )

        return None

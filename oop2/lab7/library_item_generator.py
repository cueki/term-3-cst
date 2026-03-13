"""This module contains the LibraryItemGenerator factory class."""

from book import Book
from dvd import DVD
from journal import Journal


class LibraryItemGenerator:
    """
    Factory class responsible for generating library items.

    Uses a registry of item classes. Each registered class defines
    ITEM_TYPE and EXTRA_FIELDS, so the factory can prompt for and
    construct any item type without type-specific if/elif logic.
    """

    _registry = [Book, DVD, Journal]

    @classmethod
    def register(cls, item_class):
        """
        Register a new LibraryItem subclass with the factory.
        :param item_class: a LibraryItem subclass with ITEM_TYPE and EXTRA_FIELDS
        """
        cls._registry.append(item_class)

    @classmethod
    def get_item_types(cls):
        """
        Returns a list of available library item type names.
        :return: a list of strings
        """
        return [item_cls.ITEM_TYPE for item_cls in cls._registry]

    @classmethod
    def create_item(cls):
        """
        Prompts the user to select an item type and enter item details,
        then creates and returns the appropriate library item.

        Uses the selected class's EXTRA_FIELDS to dynamically prompt
        for each field and build kwargs for the constructor.

        :return: a LibraryItem subclass instance, or None if cancelled
        """
        print("\nAvailable item types:")
        item_types = cls.get_item_types()
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

        selected_class = cls._registry[choice - 1]

        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        try:
            num_copies = int(input("Enter number of copies (positive number): "))
        except ValueError:
            print("Invalid number of copies.")
            return None

        kwargs = {}
        for field_name, prompt_text, field_type in selected_class.EXTRA_FIELDS:
            raw = input(prompt_text)
            try:
                kwargs[field_name] = field_type(raw)
            except ValueError:
                print(f"Invalid value for {field_name}.")
                return None

        return selected_class(call_number, title, num_copies, **kwargs)

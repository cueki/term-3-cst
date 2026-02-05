"""This module houses the Library class and main entry point."""

from book import Book
from dvd import DVD
from journal import Journal
from catalogue import Catalogue

# Madison Lovett A01292253
# Jan 28th, 2026


class Library:
    """
    The Library provides an interface for users to check out, return,
    and interact with library items. It delegates item management to
    the Catalogue class.

    The Library is dependent on Catalogue but decoupled from:
    - How items are stored (list, dictionary, database, etc.)
    - What search algorithm is used
    - The specific types of items (Book, DVD, Journal)

    This follows the Dependency Inversion Principle (DIP) and
    Single Responsibility Principle (SRP).
    """

    def __init__(self, catalogue):
        """
        Initialize the library with a catalogue.
        :param catalogue: a Catalogue object
        """
        self._catalogue = catalogue

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string, unique identifier
        """
        item = self._catalogue.retrieve_item_by_call_number(call_number)
        if item is None:
            print(
                f"Could not find item with call number {call_number}. Checkout failed."
            )
            return

        if item.check_availability():
            item.decrement_number_of_copies()
            print("Checkout complete!")
        else:
            print(f"No copies left for call number {call_number}. Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number to the library.
        :param call_number: a string, unique identifier
        """
        item = self._catalogue.retrieve_item_by_call_number(call_number)
        if item:
            item.increment_number_of_copies()
            print("Item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}. Return failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to access the
        list of items, check out, return, find, add, or remove items.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7): ")

            if string_input == "":
                continue

            try:
                user_input = int(string_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

            if user_input == 1:
                self._catalogue.display_all_items()
                input("Press Enter to continue")

            elif user_input == 2:
                call_number = input(
                    "Enter the call number of the item you wish to check out: "
                )
                self.check_out(call_number)

            elif user_input == 3:
                call_number = input(
                    "Enter the call number of the item you wish to return: "
                )
                self.return_item(call_number)

            elif user_input == 4:
                input_title = input("Enter the title of the item: ")
                found_titles = self._catalogue.find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(f"  - {title}")
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._catalogue.add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item: ")
                self._catalogue.remove_item(call_number)

            elif user_input == 7:
                pass

            else:
                print("Could not process the input. Please enter a number from 1 - 7.")

        print("Thank you for visiting the Library.")


def generate_test_items():
    """
    Return a list of library items with dummy data.
    :return: a list of LibraryItem objects
    """
    item_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss"),
        DVD("200.100.500", "The Matrix", 3, "1999-03-31", 1),
        DVD("200.100.501", "Inception", 2, "2010-07-16", 1),
        Journal(
            "300.400.100",
            "Nature Vol. 123",
            1,
            "Various Authors",
            "123",
            "Nature Publishing",
        ),
        Journal("300.400.101", "Science Weekly", 2, "Research Team", "456", "AAAS"),
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_items()
    catalogue = Catalogue(item_list)
    my_library = Library(catalogue)
    my_library.display_library_menu()


if __name__ == "__main__":
    main()

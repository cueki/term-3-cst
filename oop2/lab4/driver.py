"""
Dictionary Program Driver
A program that loads definitions from a file and allows users to query words.
"""

from dictionary import Dictionary, DictionaryNotLoadedError, WordNotFoundError
from file_handler import FileHandler, InvalidFileTypeError

# Madison Lovett A01292253
# Feb 4th, 2026


# File to save queried words and definitions
QUERY_LOG_FILE = "query_history.txt"
DISPLAY_WIDTH_WIDE = 60
DISPLAY_WIDTH_MEDIUM = 50
DISPLAY_WIDTH_NARROW = 40
EXIT_COMMAND = "exitprogram"


def display_welcome():
    """Display welcome message and instructions."""
    print("\n" + "=" * DISPLAY_WIDTH_WIDE)
    print("         WELCOME TO THE DICTIONARY PROGRAM")
    print("=" * DISPLAY_WIDTH_WIDE)
    print("\nInstructions:")
    print("  - Enter a word to look up its definition")
    print(f"  - Type '{EXIT_COMMAND}' to quit")
    print(f"  - All queries will be saved to {QUERY_LOG_FILE}")
    print("-" * DISPLAY_WIDTH_WIDE + "\n")


def display_definitions(word: str, definitions: list):
    """
    Display word definitions in a formatted manner.

    Args:
        word: The word being defined
        definitions: List of definitions
    """
    print(f"\n{'=' * DISPLAY_WIDTH_MEDIUM}")
    print(f"  Word: {word.upper()}")
    print(f"{'=' * DISPLAY_WIDTH_MEDIUM}")

    if len(definitions) == 1:
        print(f"\n  Definition: {definitions[0]}")
    else:
        print(f"\n  Definitions ({len(definitions)} found):")
        for i, definition in enumerate(definitions, 1):
            print(f"    {i}. {definition}")

    print(f"\n{'-' * DISPLAY_WIDTH_MEDIUM}\n")


def save_query(word: str, definitions: list):
    """
    Save the queried word and its definitions to a text file.

    Args:
        word: The word that was queried
        definitions: List of definitions found
    """
    lines = [f"Word: {word}", "Definitions:"]
    for i, definition in enumerate(definitions, 1):
        lines.append(f"  {i}. {definition}")
    lines.append("-" * DISPLAY_WIDTH_NARROW)

    try:
        FileHandler.write_lines(QUERY_LOG_FILE, lines)
    except Exception as e:
        print(f"Warning: Could not save query to log file: {e}")


def get_dictionary_source() -> str:
    """
    Prompt the user to select a dictionary source file.

    Returns:
        Path to the selected dictionary file
    """
    print("Available dictionary sources:")
    print("  1. data.json (comprehensive dictionary)")
    print("  2. data.txt (weather-related terms)")
    print("  3. Enter custom file path")

    while True:
        choice = input("\nSelect an option (1-3): ").strip()

        if choice == "1":
            return "data.json"
        elif choice == "2":
            return "data.txt"
        elif choice == "3":
            return input("Enter file path: ").strip()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


def main():
    """Main function to run the dictionary program."""
    display_welcome()
    dictionary = Dictionary()

    while not dictionary.is_loaded:
        filepath = get_dictionary_source()

        try:
            print(f"\nLoading dictionary from '{filepath}'...")
            dictionary.load_dictionary(filepath)
            print("Dictionary loaded successfully!")

        except FileNotFoundError as e:
            print(f"\nError: {e}")
            print("Please try again with a valid file path.")

        except InvalidFileTypeError as e:
            print(f"\nError: {e.message}")
            print("Please try again with a .json or .txt file.")

        except Exception as e:
            print(f"\nUnexpected error while loading dictionary: {e}")
            print("Please try again.")

    print("\n" + "-" * DISPLAY_WIDTH_WIDE)
    print("Dictionary is ready! Start entering words to look up.")
    print("-" * DISPLAY_WIDTH_WIDE)

    while True:
        try:
            user_input = input(
                f"\nEnter a word (or '{EXIT_COMMAND}' to quit): "
            ).strip()

            if user_input.lower() == EXIT_COMMAND:
                print("\n" + "=" * DISPLAY_WIDTH_WIDE)
                print("Thank you for using the Dictionary Program!")
                print(f"Your query history has been saved to '{QUERY_LOG_FILE}'")
                print("=" * DISPLAY_WIDTH_WIDE + "\n")
                break

            if not user_input:
                print("Please enter a word to look up.")
                continue

            definitions = dictionary.query_definition(user_input)

            display_definitions(user_input, definitions)
            save_query(user_input, definitions)

        except WordNotFoundError as e:
            print(f"\n{e.message}")
            if e.suggestions:
                print("Try one of the suggested words above.")

        except DictionaryNotLoadedError as e:
            print(f"\nError: {e.message}")
            break

        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Exiting...")
            break

        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            print("Please try again.")

        finally:
            # this runs after each iteration regardless of success or failure
            pass


if __name__ == "__main__":
    main()

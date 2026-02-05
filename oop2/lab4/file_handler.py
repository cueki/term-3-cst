"""
File handler module containing FileExtensions enum, custom exceptions,
and FileHandler class for managing file operations.
"""

from enum import Enum
from pathlib import Path
import json


class FileExtensions(Enum):
    """Enum representing valid file extensions for the dictionary program."""

    TXT = "txt"
    JSON = "json"
    # Invalid
    XML = "xml"
    CSV = "csv"
    INVALID = "invalid"


class InvalidFileTypeError(Exception):
    """Exception raised when an unsupported file type is encountered."""

    def __init__(self, file_extension: str, message: str = None):
        self.file_extension = file_extension
        if message is None:
            message = f"Invalid file type: '.{file_extension}'. Supported types are .txt and .json"
        self.message = message
        super().__init__(self.message)


class FileHandler:
    """
    A class to handle file operations for the dictionary program.
    Supports reading from .json and .txt files, and writing to .txt files.
    """

    VALID_EXTENSIONS = {FileExtensions.TXT, FileExtensions.JSON}

    @staticmethod
    def get_file_extension(filepath: str) -> FileExtensions:
        """
        Determine the file extension from a filepath.

        Args:
            filepath: Path to the file

        Returns:
            FileExtensions enum value

        Raises:
            InvalidFileTypeError: If the file extension is not supported
        """
        path = Path(filepath)
        extension = path.suffix.lower().lstrip(".")

        try:
            return FileExtensions(extension)
        except ValueError:
            raise InvalidFileTypeError(extension)

    @staticmethod
    def load_data(path: str, file_extension_enum: FileExtensions) -> dict:
        """
        Load data from a file based on its extension.

        Args:
            path: Path to the file to load
            file_extension_enum: FileExtensions enum indicating the file type

        Returns:
            Dictionary containing word-definition pairs

        Raises:
            InvalidFileTypeError: If the file type is not supported
            FileNotFoundError: If the file does not exist
            json.JSONDecodeError: If JSON parsing fails
        """
        if file_extension_enum not in FileHandler.VALID_EXTENSIONS:
            raise InvalidFileTypeError(
                file_extension_enum.value,
                f"File type '.{file_extension_enum.value}' is not supported. "
                f"Supported types are .txt and .json",
            )

        filepath = Path(path)
        if not filepath.exists():
            raise FileNotFoundError(f"File not found: '{path}'")

        if file_extension_enum == FileExtensions.JSON:
            return FileHandler._load_json(path)
        else:
            return FileHandler._load_txt(path)

    @staticmethod
    def _load_json(path: str) -> dict:
        """
        Load data from a JSON file.

        Args:
            path: Path to the JSON file

        Returns:
            Dictionary containing word-definition pairs
        """
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        normalized_data = {}
        for key, value in data.items():
            normalized_key = key.lower()
            if isinstance(value, str):
                value = [value]
            normalized_data[normalized_key] = value

        return normalized_data

    @staticmethod
    def _load_txt(path: str) -> dict:
        """
        Load data from a text file.
        Expected format: word:definition (one per line)
        Multiple definitions for the same word can be on separate lines.

        Args:
            path: Path to the text file

        Returns:
            Dictionary containing word-definition pairs
        """
        data = {}

        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line or ":" not in line:
                    continue

                parts = line.split(":", 1)
                if len(parts) == 2:
                    word = parts[0].strip().lower()
                    definition = parts[1].strip()

                    if word in data:
                        data[word].append(definition)
                    else:
                        data[word] = [definition]

        return data

    @staticmethod
    def write_lines(path: str, lines: list) -> None:
        """
        Write lines to a text file (append mode).

        Args:
            path: Path to the text file
            lines: List of strings to write
        """
        with open(path, "a", encoding="utf-8") as file:
            for line in lines:
                file.write(line + "\n")

    @staticmethod
    def write_definition(path: str, word: str, definition: str) -> None:
        """
        Write a word and its definition to a text file in the format word:definition.
        Appends to the file without overwriting existing content.

        Args:
            path: Path to the text file (typically data.txt)
            word: The word to add
            definition: The definition for the word

        Raises:
            ValueError: If word or definition is empty
        """
        if not word or not word.strip():
            raise ValueError("Word cannot be empty")
        if not definition or not definition.strip():
            raise ValueError("Definition cannot be empty")

        word = word.strip().lower()
        definition = definition.strip()

        with open(path, "a", encoding="utf-8") as file:
            file.write(f"{word}:{definition}\n")

"""
Dictionary module containing the Dictionary class for word lookup.
"""

import difflib
from file_handler import FileHandler

# Constants for word suggestion config
MAX_SUGGESTIONS = 5
SIMILARITY_CUTOFF = 0.6


class DictionaryNotLoadedError(Exception):
    """Exception raised when attempting to query an unloaded dictionary."""

    def __init__(
        self,
        message: str = "Dictionary has not been loaded. Please load a dictionary first.",
    ):
        self.message = message
        super().__init__(self.message)


class WordNotFoundError(Exception):
    """Exception raised when a word is not found in the dictionary."""

    def __init__(self, word: str, suggestions: list = None):
        self.word = word
        self.suggestions = suggestions or []
        if suggestions:
            suggestion_str = ", ".join(suggestions[:MAX_SUGGESTIONS])
            message = f"Word '{word}' not found. Did you mean: {suggestion_str}?"
        else:
            message = f"Word '{word}' not found in the dictionary."
        self.message = message
        super().__init__(self.message)


class Dictionary:
    """
    A class to manage dictionary operations including loading definitions
    and querying words.
    """

    def __init__(self):
        self._data = {}
        self._is_loaded = False

    @property
    def is_loaded(self) -> bool:
        """Check if the dictionary has been loaded."""
        return self._is_loaded

    def load_dictionary(self, filepath: str) -> None:
        """
        Load dictionary data from a file.

        Args:
            filepath: Path to the dictionary file (.json or .txt)

        Raises:
            InvalidFileTypeError: If the file type is not supported
            FileNotFoundError: If the file does not exist
        """
        # Determine file extension
        file_extension = FileHandler.get_file_extension(filepath)

        self._data = FileHandler.load_data(filepath, file_extension)
        self._is_loaded = True

    def query_definition(self, word: str) -> list:
        """
        Look up the definition(s) of a word.

        Args:
            word: The word to look up (case-insensitive)

        Returns:
            List of definitions for the word

        Raises:
            DictionaryNotLoadedError: If the dictionary hasn't been loaded
            WordNotFoundError: If the word is not found (includes suggestions)
        """
        if not self._is_loaded:
            raise DictionaryNotLoadedError()

        normalized_word = word.lower().strip()
        if normalized_word in self._data:
            return self._data[normalized_word]

        # try with difflib
        suggestions = self._find_similar_words(normalized_word)
        raise WordNotFoundError(word, suggestions)

    def _find_similar_words(
        self, word: str, n: int = MAX_SUGGESTIONS, cutoff: float = SIMILARITY_CUTOFF
    ) -> list:
        """
        Find similar words in the dictionary using difflib.

        Args:
            word: The word to find matches for
            n: Maximum number of suggestions to return
            cutoff: Minimum similarity ratio (0-1)

        Returns:
            List of similar words
        """
        all_words = list(self._data.keys())
        similar = difflib.get_close_matches(word, all_words, n=n, cutoff=cutoff)
        return similar

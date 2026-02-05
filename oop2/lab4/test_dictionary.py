"""
Unit tests for the Dictionary program.
"""

import unittest
import os
import json
import tempfile
import shutil

from file_handler import FileHandler, FileExtensions, InvalidFileTypeError
from dictionary import Dictionary, DictionaryNotLoadedError, WordNotFoundError


class TestFileHandler(unittest.TestCase):
    """Test cases for FileHandler."""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()

        cls.test_json_path = os.path.join(cls.test_dir, "test_data.json")
        with open(cls.test_json_path, "w") as f:
            json.dump({"Hello": ["A greeting."], "world": ["The earth."]}, f)

        cls.test_txt_path = os.path.join(cls.test_dir, "test_data.txt")
        with open(cls.test_txt_path, "w") as f:
            f.write("apple:A fruit.\napple:A company.\n")

        cls.write_test_path = os.path.join(cls.test_dir, "write_test.txt")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def setUp(self):
        if os.path.exists(self.write_test_path):
            os.remove(self.write_test_path)

    def test_load_data_json(self):
        """Test loading JSON file normalizes keys to lowercase."""
        data = FileHandler.load_data(self.test_json_path, FileExtensions.JSON)
        self.assertIn("hello", data)

    def test_load_data_txt(self):
        """Test loading TXT file with multiple definitions per word."""
        data = FileHandler.load_data(self.test_txt_path, FileExtensions.TXT)
        self.assertEqual(len(data["apple"]), 2)

    def test_load_data_invalid_extension(self):
        """Test loading with invalid extension raises error."""
        with self.assertRaises(InvalidFileTypeError):
            FileHandler.load_data("data.xml", FileExtensions.XML)

    def test_write_lines_creates_and_appends(self):
        """Test write_lines creates file and appends on subsequent calls."""
        FileHandler.write_lines(self.write_test_path, ["First"])
        FileHandler.write_lines(self.write_test_path, ["Second"])
        with open(self.write_test_path, "r") as f:
            content = f.read()
        self.assertIn("First", content)
        self.assertIn("Second", content)


class TestDictionary(unittest.TestCase):
    """Test cases for the Dictionary class."""

    @classmethod
    def setUpClass(cls):
        cls.test_dir = tempfile.mkdtemp()
        cls.test_json_path = os.path.join(cls.test_dir, "test_dict.json")
        with open(cls.test_json_path, "w") as f:
            json.dump(
                {
                    "Rain": ["Water from clouds."],
                    "rainy": ["Having rain."],
                },
                f,
            )

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def setUp(self):
        self.dictionary = Dictionary()

    def test_load_dictionary(self):
        """Test loading dictionary sets is_loaded."""
        self.assertFalse(self.dictionary.is_loaded)
        self.dictionary.load_dictionary(self.test_json_path)
        self.assertTrue(self.dictionary.is_loaded)

    def test_query_definition_case_insensitive(self):
        """Test queries work regardless of case."""
        self.dictionary.load_dictionary(self.test_json_path)
        self.assertEqual(
            self.dictionary.query_definition("rain"),
            self.dictionary.query_definition("RAIN"),
        )

    def test_query_definition_not_loaded(self):
        """Test querying unloaded dictionary raises error."""
        with self.assertRaises(DictionaryNotLoadedError):
            self.dictionary.query_definition("rain")

    def test_query_word_not_found_with_suggestions(self):
        """Test word not found includes suggestions."""
        self.dictionary.load_dictionary(self.test_json_path)
        with self.assertRaises(WordNotFoundError) as ctx:
            self.dictionary.query_definition("rainn")
        self.assertGreater(len(ctx.exception.suggestions), 0)

    def test_load_invalid_file_type(self):
        """Test loading invalid file type raises error."""
        with self.assertRaises(InvalidFileTypeError):
            self.dictionary.load_dictionary("data.xml")


if __name__ == "__main__":
    unittest.main()

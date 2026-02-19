"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzer:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    COMMON_PUNCTUATION = (",", "*", ";", ".", ":", "(", "[", "]", ")")

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode="r", encoding="utf-8") as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = []
        for line in self.text:
            if line != "\n":
                stripped_text.append(line)
        self.text = stripped_text

        # convert list of lines to list of words
        words = []
        for line in self.text:
            words.extend(line.split())
        self.text = words

        # remove common punctuation from words
        table = str.maketrans("", "", "".join(self.COMMON_PUNCTUATION))
        self.text = [word.translate(table) for word in self.text]

    @staticmethod
    def is_duplicate(word, word_list):
        """
        Checks to see if the given word appears in the provided sequence.
        This check is case in-sensitive.
        :param word: a string
        :param word_list: a sequence of words
        :return: True if not found, false otherwise
        """
        for a_word in word_list:
            if word == a_word:
                return False
        return True

    def find_different_words(self):
        """
        Filters out all the words to show different words in text.
        :return: a list of all the different words.
        """
        temp_text = self.text
        temp_lower = [w.lower() for w in temp_text]
        different_words = []
        while temp_text:
            word = temp_text.pop()
            temp_lower.pop()
            if self.is_duplicate(word.lower(), temp_lower):
                different_words.append(word)
        return different_words


def main():
    book_analyzer = BookAnalyzer()
    book_analyzer.read_data()
    different_words = book_analyzer.find_different_words()
    # print("-"*50)
    print(f"List of different words (Count: {len(different_words)})")
    # print("-"*50)
    # for word in different_words:
    #     print(word)
    # print("-" * 50)


if __name__ == "__main__":
    main()

from random import choice

class WordFinder:
    """Reads a file and creates a list of words"""
    
    def __init__(self, filename):
        """Takes a filename, reads it and creates a list of words."""
        self.word_list = self.create_word_list_from_file(filename)

    def __repr__(self):
        return f"<WordFinder word_list={self.word_list}>"

    def create_word_list_from_file(self, filename):
        """Opens a file and appends each line into a list."""
        
        word_file = open(filename)
        return [line.strip() for line in word_file]

    def random(self):
        """Returns a random item from the word list."""
        return choice(self.word_list)

class SpecialWordFinder(WordFinder):
    """Reads a file and creates a list of words, ignores lines that are blank or start with #"""

    def create_word_list_from_file(self, filename):
        """ Opens a file and appends each line (except blank lines and 
        ones that start with #) into a list. """

        word_file = open(filename)
        return [line.strip() for line in word_file if (line.strip() and not line.startswith('#'))]
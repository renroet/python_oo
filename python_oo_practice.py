class SerialGenerator:
    """creates next chronological serial number starting with user input"""

    def __init__(self, start=1):
        """creates starting number"""
        self.start = start
        self.serial = 0
        

    def generate(self):
        """creates next chronological serial number from starting positive number"""
        if self.serial < self.start:
            self.serial = self.start 
            return self.serial
        else:
            self.serial = self.serial + 1 
            return self.serial
    
    def reset(self):
        """resets serial number to starting number for next generation"""
        self.serial = 0


class WordFinder:
    """reads text file, shows number of words, and selects random word"""

    def __init__(self, file_path):
        """requires path to file to read. imports modules needed"""
        self.file = open(file_path, 'r')
        self.words = self.word_lst()
        self.num_words = self.count_words()
        print(f'{self.num_words} words read')
        from random2 import randrange
        self.rand = randrange
       
    def count_words(self):
        """counts number of words in list created from file"""
        return len(self.words)


    def word_lst(self):
        """lines of file individually put into list"""
        words = []
        for line in self.file:
            # word = line - '`n'
            words.append(line)
        return words

    def random(self):
        """selects random index of list and returns word without '\n' character trailing"""
        idx = self.rand(self.num_words)
        print(idx)
        if idx == len(self.words) - 1:
            return self.words[idx]
        else:
            return self.words[idx][:-1:]

class SpecialWordFinder(WordFinder):
    """subclass of WordFinder that filters out empty and comment lines in txt file"""

    def __init__(self, file_path):
        """inheriting initiation from WordFinder"""
        super().__init__(file_path)

    def word_lst(self):
        """function from WordFinder needed to be changed to filter out empty and comment lines in self.words"""
        """this overrides the super.__init__"""
        words = []
        for line in self.file:
            if not(line == "\n" or line.startswith('#')):
                words.append(line)
        return words

    



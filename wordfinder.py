"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    '''Find random words from file

    >>> wf = WordFinder('simple.txt')
    3 total words

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True
    '''


    def __init__(self, path):
        file = open(path)
        self.words = self.parse(file)

        print(f"{len(self.words)} total words")
    
    def parse(self, file):
        '''Return list of file words without /n'''
        return [word.strip() for word in file]
    
    def random(self):
        '''Return random word'''
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    '''More advanced search for finding words which excludes comments and blank lines
    
    >>> swf = SpecialWordFinder('complex.txt')
    3 total words

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True

    >>> swf.random() in ['pear', 'carrot', 'kale']
    True
    '''

    def parse(self, file):
        '''More advanced parse to get rid of blank lines and comments'''
        return [word.strip() for word in file if word.strip() and not word.startswith('#')]



        

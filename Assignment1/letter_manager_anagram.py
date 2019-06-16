from letter_manager import *

class Anagram:
    def __init__(self, _input1, _input2):
        '''
        LetterManager, LetterManager -> (None)
        '''
        self._input1 = _input1
        self._input2 = _input2
        self._is_anagram = False

    def __str__(self):
        return str(self._is_anagram)

    def same_word(self):
        '''
        None -> (boolean)
        Returns a boolean based on if the two inputs are anagrams
        '''
        blank = (str(self._input1) or str(self._input2)) == '[]'  #Checks if either inputs have blank inventories
        non_char = self._input1.non_char or self._input2.non_char  #Checks if either inputs have non-characters
        same_words = str(self._input1) == str(self._input2)  #Checks if their word counts are the same
        if not blank and not non_char and same_words:
            self._is_anagram = True #It is an anagram iff there are no blanks, no non-characters in the input and have the same character values
        return self._is_anagram

def main():
    #Main Method
    word1 = LetterManager(input("Please enter a word:"))
    word2 = LetterManager(input("Please enter a word:"))
    check = Anagram(word1, word2).same_word()
    print(check)

if __name__ == "__main__":
    main()


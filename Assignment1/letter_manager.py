class LetterManager:

    def __init__(self, _info):
        '''
        string -> (none)
        Constructs an inventory of the amount of instances a character appears in _info
        '''
        self._inventory = {}  #Keeps track of the amount of each character
        self._info = _info.lower()  #Sets everything to lowercase such that case sensitivity is not an issue
        self._glossary = 'abcdefghijklmnopqrstuvwxyz'  #String of accepted characters
        self.non_char = False  #Boolean that checks if there are non-characters in the input
        for char in self._glossary:  #Creates a dictionary of each character
            self._inventory[char] = 0  #Presets all values as zero
        for words in self._info:
            if words in self._inventory:
                self._inventory[words] += 1  #Fills the dictionary with the amount of characters found in the input(_info)
            else:
                self.non_char = True  #If there are any non characters, this boolean will be True

    def __str__(self):
        '''
        None -> (String)
        Returns a string of all the characters that appear in the inventory
        '''
        output = ''
        for char in self._glossary:
            output += (char * self._inventory[char])  #Creates a string of characters in alphabetical order
        return ('[' +output + ']')  #Desired output ex. "[abc]"

    def Get(self, _letter):
        '''
        char -> (int)
        Returns that amount of a specific character currently in _inventory
        '''
        _letter = _letter.lower()
        if _letter in self._inventory:
            return self._inventory[_letter]
        else:  #Error when a non-alphabetical character is inputted
            try:
                raise CharacterError(_letter)
            except CharacterError as e:
                print ('Error, invalid character "' + e._char + '" inputted')

    def Set(self, letter, value):
        '''
        char, int -> (None)
        Assigns a new character (_letter) amount according to a specified amount (_value)
        '''
        letter = letter.lower()  #Sets character to lower case so there are no discrepancies
        if not type(value) == int:  #Non-integer value error
            try:
                raise ValueError
            except ValueError:
                print('Error, non-integer inserted')
        elif (letter in self._glossary):  #Checks if the _letter is a character
            if value >= 0:
                self._inventory[letter] = value
            else:
                try:  #Error if the value is not an integer
                    raise SetError
                except SetError as error:
                    print(error)
        else:  #An error will come up if _letter is not a character or _value is not an integer,
            try: #Non-character error
                raise CharacterError(letter)
            except CharacterError as e:
                print ('Error, non-alphabetic character "' + e._char + '" inputted')

    def Size(self):
        '''
        None -> (int)
        Returns the sum of all the characters in the inventory
        '''
        return sum(self._inventory.values())

    def IsEmpty(self):
        '''
        None -> (None)
        Returns true iff _inventory does not have any characters in it
        I used .values to get a list of all the values and set() to simplify the values
        If the result is equal to {0} then _inventory is empty
        '''
        return set(self._inventory.values()) == {0}

    def Add(self, other):
        '''
        LetterManager -> (LetterManager)
        Takes another LetterManager object and adds the characters
        Returns a new LetterManager object
        '''
        new_object = self
        for words in new_object._inventory:
            new_object._inventory[words] += other._inventory[words]  #Adding characters
        return new_object

    def Subtract(self, other):
        '''
        LetterManager -> (LetterManager)
        Takes another LetterManager object and subtracts it with the current LetterManager
        Returns a new LetterManager object if character amounts are not negative
        Otherwise it will return None
        '''
        new_object = self
        for words in new_object._inventory:
            new_object._inventory[words] -= other._inventory[words]  #Subtracting Characters
            if new_object._inventory[words] < 0:  #Returns None if a character value is negative
                return None
        return new_object


class CharacterError(Exception):  #Error when a non-character is inserted in the argument
    def __init__(self, _char):  #Constructs the invalid character
        self._char = _char
    def __str__(self):  #Returns the invalid character
        return repr(self._char)

class SetError(Exception):
    def __str__(self):
        return "Error, negative value entered"
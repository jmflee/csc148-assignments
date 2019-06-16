from letter_manager import *
from letter_manager_anagram import *
import unittest

class TestLetterManager(unittest.TestCase):

    def test_str(self):
        '''Tests for the string representation of the LetterManager object'''
        test1 = LetterManager('apples')
        self.assertEqual('[aelpps]', str(test1))

    def test_constructor(self):
        '''Tests for a constructed inventory'''
        test1 = LetterManager('apples')
        expected = {'q': 0, 'y': 0, 'z': 0, 'h': 0, 'a': 1, 't': 0, 'u': 0, 'i': 0, 'b': 0, 'v': 0, 'w': 0, 'k': 0, 'p': 2, 'j': 0, 'l': 1, 'f': 0, 'd': 0, 'c': 0, 'm': 0, 'r': 0, 'g': 0, 'x': 0, 'o': 0, 'e': 1, 'n': 0, 's': 1}
        self.assertEqual(expected, test1._inventory)

    def test_characters_True(self):
        '''Tests for non-characters in the string'''
        test1 = LetterManager('/apple')
        self.assertEqual(True, test1.non_char)

    def test_characters_False(self):
        '''Tests for non-characters in the string'''
        test1 = LetterManager('apple')
        self.assertEqual(False, test1.non_char)

    def test_Get(self):
        '''Tests for amount of character values in the inventory'''
        test1 = LetterManager('falafel')
        self.assertEqual(2, test1.Get('f'))

    def test_Get_non_char_error(self):
        '''Tests when you input a non-character value'''
        test1 = LetterManager('falafel')
        self.assertRaises(CharacterError, test1.Get('/'))

    def test_Get_string_error(self):
        '''Tests when you input a string instead of a character'''
        test1 = LetterManager('falafel')
        self.assertRaises(CharacterError, test1.Get('pq'))

    def test_Set_pre_existing(self):
        '''Tests if you can assign new pre-existing character value in the inventory'''
        test1 = LetterManager('gas')
        test1.Set('g', 5)
        self.assertEqual('[agggggs]', str(test1))

    def test_Set_non_pre_existing(self):
        '''Tests if you can assign new non-pre-existing character value in the inventory'''
        test1 = LetterManager('abc')
        test1.Set('d', 5)
        self.assertEqual('[abcddddd]', str(test1))

    def test_Set_Size(self):
        '''Tests if you can use the return value for size as the second argument for the Set method'''
        test1 = LetterManager('abc')
        test1.Set('d', test1.Size())
        self.assertEqual('[abcddd]', str(test1))

    def test_Set_non_char_error(self):
        '''Tests when you input a non-character value for the first argument in Set()'''
        test1 = LetterManager('falafel')
        self.assertRaises(CharacterError, test1.Set('/', 5))

    def test_Set_string_error(self):
        '''Tests when you input a string instead of a character for the first argument in Get()'''
        test1 = LetterManager('falafel')
        self.assertRaises(CharacterError, test1.Set('pv', 5))

    def test_Set_non_int_error(self):
        '''Tests when you input a non-integer value for the second argument in Set()'''
        test1 = LetterManager('falafel')
        self.assertRaises(ValueError, test1.Set('p', 'p'))

    def test_Set_float_error(self):
        '''Tests when you input a float for the second argument of Set()'''
        test1 = LetterManager('abc')
        self.assertRaises(SetError, test1.Set('b', 5.5))

    def test_Set__neg_float_error(self):
        '''Tests when you input a negative float for the second argument of Set()'''
        test1 = LetterManager('abc')
        self.assertRaises(SetError, test1.Set('b', -5.5))

    def test_Size(self):
        '''Tests the size of the inventory'''
        test1 = LetterManager('orange')
        self.assertEqual(6, test1.Size())

    def test_Size_Set(self):
        '''Tests the size of the inventory when modified by the Set method'''
        test1 = LetterManager('aaaaabbbb')
        test1.Set('a', 2)
        test1.Set('b', 2)
        self.assertEqual(4, test1.Size())

    def test_Size_Subtract(self):
        '''Tests the size of the inventory when modified by the Subtract method'''
        test1 = LetterManager('abcdefg')
        test2 = LetterManager('defg')
        test3 = test1.Subtract(test2)
        self.assertEqual(3, test3.Size())

    def test_Size_zero(self):
        '''Tests the size of the inventory when it is zero'''
        test1 = LetterManager('')
        self.assertEqual(0, test1.Size())

    def test_Size_zero_Set(self):
        '''Tests the size of the inventory when it is set to zero by the Set method'''
        test1 = LetterManager('aaaaabbbb')
        test1.Set('a', 0)
        test1.Set('b', 0)
        self.assertEqual(0, test1.Size())

    def test_Size_zero_Subtract(self):
        '''Tests the size of the inventory when it is set to zero by the Subtract method'''
        test1 = LetterManager('aaaabbb')
        test2 = LetterManager('aaaabbb')
        test3 = test1.Subtract(test2)
        self.assertEqual(0, test3.Size())

    def test_IsEmpty_False(self):
        '''Tests if a string is not empty'''
        test1 = LetterManager('abc')
        self.assertEqual(False, test1.IsEmpty())

    def test_IsEmpty_False_Add(self):
        '''Tests if a string is not empty with the Add method'''
        test1 = LetterManager('')
        test2 = LetterManager('abc')
        test3 = test1.Add(test2)
        self.assertEqual(False, test2.IsEmpty())

    def test_IsEmpty_True(self):
        '''Tests if a string is empty'''
        test1 = LetterManager('')
        self.assertEqual(True, test1.IsEmpty())

    def test_IsEmpty_True_Subtract(self):
        '''Tests if a string is empty with the Subtract method'''
        test1 = LetterManager('abc')
        test2 = LetterManager('abc')
        test3 = test1.Subtract(test2)
        self.assertEqual(True, test3.IsEmpty())

    def test_Add(self):
        '''Tests the Add method'''
        test1 = LetterManager('abc')
        test2 = LetterManager('def')
        test3 = test1.Add(test2)
        self.assertEqual('[abcdef]', str(test3))

    def test_Add_empty(self):
        '''Tests the Add method with an empty object'''
        test1 = LetterManager('')
        test2 = LetterManager('def')
        test3 = test1.Add(test2)
        self.assertEqual('[def]', str(test3))

    def test_Add_all_empty(self):
        '''Tests the Add method with two empty objects'''
        test1 = LetterManager('')
        test2 = LetterManager('')
        test3 = test1.Add(test2)
        self.assertEqual('[]', str(test3))

    def test_Subtract(self):
        '''Tests the Subtract method'''
        test1 = LetterManager('abcd')
        test2 = LetterManager('abc')
        test3 = test1.Subtract(test2)
        self.assertEqual('[d]', str(test3))

    def test_Subtract_empty(self):
        '''Tests the Subtract method which results in an empty object'''
        test1 = LetterManager('abc')
        test2 = LetterManager('abc')
        test3 = test1.Subtract(test2)
        self.assertEqual('[]', str(test3))

    def test_Subtract_None(self):
        '''Tests the Subtract method  results in negative character values'''
        test1 = LetterManager('ab')
        test2 = LetterManager('abc')
        test3 = test1.Subtract(test2)
        self.assertEqual(None, test3)

    def test_Subtract_pre_blank_Set(self):
        '''Tests the Subtract method when it was previously blank and later populated with the Set method'''
        test1 = LetterManager('')
        test2 = LetterManager('')
        test1.Set('a', 3)
        test2.Set('a', 3)
        test3 = test1.Subtract(test2)
        self.assertEqual('[]', str(test3))

    def test_anagram(self):
        '''Tests for exact anagrams'''
        test1 = LetterManager('abc')
        test2 = LetterManager('cab')
        test3 = Anagram(test1, test2)
        self.assertEqual(True, test3.same_word())

    def test_anagram_non_char(self):
        '''Tests for anagrams where inputs contain non-characters
        Posted on Piazza: Since anagrams must be words, return False if there are ANY non-alphabetical characters in either string.'''
        test1 = LetterManager('abc/')
        test2 = LetterManager('cab$')
        test3 = Anagram(test1, test2)
        self.assertEqual(False, test3.same_word())

    def test_anagram_test1_greater_test2(self):
        '''Tests for anagrams where the first input is larger in length then the second input'''
        test1 = LetterManager('abccba')
        test2 = LetterManager('cab')
        test3 = Anagram(test1, test2)
        self.assertEqual(False, test3.same_word())

    def test_anagram_test1_lesser_test2(self):
        '''Tests for anagrams where the first input is smaller in length then the second input'''
        test1 = LetterManager('abc')
        test2 = LetterManager('cabcab')
        test3 = Anagram(test1, test2)
        self.assertEqual(False, test3.same_word())

    def test_anagram_blank_inputs(self):
        '''Tests for anagrams where both inputs are blank'''
        test1 = LetterManager('')
        test2 = LetterManager('')
        test3 = Anagram(test1, test2)
        self.assertEqual(False, test3.same_word())

    def test_anagram_blank_Set(self):
        '''Tests for anagrams where both inputs are set to blank lines by the Set method'''
        test1 = LetterManager('aaa')
        test2 = LetterManager('aaa')
        test1.Set('a', 0)
        test2.Set('a', 0)
        test3 = Anagram(test1, test2)
        self.assertEqual(False, test3.same_word())

    def test_anagram_pre_blank_Set(self):
        '''Tests for anagrams where both inputs are blank and is later populated with the Set method'''
        test1 = LetterManager('')
        test2 = LetterManager('')
        test1.Set('a', 3)
        test2.Set('a', 3)
        test3 = Anagram(test1, test2)
        self.assertEqual(True, test3.same_word())

if __name__ == '__main__':
    unittest.main(exit = False)
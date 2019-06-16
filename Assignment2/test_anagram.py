#**********************************************************
# Assignment2:
# UTOR user_name: leejos14
# First Name: Joseph
# Last Name: Lee
# Student # 1001175346
#
#
#
# Honour Code: I pledge that this program represents my own
# program code and that I have coded on my own. I received
# help from no one in designing and debugging my program.
# I have also read the plagiarism section in the course info sheet
# of CSC 148 and understand the consequences.
#*********************************************************

import unittest
from anagram import *
from letterManager import *

class TestAnagramSolver(unittest.TestCase):
	def test_zero_anagram(self):
		'''
		Tests an anagram where the max is zero
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('abb', 0), [['a', 'b', 'b'], ['ab', 'b'], ['b', 'a', 'b'], ['b', 'ab'], ['b', 'b', 'a']])

	def test_no_max_anagram(self):
		'''
		Tests an anagram where the max is not inputted
		Max is defaulted to zero if not inserted
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('abb'), [['a', 'b', 'b'], ['ab', 'b'], ['b', 'a', 'b'], ['b', 'ab'], ['b', 'b', 'a']])

	def test_limit_anagram(self):
		'''
		Tests an anagram where the max is not zero
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('abb', 2), [['ab', 'b'], ['b', 'ab']])

	def test_neg_anagram_error(self):
		'''
		Tests an anagram where the max is negative
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertRaises(ValueError, test.generateAnagrams, 'abb', -1)

	def test_no_anagram(self):
		'''
		Tests an anagram where the max is absurdly high
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('abb', 500), [['a', 'b', 'b'], ['ab', 'b'], ['b', 'a', 'b'], ['b', 'ab'], ['b', 'b', 'a']])

	def test_mix_anagram_zero(self):
		'''
		Tests an anagram where the input string has non-characters in it and max is zero
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('17846782151287abb53821$$$$!@$*)(', 0), [['a', 'b', 'b'], ['ab', 'b'], ['b', 'a', 'b'], ['b', 'ab'], ['b', 'b', 'a']])

	def test_mix_anagram_bound(self):
		'''
		Tests an anagram where the input string has non-characters in it and max is bounded
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('17846782151287abb53821$$$$!@$*)(', 2), [['ab', 'b'], ['b', 'ab']])

	def test_blank_anagram_zero(self):
		'''
		Tests an anagram where the input string is blank and max is zero
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('           ', 0), [])

	def test_blank_anagram_bound(self):
		'''
		Tests an anagram where the input string is blank and max is bounded
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('           ', 2), [])

	def test_int_anagram_zero(self):
		'''
		Tests an anagram where the input string contains an integer string and max is zero
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('12345', 0), [])

	def test_int_anagram_bound(self):
		'''
		Tests an anagram where the input string contains an integer string and max is bounded
		'''
		list = ['a', 'ab', 'c', 'b']
		test = AnagramSolver(list)
		self.assertEqual(test.generateAnagrams('12345'), [])

if __name__ == '__main__':
    unittest.main(exit = False)
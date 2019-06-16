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

from letterManager import *

class AnagramSolver:
	def __init__ (self, listOfWords):
		'''
		list -> (none)
		Takes a list of words instantiates it
		'''
		self._listOfWords = listOfWords
		self._relevant_list = []
		self._relevant_dist = {}
		self._master_list = []

	def __str__(self):
		return str(self._relevant_dist)

	def generateAnagrams (self, s, max = 0):
		'''
		string, int -> (list of lists)
		Takes a String s and returns a list of lists containing anagrams in s
		Max defaults to zero when max is not inputted
		'''
		input_string = LetterManager(s) #Creates a LetterManager of the s
		for word in self._listOfWords:  #Creates a list and dictionary of all the relevant words that are in the input
			if input_string.Subtract(LetterManager(word.lower())):
				self._relevant_list.append(word.lower())
				self._relevant_dist[word.lower()] = LetterManager(word) #Creates a LetterManager as a value for each key
		if max < 0: #Inputting a negative max results in a ValueError
			raise ValueError('Invalid Input: max is less then zero')
		else:
			self._master_list = self.buildAnagrams(input_string)  #Gets the list of lists for output
			if max > 0:
				output = [] #Create a duplicate when max is not 0
				for combination in self._master_list:  #Populates the output list only when the list corresponds with the max
					if len(combination) <= max:
						output.append(combination)
				return output
			else:
				return self._master_list #Returns everything

	def buildAnagrams(self, current):
		'''
		LetterManager -> (list of list)
		Takes a LetterManager and returns a list of lists containing all possible anagrams in the LetterManager
		'''
		_final_list = []
		for word in self._relevant_list: #Loops through the relevant words list
			possible = current.Subtract(self._relevant_dist[word])
			if possible:  #If possible exists then the word in the loops occurs in the string
				if str(possible) == '':  #Base Case is when the input is blank('')
					_final_list.append([word])  #Appends the word to the master_list
				else:
					if self.buildAnagrams(possible): #Checks if the function can reach the base case w/o yielding a blank master_list
						for displace in self.buildAnagrams(possible): #Loops through all the partial anagrams
							_final_list.append([word] + displace) #Appends the anagrams
		return _final_list

if __name__ == '__main__':
	a = open('dict.txt', 'r')
	c = []
	for b in a:
		c.append(b.strip())
	d = AnagramSolver(c)
	print(d.generateAnagrams('office key', 3))
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

from nodesrefs import BinaryTree

def ll2nr (l):
	'''
	list of lists -> (nodes and references)
	Takes a list of lists and returns a binary tree version of the list of lists
	'''
	bt = BinaryTree(l[0]) #Sets the roots node as the first element
	if not bt.getRootValue():  #Base Case when you reach a leaf node
		return None  #Returns None
	if l[1]: #If the left tree exists then make a subtree of the left
		bt.setLeftSubtree(ll2nr(l[1]))  #Processes the left subtree
	if l[2]:  #If the right subtree exists then make a subtree of the right
		bt.setRightSubtree(ll2nr(l[2]))  #Processes the right subtree
	return bt  #Returns the binary tree

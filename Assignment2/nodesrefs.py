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

class BinaryTree:
    def __init__(self, rootval):
        self.key = rootval
        self.left = None
        self.right = None

    def getRootValue(self):
        return self.key

    def getRightChild(self):
        return self.right

    def getLeftChild(self):
        return self.left

    def insertRightChild(self, val):
        t = BinaryTree(val)
        if self.right == None:
            self.right = t
        else:
            t.right = self.right
            self.right = t

    def insertLeftChild(self, val):
        t = BinaryTree(val)
        if self.left == None:
            self.left = t
        else:
            t.left = self.left
            self.left = t

    def setLeftSubtree (self, t):
        self.left = t

    def setRightSubtree (self, t):
        self.right = t
              
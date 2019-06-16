from stack import *
from stackops import *
import unittest

class TestStackOps(unittest.TestCase):

    def test_swap_Stack(self):
        '''Tests for a single swap operation with a Stack()'''
        test1 = Stack()
        test1.items = [1,2,3,4]
        swap(test1)
        self.assertEqual([1,2,4,3], test1.items)

    def test_multi_swap_Stack(self):
        '''Tests for a multiple swap operation with a Stack()'''
        test1 = Stack()
        test1.items = [1,2,3,4]
        for x in range(4):
            swap(test1)
        self.assertEqual([1,2,3,4], test1.items)

    def test_swap_Stack_error(self):
        '''Tests when you cannot swap a Stack() because the items are too small'''
        test1 = Stack()
        test1.items = [1]
        self.assertRaises(IndexError, swap(test1))

    def test_swap_Stack_empty_error(self):
        '''Tests when you cannot swap a Stack() because the items are empty'''
        test1 = Stack()
        test1.items = []
        self.assertRaises(IndexError, swap(test1))

    def test_swap_UpStack(self):
        '''Tests for a single swap operation with an UpStack()'''
        test1 = UpStack()
        test1.stack = [1,2,3,4]
        swap(test1)
        self.assertEqual([2,1,3,4], test1.stack)

    def test_multi_swap_UpStack(self):
        '''Tests for a single swap operation with an UpStack()'''
        test1 = UpStack()
        test1.stack = [1,2,3,4]
        for x in range(4):
            swap(test1)
        self.assertEqual([1,2,3,4], test1.stack)

    def test_swap_UpStack_error(self):
        '''Tests when you cannot swap a UpStack() because the items are too small'''
        test1 = UpStack()
        test1.stack = [1]
        self.assertRaises(SizeError, swap(test1))

    def test_swap_UpStack_empty_error(self):
        '''Tests when you cannot swap a UpStack() because the items are empty'''
        test1 = UpStack()
        test1.stack = []
        self.assertRaises(SizeError, swap(test1))

    def test_swap_wrong_type_error(self):
        '''Tests when you cannot swap because a non-stack was entered as an argument'''
        self.assertRaises(StackError, swap('this is a string and not a stack'))

    def test_roll_Stack(self):
        '''Tests for a single roll operation with a Stack'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        roll(test1, 5)
        self.assertEqual([2,3,4,5,1], test1.items)

    def test_roll_UpStack(self):
        '''Tests for a single roll operation with an UpStack'''
        test1 = UpStack()
        test1.stack = [1,2,3]
        roll(test1, 3)
        self.assertEqual([3,1,2], test1.stack)

    def test_no_roll_error(self):
        '''Tests when you use zero as the nth value for the roll method'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        self.assertRaises(NthError, roll(test1, 0))

    def test_negative_roll_error(self):
        '''Tests when you use a negative integer as the nth value for the roll method'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        self.assertRaises(NthError, roll(test1, -5))

    def test_float_roll_error(self):
        '''Tests when you use a float as the nth value for the roll method'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        self.assertRaises(NthError, roll(test1, 5.5))

    def test__neg_float_roll_error(self):
        '''Tests when you use a negative float as the nth value for the roll method'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        self.assertRaises(NthError, roll(test1, -5.5))

    def test_roll_Stack_greater_error(self):
        '''Tests when nth term is larger then the stack'''
        test1 = Stack()
        test1.items = [1,2,3,4,5]
        self.assertRaises(NthError, roll(test1, 6))

    def test_roll_nth_error(self):
        '''Tests when a non-integer is inserted in the roll method as the nth value'''
        self.assertRaises(NthError, roll('vrooom', 'this is a string and not an integer'))

    def test_roll_stack_type_error(self):
        '''Tests when a non-stack is inserted in the roll method'''
        self.assertRaises(StackError, roll('vrooom', 6))

if __name__ == '__main__':
    unittest.main(exit = False)
from word_processor import *
import unittest

class TestWordProcessor(unittest.TestCase):

    def test_one_insert(self):
        '''Tests for a singular insertion operation'''
        test = Word_Processor()
        test.insert('apples')
        self.assertEqual(['apples'], test._document)

    def test_multiple_insert(self):
        '''Tests for a multiple insertion operations with different symbols such as floats, integers and symbolts'''
        test = Word_Processor()
        list = ['first', 2, 3.0, 8/2, 'fifth', 'sixth', 'seventh', 'eighth']
        for words in list:  #Inserts all the values of list into the document
            test.insert(words)
        self.assertEqual(['first', 2, 3.0, 4.0, 'fifth', 'sixth', 'seventh', 'eighth'], test._document)

    def test_one_redo(self):
        '''Tests for a singular redo operation'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._redo.items = [['first'], ['first', 'third']]
        self.assertEqual(['first', 'third'], test.redo())

    def test_multiple_redo(self):
        '''Tests for a multiple redo operations'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._redo.items = [['first'], ['first', 'third'], ['first', 'third', 'fourth'], ['first', 'second']]
        for x in range(4):
            output = test.redo()
        self.assertEqual(['first'], output)

    def test_invalid_redo_error(self):
        '''Tests when a redo is no longer possible'''
        test = Word_Processor()
        self.assertRaises(IndexError, test.redo())

    def test_one_undo(self):
        '''Tests for one undo operation'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._undo.items = [['first'], ['first', 'third']]
        self.assertEqual(['first', 'third'], test.undo())

    def test_multiple_undo(self):
        '''Tests for a multiple undo operations'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._undo.items = [['first'], ['first', 'third'], ['first', 'third', 'fourth'], ['first', 'second']]
        for x in range(4):
            output = test.undo()  #Stops at ['first']
        self.assertEqual(['first'], output)

    def test_invalid_undo_error(self):
        '''Tests when an undo is no longer possible'''
        test = Word_Processor()
        self.assertRaises(IndexError, test.undo())

    def test_redo_undo(self):
        '''Tests for a singular undo operation followed by a redo operation'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._undo.items = [['first', 'third']]
        test.undo()
        output = test.redo()
        self.assertEqual(['first', 'second', 'third'], output)

    def test_multiple_redo_undo(self):
        '''Tests for a multiple undo operations followed by multiple redo operations'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._undo.items = [['first'], ['first', 'third'], ['first', 'third', 'fourth'], ['first', 'second']]
        for x in range(4):
            test.undo()  #Stops at ['first']
        for y in range(2):
            output = test.redo()  #Stops at ['first', 'third', 'fourth']
        self.assertEqual(['first', 'third', 'fourth'], output)

    def test_one_delete(self):
        '''Tests for deleting one line from the document'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        self.assertEqual(['first', 'third'], test.delete(2))

    def test_multiple_delete(self):
        '''Tests for deleting multiple lines at different locations in the document'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
        for x in range(8,1,-1): #Deletes all the elements except for 'first'
            output = test.delete(x)
        self.assertEqual(['first'], output)

    def test_invalid_delete_index_error(self):
        '''Tests when a specified delete line is not in the document'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        self.assertRaises(IndexError, test.delete(5))

    def test_invalid_delete_type_error(self):
        '''Tests when a specified delete line is not an integer'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        self.assertRaises(ValueError, test.delete('words'))

    def test_delete_float_error(self):
        '''Tests when you set a delete line as a float'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        self.assertRaises(ValueError, test.delete(5.5))

    def test_delete_neg_float_error(self):
        '''Tests when you set a delete line as a float'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        self.assertRaises(ValueError, test.delete(-5.5))

    def test_one_del_undo(self):
        '''Tests when you undo a deleted line'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test.delete(2)
        output = test.undo()
        self.assertEqual(['first', 'second', 'third'], output)

    def test_multiple_del_undo(self):
        '''Tests for a multiple delete operations followed by multiple undo operations'''
        test = Word_Processor()
        test._document = ['first', 'second', 'third']
        test._document = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth']
        for x in range(8,1,-1):  #Deletes all the elements except for 'first'
            output = test.delete(x)
        for y in range(6):  #Undo all the operations deletes except for 'eighth'
            output = test.undo()
        self.assertEqual(['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh'], output)


if __name__ == '__main__':
    unittest.main(exit = False)
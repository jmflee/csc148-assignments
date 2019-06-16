from stack import *

def swap(s):
    '''
    object -> (None)
    swap top two items on stack s
    '''
    if type(s) == UpStack or type(s) == Stack:  #Only accepts Stack and UpStack objects
        if s.size() > 1:
            old_front = s.peek()  #Saves the front of the stack
            s.pop()  #Pops it
            new_front = s.peek()  #Saves the new front of the stack
            s.pop()  #Pops it
            s.push(old_front)  #Push int the original front value
            s.push(new_front)  #Push in the new front value
        else:  #Will result in an error if length of the stack is less then one
            try:
                raise SizeError
            except SizeError as error:
                print(error)
    else:  #If stacks objects are not inputted, an error will appear
        try:
            raise StackError
        except StackError as error:
            print(error)

def roll (s, n):
    '''
    object, int -> (None)
    perform the roll operation on a stack s.
    A roll with integer n causes the nth item from the top to be removed
    and placed on top of the stack.
    '''
    temp = Stack()
    if not (type(s) == Stack or type(s) == UpStack):  #Error if a stack object is not inserted in the first argument
        try:
            raise StackError
        except StackError as error:
            print(error)
    elif not type(n) == int or n <= 0 or n > s.size():
        try:
            raise NthError
        except NthError as error:  #Error if the nth element is larger then the stack or is negative or is a non-integer
            print(error)
    else: #Roll will only work if the first argument is a Stack object and it's second argument is an integer
        for x in range(n):  #Pops all the elements in the stack until nth element is reached
            temp.push(s.pop())  #A temporary stack will keep track of all the popped elements
        new_front = temp.pop()  #The nth item will always be in the front of the stack
        for y in range(temp.size()):
            s.push(temp.pop())  #Repush the remaining elements in the temporary stack
        s.push(new_front)  #Finally it pushes the nth element to the front

class SizeError(Exception): #Error when the size of the stack is too small
    def __str__(self):
        return 'Error, stack size too small to change'

class NthError(Exception):  #Error when the nth item is lesser or equal to zero or greater then the size of the stack
    def __str__(self):
        return 'Error, nth item cannot be computed'

class StackError(Exception):  #Error when a stack is not inserted in the argument
    def __str__(self):
        return 'Error, stack was not inputted as an argument'
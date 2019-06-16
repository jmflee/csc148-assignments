from stack import Stack

class Word_Processor:

    def __init__ (self):
        '''
        None -> (None)
        A new _document list to store user input and a stack object for _undo and _redo
        to keep track of revisions requested by the user.
        UpStack isn't efficient since it has to shift each element to the right
        which wastes time.
        '''
        self._document = []
        self._undo = Stack() #Everytime there is a command aside from undo, the stack will be filled with the previous version of the document
        self._redo = Stack()  #Everytime the undo function is called, an instance of the document prior to the operation will be kept in the stack

    def __str__(self):
        return (str(self._document))

    def delete(self, position):
        '''
        int -> (list)
        Returns and removes an element from _document
        '''
        try:
            self._document[int(position)-1]  #This checks if the line is an integer and coincides in the _document
            if not type(int(position)) == int:  #Raises a ValueError when a non-integer is inserted
                raise ValueError
        except ValueError:
            print("Error, input was not an integer")
        except IndexError:
            print("Error, line number not found in document")
        else:
            self._redo.items = []  #_redo becomes blank because you cannot redo when you delete an item in _document
            self._undo.push(list(self._document)) #Create a copy of the _document in _undo if the users decides to undo()
            self._document.pop(int(position) - 1)  #I set it to int(position)-1 since the example appeared to list delete from [1,infinity]
            return self._document


    def undo(self):
        '''
        None -> (list)
        Returns the second most recent revision of _document
        '''
        if self._undo.isEmpty(): #No more undo operations result in an error
            try:
                raise ValueError
            except ValueError:
                print("Error, undo not possible!")
        else:
            self._redo.push(list(self._document)) #Creates a copy of the _document in _redo if the user decides to redo() their undo()
            self._document = self._undo.peek()
            self._undo.pop()  #_undo follows fifo and as such, the second most recent element will be in front when called again
            return self._document

    def redo(self):
        '''
        None -> (list)
        Returns and reverses the previous change to _document caused by undo()
        '''
        if self._redo.isEmpty():  #No more redo operations result in an error
            try:
                raise ValueError
            except ValueError:
                print("Error, redo not possible")
        else:
            self._undo.push(list(self._document)) #Creates a copy of the _document in _undo if the user decides to undo() their redo()
            self._document = list(self._redo.peek())
            self._redo.pop()  #_redo follows fifo and as such, the second most recent element will be in front when called again
            return self._document

    def insert(self, line):
        '''
        None -> (None)
        Appends the variable line to _document
        '''
        self._redo.items = []  #_redo becomes blank because you cannot redo when you add a new item in _document
        self._undo.push(list(self._document))  #Creates a copy of _document in _undo if the user decides to undo()
        self._document.append(line)
        return self._document

def main():
    #Main Method
    program = Word_Processor()
    command = None
    key_words = ['', 'd', 'undo', 'redo']
    while not command == '': #Repeatedly asks for a command until a blank line is entered
        command = input("Command?")
        if not command in key_words:
            program.insert(command)
            print(program)
        elif command == 'undo':
            program.undo()
            print(program)
        elif command == 'redo':
            program.redo()
            print(program)
        elif command == 'd':
            program.delete(input("Delete which line?"))
            print(program)

if __name__ == "__main__":
    main()


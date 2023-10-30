#
# Connect 4 game board implementation
#
# Name: 

class Board:
    """Class that defines a Connect 4 Board."""

    def __init__(self, width = 7, height = 6):
        """Construct a board of size width x height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for r in range(height)]

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __repr__(self):
        """Return a string representation for an object of type Board.
        """
        s = ''                  # The string to return
        for row in range(self.height):
            s += '|'            # Add the spacer character
            for col in range(self.width):
                s += self.data[row][col] + '|'
            s += '\n'
        s += '--' * self.width  # Add the bottom of the board
        s += '-\n'
        for col in range(self.width):
            s += ' ' + str(col % 10) # Add labels
        s += '\n'
        return s                # The board is complete, return it

    def addMove(self, col, ox):
        """Add the game piece ox (either 'X' or 'O') to column col."""


        # Loop from the bottom to the top. check the col index is == "". If yes, add there. Else, loop 
        for i in range(len(self.data)):
            if self.data[-(i+1)][int(col)] == " ":
                self.data[-(i+1)][int(col)] = ox 
                break 
        

    def clear(self):
        """Clear the game board of all game pieces."""
        self.data = [[' ']*self.width for r in range(self.height)]

    def setBoard(self, moves):
        """Set the board using an input string representation."""
        oorx = "X"
        for i in moves:
            self.addMove(i,oorx)
            if oorx == "X": 
                oorx = "O"
            else:
                oorx = "X"


    def allowsMove(self, col):
        """Return True if adding a game piece in the given column is
           permitted and return False otherwise."""
        for i in range(len(self.data)):
            if self.data[-(i+1)][col] == " ":
                return True
        return False

    def isFull(self):
        """Return True if the game board is full and False otherwise."""
        for r in self.data:
            for c in r:
                if c == " ":
                    return False
                
        return True

    def delMove(self, col):
        """Delete the topmost game piece from the given column."""
        for i in self.data:
            if i[col] != " ":
                i[col] = " "
                return "Done"

    def winsFor(self, ox):
        """Return True if the game has been won by player ox where ox
           is either 'X' or 'O'."""
        if self.horizontal(ox) or self.vertical(ox) or self.right_diagonal(ox) or self.left_diagonal(ox):
            return True 
        return False
    def horizontal(self, ox):
        count = 0 
        for r in self.data:
            for c in r:
                if c!= ox and count != 0:
                    count=0
                if c == ox:
                    count += 1
                if count >= 4:
                    return True 
            count = 0 
        return False
    def vertical(self,ox):
        #b.setBoard("0100000")
        l = {}
        for r in range(len(self.data)):
            for c in range(len(self.data[0])):
                if r == 0 or self.data[r][c] != ox:
                    l[c] = 0
                if self.data[r][c] == ox:
                    l[c] += 1 
        for i in l.values():
            if i >= 4:
                return True 
        return False 
    def right_diagonal(self,ox):
        l = {}
        # l is the dictionary used to keep track of the row and column that we expect to have ox
        # and the number of times this chain has continued. 
        # an element would look like (2,3): 3 
        for r in range(len(self.data)):
            # for each row
            for c in range(len(self.data[0])):
                # for each column 
                if self.data[r][c] == ox:
                    # if where we are at is the symbol we want
                    if (r,c) in l.keys(): 
                        print(l)
                        # and it is part of a continuing chain
                        l[(r+1,c+1)] = l[(r,c)] + 1
                        # then add the next element we expect in the chain
                        del l[(r,c)]
                        # delete our current placeholder. 
                    else:
                        print(r,c)
                        # start the chain
                        l[(r+1,c+1)] = 1
                elif (r,c) in l.keys() and l[(r,c)] < 4:
                    # if we did not get the symbol we were expecting and we should have continued a chain, 
                    # delete the chain from the dictionary  
                    del l[(r,c)]
         
        for i in l.values():
            if i>=4: 
                return True 
                # if our chain has more than 4, then we have a diagonal. 

        return False 
    def left_diagonal(self,ox):

        ''' 
        Idea is that we loop through and find that if there is supposed to be a left diagonal, 
        where would it be (1 row below, 1 column to the left)

        Thus, we keep track of where the oxs are and if they have a chain of oxs to their diagonal left. 
        '''
        l = {}
        # l is the dictionary used to keep track of the row and column that we expect to have ox
        # and the number of times this chain has continued. 
        # an element would look like (2,3): 3 
        for r in range(len(self.data)):
            # for each row
            for c in range(len(self.data[0])):
                # for each column 
                if self.data[r][c] == ox:
                    # if where we are at is the symbol we want
                    if (r,c) in l.keys(): 
                        print(l)
                        # and it is part of a continuing chain
                        l[(r+1,c-1)] = l[(r,c)] + 1
                        # then add the next element we expect in the chain
                        del l[(r,c)]
                        # delete our current placeholder. 
                    else:
                        print(r,c)
                        # start the chain
                        l[(r+1,c-1)] = 1
                elif (r,c) in l.keys() and l[(r,c)] < 4:
                    # if we did not get the symbol we were expecting and we should have continued a chain, 
                    # delete the chain from the dictionary  
                    del l[(r,c)]
         
        for i in l.values():
            if i>=4: 
                return True 
                # if our chain has more than 4, then we have a diagonal. 

        return False 



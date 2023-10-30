import random 
class Player:
    """Class that defines a Connect 4 player."""

    def __init__(self, ox, tbt, ply):
        """Create a Player who plays ox ("O" or "X") using tbt as the
           tie-breaking type.  The player will look ahead up to ply
           plies."""
        self.ox = ox
        self.tbt = tbt
        self.ply = ply

    def __repr__(self):
        output = f'Player for {self.ox}'
        output += f' with tiebreak {self.tbt}'
        output += f' and ply = {self.ply}\n'
        return output

    def oppChar(self):
        """Return the opposite game pi ece character."""
        if self.ox  == "O":
            return "X"
        else:
            return "O"

    def scoreBoard(self, b):
        """Return a score for the given board b."""
        if b.winsFor(self.ox):
            return 100.0
        if b.winsFor(self.oppChar()):
            return 0.0
        else: return 50.0
        
        
    def tiebreakMove(self, scores):
        """Return the column number to move in, based on self.tbt."""
        # and the score 
        d = {}
        max_val = - 1
        for index, value in enumerate(scores):
            d.setdefault(value, [index]).append(index)
            if value>max_val: max_val = value

        if self.tbt== "LEFT":
            return [d[max_val][0],max_val]
        if self.tbt == "RIGHT":
            return [d[max_val][-1],max_val]
        if self.tbt == "RANDOM":
            return [random.choice(d[max_val]),max_val]
            
    def i_won(self,b):
        ''' Check if I won '''
        if b.winsFor(self.ox):
            return True 
        return False 
    def opp_won(self, b,l):
        ''' Check if opp won '''
        if b.winsFor(self.oppChar()): return True
        return False

    def full_col(self,b,c):
        ''' Check if col is full'''
        if  b.allowsMove(c): return False
        return True 
    def full_board(self,b):
        ''' Check if board is full'''
        for i in range(b.getWidth()):
            if not self.full_col(b,i):
                return False 
        return True 
    def scoresFor(self, b):
        """Return a list of scores for board b, one score for each column
           of the board."""

        final_list = [50] * b.getWidth()

        for c in range(b.getWidth()):
            print(c)
            if self.full_col(b,c): 
                print("full")
                final_list[c] = -1 
            elif self.i_won(b):
                print("won")
                final_list[c] = 100 
            elif self.opp_won(b,final_list):
                print("opp_won")
                final_list[c] = 0 

            elif self.ply == 0:
                print("ply=0")
                final_list[c] = 50 

            else: 
                print("base case 4")
                b.addMove(c,self.ox)
                if self.full_col(b,c): 
                    final_list[c] = -1 
                elif self.i_won(b):
                    final_list[c] = 100
                
                print("Created opp")
                opponent = Player(self.oppChar(),self.tbt, self.ply-1)
                opponent_moves = opponent.scoresFor(b)
                print("Opponent destroyed")
                # find the max in opponent moves, subtract it from a 100 as the column 
                # make sure opponents best score isn't -1 
                # delete all game pieces 
                col_to_move, max_score = opponent.tiebreakMove(opponent_moves)
                final_list[c] = 100 - max_score
                b.delMove(c)
        return final_list
    
        

    def nextMove(self, b):
        """Return the next move for this player, where a move is a column
           in which the player should place its game piece."""

        scores = self.scoresFor(b)
        return self.tiebreakMove(scores)[0]


#
# Connect 4 game
#
# Name: 
#

from board import *
from player import *

#
# Main function that implements a human-vs.-AI Connect 4 game.
# You don't need to write any code here.
#
def main():
    """Play a single game of Connect 4 against a human."""
    ply = int(input("Enter ply (level from 0 to 5): "))
    px = "human"
    po = Player("O", "LEFT", ply)
    b = Board(7, 6)
    playGame(b, px, po)

def playGame(b, px, po):
    """Play a game of Connect Four.
       px and po are objects of type Player OR the string "human".
       If either is a Player object, px must have a player symbol of "X"
       and po must have a symbol of "O".
    """
    #
    # The game starts with "X" moving.  The nextPieceToMove and
    # nextPlayerToMove variables will alternate between "X" and "O"
    # (you might or might not need both variables).  At the end of the
    # game, nextPieceToMove and nextPlayerToMove should give the
    # identity of the winning player.  the nextPieceToMove will
    # alternate during game play, so the nextPieceToMove at the end of
    # the game will be the winner which could be "X" or "O".
    #
    nextPieceToMove = "O"
    nextPlayerToMove = po

    while not b.winsFor(nextPieceToMove):

        if nextPieceToMove == "X": nextPieceToMove = "O"
        else: nextPieceToMove = "X"
        if nextPlayerToMove == po: nextPlayerToMove = px
        else: nextPlayerToMove = po

        if nextPlayerToMove == "human":
            col_to_move = int(input("What column would you like to move?"))
            b.addMove(col_to_move,nextPieceToMove)
        else:
            #print(nextPlayerToMove)
            b.addMove(int(nextPlayerToMove.nextMove(b)), nextPieceToMove)
        print(b)
        
    print(nextPieceToMove + " wins!")        
    

    # FILL IN CODE HERE

    #
    # In case we're being called from an automatic player (e.g., the
    # tournament), return the winning board and the (character)
    # identity of the winning player.
    #
    return(b.data, nextPieceToMove)

if __name__ == '__main__':
    main()

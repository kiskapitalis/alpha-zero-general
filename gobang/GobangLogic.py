'''
Author: MBoss
Date: Jan 17, 2018.
Board class.
Board data:
  1=white, -1=black, 0=empty
  first dim is column , 2nd is row:
     pieces[1][7] is the square in column 2,
     at the opposite end of the board in row 8.
Squares are stored and manipulated as (x,y) tuples.
x is the column, y is the row.
'''
class Board():
    def __init__(self, col, row):
        "Set up initial board configuration."
        self.col = col
        self.row = row
        # Create the empty board array.
        self.pieces = [None]*self.col
        for i in range(self.col):
            self.pieces[i] = [0]*self.row

    # add [][] indexer syntax to the Board
    def __getitem__(self, index): 
        return self.pieces[index]

    def get_legal_moves(self, color):
        """Returns all the legal moves for the given color.
        (1 for white, -1 for black
        """
        moves = set()  # stores the legal moves.

        # Get all empty locations.
        for x in range(self.col):
            for y in range(self.row):
                if self[x][y] == 0:
                    moves.add((x, y))
        return list(moves)

    def has_legal_moves(self):
        """Returns True if has legal move else False
        """
        # Get all empty locations.
        for x in range(self.col):
            for y in range(self.row):
                if self[x][y] == 0:
                    return True
        return False

    def execute_move(self, move, color):
        """Perform the given move on the board; flips pieces as necessary.
        color gives the color pf the piece to play (1=white,-1=black)
        """
        (x,y) = move
        assert self[x][y] == 0
        self[x][y] = color


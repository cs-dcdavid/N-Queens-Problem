# A Chessboard is made up of 
#    columns (called "files" that are letters from a to g) and 
#    row (called "ranks" that are numbers from 1 to 8). Therefore,
#    if a chess piece is said to be in "e4",
#    then it is in the "e file" (5th column) and "4th rank" (4th column)
class Queen:
    def __init__(self, position):
        self.file = position[0]
        self.rank = int(position[1])
    
    # --------------------------------------------------------
    # Static methods to get the next/previous files and ranks
    @staticmethod
    def next_file(file):
        return chr(ord(file) + 1)
    @staticmethod
    def prev_file(file):
        return chr(ord(file) - 1)
    @staticmethod
    def next_rank(file):
        return rank + 1
    @staticmethod
    def prev_rank(file):
        return rank - 1
    # --------------------------------------------------------
    
    # Check for intersections in the file "|"
    def check_file(self, queen2):
        return self.file == queen2.file
    
    # Check for intersections in the rank "—"
    def check_rank(self, queen2):
        return self.rank == queen2.rank
    
    # Check for intersections in the rising diagonal "⟋"
    def check_rising_diagonal(self, queen2):
        pass
    
    # Check for intersections in the falling diagonal "⟍"
    def check_falling_diagonal(self, queen2):
        pass
    
    # Check for intersections in the file, rank, and both diagonals
    def intersects_with(self, queen2):
        Queen.next_file(self.file)

q1 = Queen('a3')
q2 = Queen('a3')

q1.intersects_with(q2)




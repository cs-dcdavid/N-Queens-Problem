# A Chessboard is made up of 
#    columns (called "files" that are letters from a to g) and 
#    row (called "ranks" that are numbers from 1 to 8). Therefore,
#    if a chess piece is said to be in "e4",
#    then it is in the "e file" (5th column) and "4th rank" (4th column)
class Queen:
    def __init__(self, position):
        self.file = ord(position[0]) - 96
        self.rank = int(position[1])
    
    # Check for intersections in the file "|"
    def check_file(self, queen2):
        pass
    
    # Check for intersections in the rank "—"
    def check_rank(self, queen2):
        pass
    
    # Check for intersections in the rising diagonal "⟋"
    def check_rising_diagonal(self, queen2):
        pass
    
    # Check for intersections in the falling diagonal "⟍"
    def check_falling_diagonal(self, queen2):
        pass
    
    # Check for intersections in the file, rank, and both diagonals
    def intersects_with(self, queen2):
        

q1 = Queen('a3')
q2 = Queen('a3')

print(q1.rank - 2)




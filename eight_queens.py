from itertools import permutations  
import math 

# The n-Queens puzzle is the problem of placing 
# n-Queens in an n-by-n chessboard
class Chessboard:
    def __init__(self, n):
        self.n = n
        self.files = self.generate_files()
        self.ranks = self.generate_ranks()
        self.queens = []
    
    # int -> [file-a, file-b, ... nth-file]
    def generate_files(self):
        files = []
        file = 'a'
        for i in range(self.n):
            files.append(chr(ord(file) + i))
        return files
    
    # int -> [rank-1, rank-2, ... rank-n]
    def generate_ranks(self):
        ranks = []
        for i in range(self.n):
            i += 1
            ranks.append(i)
        return ranks

# A Chessboard is made up of 
#    columns (called "files" that are letters from a to g) and 
#    row (called "ranks" that are numbers from 1 to 8). Therefore,
#    if a chess piece is said to be in "e4",
#    then it is in the "e file" (5th column) and "4th rank" (4th column)
class Queen:
    def __init__(self, position, board):
        self.position = position
        self.file = position[0]
        self.rank = int(position[1])
        self.board = board
    
    # Check for two queens in the same position
    # Queen, Queen -> bool
    #              -> true (if the two queens are in the same position)
    #              -> false (if the two queens are in the same position)
    @staticmethod
    def same_position(queen1, queen2):
        return queen1.position == queen2.position
    
    # Check for intersections in the file "|"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their files)
    #              -> false (if the two queens never intersect in their files)
    @staticmethod
    def same_file(queen1, queen2):
        return queen1.file == queen2.file
    
    # Check for intersections in the rank "—"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their ranks)
    #              -> false (if the two queens never intersect in their ranks)
    @staticmethod
    def same_rank(queen1, queen2):
        return queen1.rank == queen2.rank

    # Increment the file letter (going up alphabetically)
    # Queen -> [file-a, file-b, ..., nth-file]
    def next_files(self):
        f = self.file
        index = self.board.files.index(f)
        files = self.board.files[index+1:]
        return files
    
    # Decrement the file letter (going back alphabetically)
    # Queen -> [file-a, file-b, ..., nth-file]
    def prev_files(self):
        f = self.file
        index = self.board.files.index(f)
        files = self.board.files[:index]
        files.reverse() # WHY REVERSE? Search for "WHY REVERSE" to jump to the code + explanation
        return files
    
    # Increment the rank number
    # Queen -> [rank-1, rank-2, ... rank-n]
    def next_ranks(self):
        r = self.rank
        index = self.board.ranks.index(r)
        ranks = self.board.ranks[index+1:]
        return ranks
    
    # Decrement the rank number
    # Queen -> [rank-1, rank-2, ... rank-n]
    def prev_ranks(self):
        r = self.rank
        index = self.board.ranks.index(r)
        ranks = self.board.ranks[:index]
        ranks.reverse() # WHY REVERSE? Search for "WHY REVERSE" to jump to the code + explanation
        return ranks
    
    # Check for intersections in the rising diagonal "⟋"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their rising diagonals)
    #              -> false (if the two queens never intersect in their rising diagonals)
    @staticmethod
    def same_rising_diagonal(queen1, queen2):
        next_files, prev_files = queen1.next_files(), queen1.prev_files()
        next_ranks, prev_ranks = queen1.next_ranks(), queen1.prev_ranks()
        print(queen1.position, next_files, prev_files, next_ranks, prev_ranks)
        
        # WHY REVERSE: (notes from prev_files and prev_ranks)
        #    Given some queen in the e4 square,
        #    the left-side of the rising diagonal would be:
        #        [b1, c2, d3]
        #    Whereas without reversing,
        #    queen1.prev_files() returns [a, b, c, d]
        #    and queen1.prev_ranks() returns [1, 2, 3]
        #    ------------------------------------------------
        #    Hence, concatenating the strings from the two lists
        #    would yield [a1, b2, c3], which does not match with [b1, c2, d3].
        #    Reversing the two lists to yield [d, c, b, a] and [3, 2, 1]
        #    would yield [d3, c2, b1].
        #    ------------------------------------------------
        #    We only really care if queen2's position is in the list
        #    so we don't care about the order of the list at all
        prev_squares = [
            prev_files[i]+str(prev_ranks[i])
            for i in range(min(len(prev_files), len(prev_ranks)))
        ]
        
        next_squares = [
            next_files[i]+str(next_ranks[i])
            for i in range(min(len(next_files), len(next_ranks)))
        ]
        
        rising_diagonal_squares = prev_squares + next_squares
        return queen2.position in rising_diagonal_squares
    
    # Check for intersections in the falling diagonal "⟍"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their falling diagonals)
    #              -> false (if the two queens never intersect in their falling diagonals)
    @staticmethod
    def same_falling_diagonal(queen1, queen2):
        next_files, prev_files = queen1.next_files(), queen1.prev_files()
        next_ranks, prev_ranks = queen1.next_ranks(), queen1.prev_ranks()
        
        # WHY REVERSE: (notes from prev_files and prev_ranks)
        #    Given some queen in the d4 square,
        #    the left-side of the falling diagonal would be:
        #        [a7, b6, c5]
        #    Whereas without reversing,
        #    queen1.prev_files() returns [a, b, c]
        #    and queen1.next_ranks() returns [5, 6, 7, 8]
        #    ------------------------------------------------
        #    Hence, concatenating the strings from the two lists
        #    would yield [a5, b6, c7], which does not match with [a7, b6, c5].
        #    Reversing the list from queen1.prev_files() to yield [c, b, a] 
        #    and queen1.next_ranks() to still yield [5, 6, 7, 8]
        #    would yield [c5, b6, a7].
        #    ------------------------------------------------
        #    We only really care if queen2's position is in the list
        #    so we don't care about the order of the list at all
        prev_squares = [
            prev_files[i]+str(next_ranks[i])
            for i in range(min(len(prev_files), len(next_ranks)))
        ]
        
        next_squares = [
            next_files[i]+str(prev_ranks[i])
            for i in range(min(len(next_files), len(prev_ranks)))
        ]
        
        rising_diagonal_squares = prev_squares + next_squares
        return queen2.position in rising_diagonal_squares
    
    # Check for intersections in the file, rank, and both diagonals
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in any direction)
    #              -> false (if the two queens never intersect in any direction)
    @staticmethod
    def intersects_with(queen1, queen2):
        if queen1.board != queen2.board:
            print("ERROR: The queens (", queen1.position, ") and (", queen2.position,") are not on the same board.")
            return None
        return Queen.same_position(queen1, queen2) or Queen.same_rank(queen1, queen2) or Queen.same_file(queen1, queen2) or Queen.same_rising_diagonal(queen1, queen2) or Queen.same_falling_diagonal(queen1, queen2)
    
    # Given a list of queens, figure out whether it would be a solution
    # to the n-queens problem
    @staticmethod
    def is_a_solution(queens):
        bools = []
        for q1 in queens:
            for q2 in queens:
                if q1.position != q2.position:
                    bools.append(Queen.intersects_with(q1,q2))
        
        is_a_solution = True
        for b in bools:
            is_a_solution = is_a_solution and not b
            
        return is_a_solution


cb = Chessboard(8)
queens = [Queen('a2', cb), Queen('b4', cb), Queen('c6', cb), Queen('d8', cb), Queen('e3', cb), Queen('f1', cb), Queen('g7', cb), Queen('h5', cb)]
print(Queen.is_a_solution(queens))
print(queens[0].board.ranks)






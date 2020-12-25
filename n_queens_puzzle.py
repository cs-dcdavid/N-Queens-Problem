from itertools import product # to generate all the squares in a chessboard
from random import choice # to randomly generate n-Queens
from random import shuffle # to randomly generate a solution
from math import factorial # to calculate total number of possibilities

nodes_expanded = 0

# The n-Queens puzzle is the problem of placing 
# n-Queens in an n-by-n chessboard
class Chessboard:
    def __init__(self, n):
        self.n = n
        self.files = self.generate_files()
        self.ranks = self.generate_ranks()
        self.squares = self.generate_squares()
    
    # Chessboard -> [file-a, file-b, ... nth-file]
    def generate_files(self):
        files = [
            chr(97 + i)
            for i in range(self.n)
        ]
        return files
    
    # Chessboard -> [rank-1, rank-2, ... rank-n]
    def generate_ranks(self):
        ranks = [
            i + 1
            for i in range(self.n)
        ]
        return ranks
        
    # Chessboard -> [square-a1, square-a2, ..., square-b1, square-b2, ..., nth-square-n]
    def generate_squares(self):
        squares = [
            r[0] + str(r[1])
            for r in product(self.generate_files(), self.generate_ranks())
        ]
        return squares
    
    # Chessboard -> [Queen-1, Queen-2, ..., Queen-n]
    def generate_n_queens(self):
        queens = []
        for _ in range(self.n):
            q = Queen(choice(self.squares), self)
            if q not in queens:
                queens.append(q)
        return queens
    
    # Recursive method where 
    #    - assignments is [Queen-1, Queen2, ..., Queen-n]
    #    - unassigned is [square-a1, square-a2, ..., nth-square-n]
    def generate_solution(self, assignments, unassigned):
        if len(assignments) == self.n:
            return assignments
        # --------------------------------------------------------------------
        # Optimization of up to log_2(n) compared to basic backtracking search
        local_unassigned = unassigned.copy()
        conflicts = []
        for u in local_unassigned:
            q = Queen(u, self)
            for a in assignments:
                if q.intersects_with(a):
                    conflicts.append(u)
        for c in conflicts:
            local_unassigned.remove(c)
        shuffle(local_unassigned)
        # --------------------------------------------------------------------
        for u in local_unassigned:
            global nodes_expanded
            nodes_expanded += 1
            
            local_assignments = assignments.copy()
            local_assignments.append(Queen(u, self))
            if Queen.is_a_partial_solution(local_assignments):
                result = self.generate_solution(local_assignments, local_unassigned)
                if result is not None:
                    return result
        return None
    
    # Chessboard -> int
    def get_length_possibilities(self):
        return (factorial(len(self.squares)) / (factorial(self.n) * factorial(len(self.squares) - self.n)))
    
    # Chessboard -> int
    def get_length_fundamental_solutions(self):
        if self.n > 27:
            print("ERROR: The problem size is too big. The n-Queens puzzle is only solved for up to n=27.")
            return None
        fundamental_solutions = [ 
        1, 0, 0,
        1, 2, 1,
        6, 12, 46,
        92, 341, 1787,
        9233, 45752, 285053,
        1846955, 11977939, 83263591,
        621012754, 4878666808, 39333324973,
        336376244042, 3029242658210, 28439272956934,
        275986683743434, 2789712466510289, 29363495934315694
        ]
        return fundamental_solutions[self.n]
    
    # Chessboard -> int
    def get_length_all_solutions(self):
        if self.n > 27:
            print("ERROR: The problem size is too big. The n-Queens puzzle is only solved for up to n=27.")
            return None
        all_solutions = [
        1, 0, 0,
        2, 10, 4,
        40, 92, 352,
        724, 2680, 14200,
        73712, 365596, 2279184,
        14772512, 95815104, 666090624, 
        4968057848, 39029188884, 314666222712,
        2691008701644, 24233937684440, 227514171973736,
        2207893435808352, 22317699616364044, 234907967154122528
        ]
        return all_solutions[self.n]

# A Chessboard is made up of 
#    columns (called "files" that are letters from a to g) and 
#    row (called "ranks" that are numbers from 1 to 8). Therefore,
#    if a Queen is said to be in "e4",
#    then it is in the "e file" (5th column) and "4th rank" (4th column)
class Queen:
    def __init__(self, position, board):
        self.position = position
        self.board = board
    
    def __str__(self):
        return '{self.position} Queen'.format(self=self)
    
    # Check for two queens in the same position
    # Queen, Queen -> bool
    #              -> true (if the two queens are in the same position)
    #              -> false (if the two queens are in the same position)
    def on_same_position(self, q2):
        return self.position == q2.position
    
    # Check for intersections in the file "|"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their files)
    #              -> false (if the two queens never intersect in their files)
    def on_same_file(self, q2):
        return self.position[0] == q2.position[0]
    
    # Check for intersections in the rank "—"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their ranks)
    #              -> false (if the two queens never intersect in their ranks)
    def on_same_rank(self, q2):
        return self.position[1] == q2.position[1]

    # Increment the file letter (going up alphabetically)
    # Queen -> [file-a, file-b, ..., nth-file]
    def get_next_files(self):
        f = self.position[0]
        index = self.board.files.index(f)
        files = self.board.files[index+1:]
        return files
    
    # Decrement the file letter (going back alphabetically)
    # Queen -> [file-a, file-b, ..., nth-file]
    def get_prev_files(self):
        f = self.position[0]
        index = self.board.files.index(f)
        files = self.board.files[:index]
        files.reverse() # WHY REVERSE? Search for "WHY REVERSE" to jump to the code + explanation
        return files
    
    # Increment the rank number
    # Queen -> [rank-1, rank-2, ... rank-n]
    def get_next_ranks(self):
        r = int(self.position[1])
        index = self.board.ranks.index(r)
        ranks = self.board.ranks[index+1:]
        return ranks
    
    # Decrement the rank number
    # Queen -> [rank-1, rank-2, ... rank-n]
    def get_prev_ranks(self):
        r = int(self.position[1])
        index = self.board.ranks.index(r)
        ranks = self.board.ranks[:index]
        ranks.reverse() # WHY REVERSE? Search for "WHY REVERSE" to jump to the code + explanation
        return ranks
    
    # Check for intersections in the rising diagonal "⟋"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their rising diagonals)
    #              -> false (if the two queens never intersect in their rising diagonals)
    def on_same_rising_diagonal(self, q2):
        next_files, prev_files = self.get_next_files(), self.get_prev_files()
        next_ranks, prev_ranks = self.get_next_ranks(), self.get_prev_ranks()
        
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
        return q2.position in rising_diagonal_squares
    
    # Check for intersections in the falling diagonal "⟍"
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in their falling diagonals)
    #              -> false (if the two queens never intersect in their falling diagonals)
    def on_same_falling_diagonal(self, q2):
        next_files, prev_files = self.get_next_files(), self.get_prev_files()
        next_ranks, prev_ranks = self.get_next_ranks(), self.get_prev_ranks()
        
        # WHY REVERSE: (notes from prev_files and prev_ranks)
        #    Given some queen q1 in the d4 square,
        #    the left-side of the falling diagonal would be:
        #        [a7, b6, c5]
        #    Whereas without reversing,
        #    q1.prev_files() returns [a, b, c]
        #    and q1.next_ranks() returns [5, 6, 7, 8]
        #    ------------------------------------------------
        #    Hence, concatenating the strings from the two lists
        #    would yield [a5, b6, c7], which does not match with [a7, b6, c5].
        #    Reversing the list from q1.prev_files() to yield [c, b, a] 
        #    and q1.next_ranks() to still yield [5, 6, 7, 8]
        #    would yield [c5, b6, a7].
        #    ------------------------------------------------
        #    We only really care if q2's position is in the list
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
        return q2.position in rising_diagonal_squares
    
    # Check for intersections in the file, rank, and both diagonals
    # Queen, Queen -> bool
    #              -> true (if the two queens intersect in any direction)
    #              -> false (if the two queens never intersect in any direction)
    #              -> None + error (if the two queens are not in the same board)
    def intersects_with(self, q2):
        if self.board != q2.board:
            print("ERROR: The queens (", self.position, ") and (", q2.position,") are not on the same board.")
            return None
        return self.on_same_position(q2) or self.on_same_rank(q2) or self.on_same_file(q2) or self.on_same_rising_diagonal(q2) or self.on_same_falling_diagonal(q2)
        
    # Given a list of queens, figure out whether it could be a solution to the n-Queens problem
    # [Queen-1, Queen-2, ..., Queen-n] -> bool
    #                                  -> true (if all queens do not intersect in any direction)
    #                                  -> false (if there are queens that intersect in some direction)
    @staticmethod
    def is_a_partial_solution(queens):
        bools = [
            q1.intersects_with(q2)
            for q1 in queens
            for q2 in queens
            if q1.position != q2.position
        ]
        
        is_a_solution = True
        for b in bools:
            is_a_solution = is_a_solution and not b
            
        return is_a_solution
    
    # Given a list of queens, figure out whether it would be a solution to the n-Queens problem
    # [Queen-1, Queen-2, ..., Queen-n] -> bool
    #                                  -> true (if all queens do not intersect in any direction)
    #                                  -> false (if there are queens that intersect in some direction)
    #                                  -> None + error (if the number of queens do not match the size of the board)
    @staticmethod
    def is_a_solution(queens):
        if queens[0].board.n != len(queens):
            print("ERROR: The number of queens does not match the size of the board.")
            return None

        bools = [
            q1.intersects_with(q2)
            for q1 in queens
            for q2 in queens
            if q1.position != q2.position
        ]
        
        is_a_solution = True
        for b in bools:
            is_a_solution = is_a_solution and not b
            
        return is_a_solution


cb = Chessboard(8)
queens = [Queen('a2', cb), Queen('b4', cb), Queen('c6', cb), Queen('d8', cb), Queen('e3', cb), Queen('f1', cb), Queen('g7', cb), Queen('h5', cb)]
#print(Queen.is_a_solution(queens))

#print(nodes_expanded)
cb2 = Chessboard(8)
print([str(q) for q in cb2.generate_solution([], cb2.squares)])
print(nodes_expanded)
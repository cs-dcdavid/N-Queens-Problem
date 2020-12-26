from itertools import product # to generate all the squares in a chessboard
from random import choice # to randomly generate n-Queens
from random import shuffle # to randomly generate a solution
from math import comb # to calculate total number of possibilities
from os import system, name # to clear the console for output

combinations_found = 0
nodes_expanded = 0

beth_harmon = '''%%%%%%%%%%%%%%%%%%%&&&&&&&&&&&&%%%&(/((%#(&%(%%##(#((%####%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&#%*(&(((#%%%%#%#%%((######%%%%%%%%%%
%%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&@%%##&//*.,,*/##(%#(/%######%%%%%%%%
%%%%%%%%%%%%%%%&&&&&&&&&&&&&&&&&&&&%#(#%/.......,%#%#//######%%%%%%%%%
%%%%%%%%%%%%##&&&&&&&&&&&&&&&&&&&&%#(%&%,........*&&%//####%#%%%%%%%%%
%%%%%%%%%%%%#%&&&&&&&&&&&&%%%&&%%%%%&%%*,,,....../&&#/((#%%%#%%%%%%%%%
%%%%%%%%%%%###%&&&&&&&%&&&&&&&&%%%%#/****,,,/(##(%&%####(##%%#%%%%%%%%
%%%%%%%%%%%%%#%%&&&&&&%&&&&&%&&#@%&#/**/((&%*.&&/%##%%(***###%%%%%%%%%
%%%%%%%%%%%%##%%#&&&&%&(&&%###(///(%/...,*//((,.(##%%%(//#%#%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%&&%(((&%(/**/(#%/......,...,%%#%%%&%%%%%%#%%%%%%%%
%%%%%%%%%%%%%%%%%%%%##&&&&&&#((//#%%/. ..,,,,,,#%%%/(%##%####%%%%%%%%%
%%%%%%%%%%%%%%%%%%%######%&&%%#(((%&#/*.,.,,,,/ %%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%&&#%%%&&&%%%####.*..,,,,*,*..  ,&&&&&&&&&%%%%%%%%%
%%%%%%%%&&&&&&&&&&&&&(((##%&&&&&%#%%###(**,,,./.... @&&&&&&&&&&&&&&%%%
%%%%%%&&&&@&&&#(**,,***/(#//(/(%&%(/**,,,/**,,,,..../***,..*&&&&&&&&%%
%%%%%&&&&&&&%#(/*,.,..,,,,,,,,,/*,,,,**,,,,*****,,,*,,,...,/.(&&&&&&%%
%%%%&&&&&&&%#((*,...,,,,.,,**,,,...........,,***,,,,,,,,/&,.....&&&&&%
%%%&&&&&&&%#((/,,.,%%%%%#(//*///*,,,,,./@&@*,,,**///(#%&&/*,.....&&&&&
%%%&&&&&&%#((/*,..,@&&&&&&&&@%%%%%%#(&%*.,*/#&&&&&&&&&&&%(*,,..../&&&&
%%%&&&&@%#((/*,,,,&&&&&&&&&&&&&&&#%,*/(%#(&&&&&&&&&&&&&&&#/*,,..../&&&
%%&&&&&%##(/**,,,*&&&&&&&&&&&&&&&&&&&&&&&&&&&&@&&&&&&&&&&#(/*,,....%&&
%%&&&&&%#(//**,,,@&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#(/*,,...,#&
%%@&@%%#(/***,,,*&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&@%#(/*,,,,,,*'''

# The n-Queens puzzle is the problem of placing 
# n-Queens in an n-by-n chessboard
class Chessboard:
    def __init__(self, n):
        self.n = n
        self.files = self.generate_files()
        self.ranks = self.generate_ranks()
        self.squares = self.generate_squares()
        self.queens = []
    
    def __str__(self):
        return self.generate_string_chessboard().format(self=self)
    
    # Generate a two-dimensional list that is 
    # ready to be processed into a chessboard
    # Chessboard -> [[nth-square-n, ..., nth-square2, nth-square1], 
    #                ..., 
    #                [square-bn, ..., square-b2, square-b1], 
    #                [square-an, ..., square-a2, square-a1]]
    def generate_two_dimensional_board(self):
        one_dimensional = self.squares.copy()
        one_dimensional.sort(key=lambda x: int(x[1:])) # special sorting key so a10 doesnt go right after a1
        two_dimensional = [one_dimensional[i:i+self.n] for i in range(0, len(one_dimensional), self.n)]
        two_dimensional.reverse()
        return two_dimensional
    
    # Generate a string representation of a chessboard
    # Chessboard -> string
    def generate_string_chessboard(self):
        three_spaces = "   "
        three_single_lines = "───"
        three_double_lines = "═══"

        # Setup for string processing
        two_dimensional = self.generate_two_dimensional_board()
        queen_positions = [
            q.position
            for q in self.queens
        ]

        file_labels, rank_labels = self.files.copy(), self.ranks.copy()
        rank_labels.reverse()

        # Construct horizontal dividers
        horizontal_divider = ""
        for i in range(self.n):
            if i == 0:
                horizontal_divider += "   ╟" + three_single_lines
            else:
                horizontal_divider += "│" + three_single_lines
            if i == self.n-1:
                horizontal_divider += "╢\n"
        
        # Construct top border, bottom border, inner-rows, bottom labels
        top_border, bottom_border, inner_rows, bottom_labels = "", "", "", ""
        # construct each row
        for i in range(self.n): 
            # construct each cell
            for j in range(self.n):
                # if it is the first cell, draw the left double-line border
                if j == 0: 
                    rank_label = str(rank_labels[i])
                    if len(rank_label) == 1:
                        rank_label += " "
                    # if there's a queen, draw a 'Q' for the queen
                    if two_dimensional[i][j] in queen_positions: 
                        inner_rows += " " + rank_label + "║ Q "
                    # if there is no queen, draw spaces
                    else: 
                        inner_rows += " " + rank_label + "║" + three_spaces
                # if it is not the first cell of the row, draw a single-line divider
                else: 
                    # if there's a queen, draw a 'Q' for the queen
                    if two_dimensional[i][j] in queen_positions: 
                        inner_rows += "| Q "
                    # if there is no queen, draw spaces
                    else: 
                        inner_rows += "│" + three_spaces 
                # if it is the last cell in the row, draw the right double-line border
                if j == self.n-1: 
                    inner_rows += "║\n"
                    # draw a horizontal divider except for the last row
                    if i != self.n-1: 
                        inner_rows += horizontal_divider
            # if it is the beginning of the row, draw corners and spacing for file labels
            if i == 0:
                top_border += three_spaces + "╔" + three_double_lines
                bottom_labels += three_spaces + "  " + file_labels[i]
                bottom_border += three_spaces + "╚" + three_double_lines
            # if it is in the middle of the row, draw dividers and other file labels
            else:
                top_border += "╤" + three_double_lines
                bottom_labels += three_spaces + file_labels[i]
                bottom_border += "╧" + three_double_lines
            # draw a closing corner at the end of the row
            if i == self.n-1:
                top_border += "╗\n"
                bottom_border += "╝\n"
        return top_border + inner_rows + bottom_border + bottom_labels

    # Generate the files in a chessboard
    # Chessboard -> [file-a, file-b, ... nth-file]
    def generate_files(self):
        if self.n < 0 or self.n > 52:
            print("ERROR: n =", self.n, "would result to a too big of a board.")
            return []
        files = []
        for i in range(self.n):
            if i < 26:
                files.append(chr(65 + i))
            elif i >= 26:
                files.append(chr(65 + 6 + i))
            else:
                print("ERROR: n =", self.n, "is an invalid size for the n-Queens puzzle.")
        return files
    
    # Generate the ranks in a chessboard
    # Chessboard -> [rank-1, rank-2, ... rank-n]
    def generate_ranks(self):
        ranks = [
            i + 1
            for i in range(self.n)
        ]
        return ranks
    
    # Generate the squares in a chessboard
    # Chessboard -> [square-a1, square-a2, ..., square-b1, square-b2, ..., nth-square-n]
    def generate_squares(self):
        squares = [
            r[0] + str(r[1])
            for r in product(self.generate_files(), self.generate_ranks())
        ]
        return squares
    
    # Randomly place n Queens in an n-by-n chessboard
    # Chessboard -> [Queen-1, Queen-2, ..., Queen-n]
    def generate_n_queens(self):
        queens = []
        for _ in range(self.n):
            q = Queen(choice(self.squares), self)
            if q not in queens:
                queens.append(q)
        return queens
    
    # Recursive method to find a solution where 
    #    - assignments is [Queen1, Queen2, ..., Queen-n]
    #    - unassigned is [square-a1, square-a2, ..., nth-square-n]
    # Chessboard, [], [square-a1, square-a2, ..., nth-square-n] -> [Queen1, Queen2, ..., Queen-n]
    #                                                           -> None (if there are no solutions)
    def generate_solution(self, assignments, unassigned):
        if len(assignments) == self.n:
            assignments.sort(key=lambda x: x.position)
            self.queens = assignments
            return assignments
        # --------------------------------------------------------------------
        # Forward checking to optimize the backtracking search by reducing the number 
        # of nodes explored by O(log_2(n)) compared to basic backtracking search
        local_unassigned = unassigned.copy()
        conflicts = []
        for u in local_unassigned:
            q = Queen(u, self)
            for a in assignments:
                if q.intersects_with(a):
                    conflicts.append(u)
        for c in conflicts:
            local_unassigned.remove(c)
        # --------------------------------------------------------------------
        for u in local_unassigned:       
            global nodes_expanded
            nodes_expanded += 1
            local_assignments = assignments.copy()
            local_assignments.append(Queen(u, self))
            if len(local_assignments) == self.n:
                global combinations_found
                combinations_found += 1
            if Queen.is_a_partial_solution(local_assignments):
                result = self.generate_solution(local_assignments, local_unassigned)
                if result is not None:
                    return result
        return None
    
    # Get number of nodes expanded in the worst-case
    # Chessboard -> int
    def get_max_nodes_expanded(self):
        max = 0
        for i in range(self.n + 1):
            max += comb(len(self.squares), self.n - i)
        return max

    # Get number of possible combinations of 
    # placing n-Queens in an n-by-n chessboard (nCr)
    # Chessboard -> int
    def get_length_possibilities(self):
        return comb(len(self.squares), self.n)
    
    # Get number of solutions excluding rotations and reflections
    # Chessboard -> int
    def get_length_fundamental_solutions(self):
        if self.n > 27:
            print("ERROR: The problem size is too big. The n-Queens puzzle is only solved for up to n = 27.")
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
        return fundamental_solutions[self.n-1]
    
    # Get number of solutions including rotations and reflections
    # Chessboard -> int
    def get_length_all_solutions(self):
        if self.n > 27:
            print("ERROR: The problem size is too big. The n-Queens puzzle is only solved for up to n = 27.")
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
        return all_solutions[self.n-1]

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
        return '{self.position}'.format(self=self)
    
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
        return self.position[1:] == q2.position[1:]

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
        r = int(self.position[1:])
        index = self.board.ranks.index(r)
        ranks = self.board.ranks[index+1:]
        return ranks
    
    # Decrement the rank number
    # Queen -> [rank-1, rank-2, ... rank-n]
    def get_prev_ranks(self):
        r = int(self.position[1:])
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
        #print(self.position, q2.position, self.on_same_position(q2), self.on_same_rank(q2), self.on_same_file(q2), self.on_same_rising_diagonal(q2), self.on_same_falling_diagonal(q2))
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

# Get the solution to the n-Queens puzzle
# + side effect of printing relevant information
# int -> [Queen1, Queen2, ..., Queen-n]
def result(n):
    print('Loading...')
    cb = Chessboard(n)
    local_squares = cb.squares.copy()
    shuffle(local_squares)
    output = cb.generate_solution([], local_squares)
    clear()
    global combinations_found
    global nodes_expanded

    if output is None: # no solutions found
        print('The program was not able to find a solution for n = ', n, '. In fact, the n-Queens puzzle has no solutions for n = 2 and n = 3.', sep='')
    else:
        print('The program found the following solution, having explored ', combinations_found, ' ', cb.n,'-Queen positions.', sep='')

    if n <= 27: # if the n-Queens puzzle is solved at the given 'n'
        print('Out of the theoretical maximum of ', cb.get_length_possibilities(), ' ', cb.n,'-Queen-positions in a ', cb.n,'-by-', cb.n,' chessboard,', sep='')
        print('there are a total of ', cb.get_length_all_solutions(), ' solutions and if rotations and reflections', sep='')
        print('are excluded, there are only ', cb.get_length_fundamental_solutions(), ' fundamental solutions.\n', sep='')
    else:
        print('Unfortunately, the n-Queens puzzle is only solved until n = 27. This means that')
        print('this program can still find a solution for n > 27, but some data such as')
        print('the total number of solutions (fundamental/all) is not known yet.\n')

    print('The program also expanded ', nodes_expanded, ' nodes out of the theoretical maximum of ', cb.get_max_nodes_expanded(), ' nodes.', sep='')
    print('\n', cb, '\n', sep='')
    nodes_expanded = 0
    combinations_found = 0
    return output

# Print relevant information about the program
# None -> None
def output():
    flag = ''
    while(True):
        # User input was not an integer
        if flag == 'ValueError':
            print(beth_harmon, '\n')
            print('ERROR: The input \'', n, '\' is not an integer.', sep='')
            print('Please try again by inputting a number between 1 to 52.\n')
        # There is no solution for the n-Queens problem. (e.g. n=2, n=3)
        elif flag == 'NoSolution':
            print(beth_harmon, '\n')
            print('ERROR: There are no solutions for n = ', n)
            print('Please try again by inputting a number between 1 to 52.\n')
        # The n-Queens problem is too big. n > 52 is possible, but I don't want to program
        # files (columns) that go after capital letters + regular letters (26 + 26 = 52)
        elif flag == 'TooLong':
            print(beth_harmon, '\n')
            print('ERROR: The', n, '-Queens puzzle would take too long.')
            print('Please try again by inputting a number between 1 to 52.\n')
        # It might take too long. The user can decide to go through it
        elif flag == 'AreYouSure?':
            yes = ['y', 'Y', 'yes', 'Yes', 'yEs', 'yeS', 'YEs', 'YeS', 'yES', 'YES']
            print(beth_harmon, '\n')
            print('NOTE: Starting at n = 10, the program slows down because it has to explore up to 17 trillion possibilities.')
            print('Are you sure you want to proceed (y/n)?: ', end='')
            yes_or_no = input()
            if yes_or_no in yes:
                try: 
                    n = int(n)
                    print('If the program takes too long, Ctrl+C (Windows) or Cmd+. (Mac) to force exit.')
                    result(n)
                    flag = ''
                except ValueError:
                    flag = 'ValueError'
                    continue
            else:
                clear()
        else:
            print('This is a Python program by DC David involving the n-Queens puzzle,')
            print('which is the problem of placing \'n\' non-attacking Queens in an n-by-n chessboard.\n')
            
        print('Type \'exit\' at any time to stop the program.')
        print('What integer \'n\' would you like to solve next? (type a number from 1 to 52): ', end='')
        n = input()
        clear()
        if n == 'exit':
            break
        try: 
            n = int(n)
            # The n-Queens problem is too big. n > 52 is possible, but I don't want to program
            # files (columns) that go after capital letters + regular letters (26 + 26 = 52)
            if n > 52:
                flag = "TooBig"
                continue
            # It might take too long. Kinduva soft error, the user can decide to go through it
            elif n >= 10:
                flag = "AreYouSure?"
                continue
            result(n)
            flag = ''
        # User input was not an integer
        except ValueError:
            flag = 'ValueError'
            continue

# Clear the console
# None -> None
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name2 is 'posix') 
    else: 
        _ = system('clear') 

if __name__ == "__main__":
    output()

# TODO: Optimize backtracking search further
def find_next_empty(puzzle):
    # finds next empty row, col - as we are representing our empty spaces with -1,
    # we can just look for the next row, col that is -1
    # if board is completely filled (no empty spaces) return (None, None)

    # as we are doing a 9 x 9 sudoku board, our row, col locations/indexes will be in range 0-8
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None # if board full

def is_valid(guess, puzzle, row, col):
    # checks if the guess is valid
    # returns True if valid, False if not

    # sudoku rules for checking if valid:
    # is the number in the current row
    # -"- column
    # -"- 3x3 square

    # row checker
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # column chekcer
    # col_vals = []
    # for i in range(9):
        # col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)] # this is list comprehension of the above code
    if guess in col_vals:
        return False

    # 3 x 3 square checker
    # this is difficult but we can find where the 3 x 3 starts 
    # then iterate through it
    row_start = (row // 3) * 3 # 1//3 = 0(th row)   5//3 = 1    8//3 = 2
    col_start = (col // 3) * 3

    for r in range(row_start, (row_start + 3)):
        for c in range(col_start, (col_start + 3)):
            if puzzle[r][c] == guess:
                return False

    # if we pass all these checks, input is valid
    return True

def solve_sudoku(puzzle):
    # solve sudoku using a backtracking technique
    # similar to Minesweeper, our puzzle is a list of lists, where each inner list is a row
    # return whether a solution exists
    # mutate the puzzle to be the solution - lists are mutable

    # 1. a) choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle) # helper function

    #  b) if no spaces left, puzzle should be complete as we have only allowed valid inputs
    if row == None:
        return True

    # 2. if there is an empty spot, find the right number between 1 - 9
    for guess in range(1, 10): # this is 1, 2, 3, .... 9
        # 3. check if guess is valid by using another helper function
        if is_valid(guess, puzzle, row, col):
            # 3. a) if valid guess, mutate our array
            puzzle[row][col] = guess
            # now recurse these steps
            # 4. recursively call our function
            if solve_sudoku(puzzle):
                return True

            # 5. if not valid OR our guess doesn't solve the entire puzzle, then we need to
            # back track and try a new number
        puzzle[row][col] = -1 # reset the value at our guess location

    # if we go through the for loop above (which covers every number in every location),
    # and we still haven't solved the sudoku, then the puzzle is UNSOLVABLE
    return False
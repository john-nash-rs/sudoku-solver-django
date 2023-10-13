from django.shortcuts import render
from .forms import SudokuForm

def is_valid_move(board, row, col, num):
    # Check if 'num' is not in the current row or column
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    
    # Check if 'num' is not in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False

    return True

def solve_sudoku(request):
    def solve_sudoku(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid_move(board, row, col, num):
                            board[row][col] = num

                            if solve_sudoku(board):
                                return True
                            
                            board[row][col] = 0

                    return False
        return True

    if request.method == 'POST':
        # Create an empty list to store Sudoku puzzle values
        puzzle_values = []

        # Create a new set of sudoku fields for each request
        sudoku_fields = [SudokuForm(prefix=str(i)) for i in range(81)]

        # Loop through the POST data and extract 'puzzle' values
        for i in range(81):
            field_name = f"{i}-puzzle"
            field_value = request.POST.get(field_name, '')
            if field_value == '':
                field_value = '0'

            puzzle_values.append(field_value)

        # Create a 2D board from puzzle_values
        board = [[int(puzzle_values[i * 9 + j]) for j in range(9)] for i in range(9)]

        # Call the solve_sudoku function to solve the puzzle
        print (board)
        print ("board")
        solved_sudoku = solve_sudoku(board)
        print (board)

        if solved_sudoku:
            # Create a list of solved Sudoku values
            solved_sudoku_values = [str(board[i][j]) for i in range(9) for j in range(9)]

            # Update the form fields with the solved puzzle
            for i in range(81):
                sudoku_fields[80 - i].data = solved_sudoku_values[i]

            return render(request, 'solver/solve_sudoku.html', {'solved_sudoku_values': sudoku_fields})

    else:
        # Create a new set of sudoku fields for each request
        sudoku_fields = [SudokuForm(prefix=str(i)) for i in range(81)]

    return render(request, 'solver/solve_sudoku.html', {'sudoku_fields': sudoku_fields})

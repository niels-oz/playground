from random import randint


def display_board(b):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', b[0], '  |  ', b[1], '  |  ', b[2], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', b[3], '  |  ', b[4], '  |  ', b[5], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ', b[6], '  |  ', b[7], '  |  ', b[8], '  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')

    return None


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = input('Enter your move: ')
    try:
        move = int(move)
    except ValueError:
        print('Error: Please enter a number.')
        enter_move(board)
    if move > 0 and move < 10:
        if board[move - 1] == 'X' or board[move - 1] == 'O':
            print('Error: Please pick an empty field.')
            enter_move(board)
        board[move - 1] = 'O'
        display_board(board)
    else:
        print('Error: Please enter a valid field.')
        enter_move(board)


def make_list_of_free_fields(board):
    # The function browses the board and returns a list of all the empty fields
    empty_fields = []
    for field in board:
        if field != 'O' and field != 'X':
            empty_fields.append(field)
    return empty_fields


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game

    winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for line in winning_lines:
        if str(board[line[0]]) + str(board[line[1]]) + str(board[line[2]]) == sign * 3:
            return True
    return False


def draw_move(board):
    # The function draws the computer's move and updates the board.
    options = make_list_of_free_fields(board)
    if options:
        computer_move = randint(0, len(options) - 1)
        board[options[computer_move] - 1] = 'X'
        display_board(board)


board = [1, 2, 3, 4, 'X', 6, 7, 8, 9]

display_board(board)

while make_list_of_free_fields(board):
    enter_move(board)
    if victory_for(board, 'O'):
        print('Yaaaaaaa. Congrats you won.')
        break
    draw_move(board)
    if victory_for(board, 'X'):
        print('Muhahahaha. AI in your face. You lost.')
        break
else:
    print('No more empty fields. Game ends as a tie.')

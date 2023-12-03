"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = sum([i.count(X) for i in board])
    count_O = sum([i.count(O) for i in board])
    if count_X == 0 and count_O == 0:
        return X
    elif count_X > count_O:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return set(
        [
            (i, j)
            for i, row in enumerate(board)
            for j, column in enumerate(row)
            if EMPTY == column
        ]
    )


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = copy.deepcopy(board)
    if not action:
        raise Exception("Not a valid action")
    y, x = action
    if player(new_board) == X:
        new_board[y][x] = X
    else:
        new_board[y][x] = O
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_list = winning_coordinates(3)

    if x_win(board, winning_list):
        return X
    if o_win(board, winning_list):
        return O
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X or winner(board) == O:
        return True

    if not actions(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)
    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        if terminal(board):
            return utility(board)
        v = -float("inf")
        best_action = None

        for action in actions(board):
            current_v = minimax(result(board, action))
            if type(current_v) is not tuple:
                if current_v:
                    if current_v > v:
                        v = current_v
                        best_action = action
                        return best_action

        return v
    else:
        if terminal(board):
            return utility(board)
        v = float("inf")
        best_action = None

        for action in actions(board):
            current_v = minimax(result(board, action))
            if type(current_v) is not tuple:
                if current_v:
                    if current_v < v:
                        v = current_v
                        best_action = action
                        return best_action

        return v


def winning_coordinates(board_size):
    winning_coordinates = []

    for i in range(board_size):
        winning_coordinates.append([(i, j) for j in range(board_size)])

    for j in range(board_size):
        winning_coordinates.append([(i, j) for i in range(board_size)])

    diagonal1 = [(i, i) for i in range(board_size)]
    diagonal2 = [(i, board_size - 1 - i) for i in range(board_size)]
    winning_coordinates.append(diagonal1)
    winning_coordinates.append(diagonal2)
    return winning_coordinates


def diagonal_1(board_list):
    diagonal_1_list = []
    for index, value in enumerate(board_list):
        diagonal_1_list.append(value[index])
    return diagonal_1_list


def diagonal_2(diagonal_2_list):
    diagonal_list = []
    diagonal_list.append(diagonal_2_list[0][2])
    diagonal_list.append(diagonal_2_list[1][1])
    diagonal_list.append(diagonal_2_list[2][0])
    return diagonal_list


def x_win(board, winning_list):
    x_cordinates = []
    new_list = []
    for i, row in enumerate(board):
        for j, colum in enumerate(row):
            if colum == X:
                new_list.append((i, j))
            else:
                new_list.append((None, None))
        x_cordinates.append(new_list)
        new_list = []

    column_2 = [i[2] for i in x_cordinates]
    column_1 = [i[1] for i in x_cordinates]
    column_0 = [i[0] for i in x_cordinates]
    for i in x_cordinates:
        for j in winning_list:
            if i == j:
                return X

    if diagonal_1(x_cordinates) in winning_list:
        return X
    if diagonal_2(x_cordinates) in winning_list:
        return X
    if column_0 in winning_list:
        return X
    if column_1 in winning_list:
        return X
    if column_2 in winning_list:
        return X
    return None


def o_win(board, winning_list):
    o_cordinates = []
    new_list = []
    for i, row in enumerate(board):
        for j, colum in enumerate(row):
            if colum == O:
                new_list.append((i, j))
            else:
                new_list.append((None, None))
        o_cordinates.append(new_list)
        new_list = []

    column_2 = [i[2] for i in o_cordinates]
    column_1 = [i[1] for i in o_cordinates]
    column_0 = [i[0] for i in o_cordinates]
    for i in o_cordinates:
        for j in winning_list:
            if i == j:
                return O

    if diagonal_1(o_cordinates) in winning_list:
        return O
    if diagonal_2(o_cordinates) in winning_list:
        return O
    if column_0 in winning_list:
        return O
    if column_1 in winning_list:
        return O
    if column_2 in winning_list:
        return O
    return None


if __name__ == "__main__":
    print(terminal(initial_state()))

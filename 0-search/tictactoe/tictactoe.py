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
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    #raise NotImplementedError

    player_x = 0
    player_o = 0

    player_x = len([col for row in board for col in row if col == X])
    player_o = sum([row.count(O) for row in board])    

    return X if player_x <= player_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError
    action = {(row,col) for row in range(3) for col in range(3) if board[row][col] == EMPTY}

    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #raise NotImplementedError

    #if action not in actions(board):
     #   raise ValueError

    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = player(new_board)

    return new_board
    #board[action[0]][action[1]] = player(board)

    #return board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError
    winning_combination = [[row[i] for row in board] for i in range(3)] + [board[0], board[1], board[2]] + 
    [[board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]]

    for row in winning_combination:
        move = row[0]

        if move is not EMPTY and row.count(row[0]) == 3:
            return move

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError

    return True if winner(board) is not None or not actions(board) else False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError
    win = winner(board)

    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.RR
    """
    #raise NotImplementedError

    if terminal(board):
        return None

    # Optimization by hardcoding the first move
    if board == initial_state():
        return 0, 1

    current_player = player(board)
    optimal_value = float("-inf") if current_player == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), optimal_value)

        if current_player == X:
            new_value = max(optimal_value, new_value)

        if current_player == O:
            new_value = min(optimal_value, new_value) 


        if new_value != optimal_value:
            optimal_value = new_value
            best_action = action

    return best_action


def minimax_value(board, optimal_value):
    """
    Returns the best value for each recursive minimax iteration.
    Optimized using Alpha-Beta Pruning: If the new value found is better
    than the best value then return without checking the others.
    """
    if terminal(board):
        return utility(board)

    current_player = player(board)
    value = float("-inf") if current_player == X else float("inf")

    for action in actions(board):
        new_value = minimax_value(result(board, action), value)

        if current_player == X:
            if new_value > optimal_value:
                return new_value
            value = max(value, new_value)

        if current_player == O:
            if new_value < optimal_value:
                return new_value
            value = min(value, new_value)

    return value


import re


# Function to read the contents of the input file
# The whole project is designed to read multiple lines of input board positions and also write their respective output
def read_input(text_file):
    file = open(text_file, 'r')
    input_board_positions = file.readlines()
    for i in range(len(input_board_positions)):
        input_board_positions[i] = re.findall('[WBx]', input_board_positions[i])
    file.close()
    return input_board_positions


# Function to write the output to user mentioned file
# Output positions for each input position in file is written
def write_output(output_board_positions, text_file):
    file = open(text_file, 'w')
    for board in output_board_positions:
        file.write(board + '\n')
    file.close()


# Function to generate a list of all possible positions for the opening game
# There can't be more than 8 coins for any player, the function would return an empty list in that case
def generate_add(board):
    opening_list = []
    count_empty = board.count('x')
    count_white = board.count('W')
    if count_empty == 2 or count_white == 8:
        return opening_list
    for position in range(len(board)):
        if board[position] == 'x':
            board_copy = board.copy()
            board_copy[position] = 'W'
            if close_mill(position, board_copy):
                generate_remove(board_copy, opening_list)
            else:
                opening_list.append(board_copy)
    return opening_list


# Function to generate all possible positions when Black is Maximizer
def generate_add_black(board):
    new_board = inverse_board(board)
    opening_list_black = generate_add(new_board)
    for i in range(len(opening_list_black)):
        opening_list_black[i] = inverse_board(opening_list_black[i])
    return opening_list_black


# Function to decide the midgame-endgame move
# If count is 3 hop, if count is more than 3 move,
# else return an empty list saying that it's a leaf node (no more moves possible)
def generate_midgame_endgame(board):
    count_white = board.count('W')
    if count_white == 3:
        game_list = generate_hop(board)
    elif count_white > 3:
        game_list = generate_move(board)
    else:
        game_list = []
    return game_list


# Function to decide the midgame-endgame move when Black is Maximizer
def generate_midgame_endgame_black(board):
    new_board = inverse_board(board)
    game_list_black = generate_midgame_endgame(new_board)
    for i in range(len(game_list_black)):
        game_list_black[i] = inverse_board(game_list_black[i])
    return game_list_black


# Function generate all possible hop positions when the player is left with only 3 coins
def generate_hop(board):
    hopping_list = []
    for position_1 in range(len(board)):
        if board[position_1] == 'W':
            for position_2 in range(len(board)):
                if board[position_2] == 'x':
                    board_copy = board.copy()
                    board_copy[position_1] = 'x'
                    board_copy[position_2] = 'W'
                    if close_mill(position_2, board_copy):
                        generate_remove(board_copy, hopping_list)
                    else:
                        hopping_list.append(board_copy)
    return hopping_list


# Function to determine the list of neighbours for each position, used in generate_move()
def list_of_neighbours(position):
    match position:
        case 0:
            return [1, 2, 15]
        case 1:
            return [0, 3, 8]
        case 2:
            return [0, 3, 4, 12]
        case 3:
            return [1, 2, 5, 7]
        case 4:
            return [2, 5, 9]
        case 5:
            return [3, 4, 6]
        case 6:
            return [5, 7, 11]
        case 7:
            return [3, 6, 8, 14]
        case 8:
            return [1, 7, 17]
        case 9:
            return [4, 10, 12]
        case 10:
            return [9, 11, 13]
        case 11:
            return [6, 10, 14]
        case 12:
            return [2, 9, 13, 15]
        case 13:
            return [10, 12, 14, 16]
        case 14:
            return [7, 11, 13, 17]
        case 15:
            return [0, 12, 16]
        case 16:
            return [13, 15, 17]
        case 17:
            return [8, 14, 16]


# Function to generate the list of all possible moves when the player is in mid-game scenario
def generate_move(board):
    move_list = []
    for position in range(len(board)):
        if board[position] == 'W':
            neighbours = list_of_neighbours(position)
            for neighbour in neighbours:
                if board[neighbour] == 'x':
                    board_copy = board.copy()
                    board_copy[position] = 'x'
                    board_copy[neighbour] = 'W'
                    if close_mill(neighbour, board_copy):
                        generate_remove(board_copy, move_list)
                    else:
                        move_list.append(board_copy)
    return move_list


# Function to remove a Minimizer's coin, used when Maximizer closes a mill
def generate_remove(board, check_list):
    list_size = len(check_list)
    for position in range(len(board)):
        if board[position] == 'B':
            if not close_mill(position, board):
                board_copy = board.copy()
                board_copy[position] = 'x'
                check_list.append(board_copy)
    if len(check_list) == list_size:
        check_list.append(board)


# Function to determine is the Maximizer is closing a mill, used in add, move and hop situations
def close_mill(position, board):
    P = board[position]
    match position:
        case 0:
            if board[2] == P and board[4] == P:
                return True
            else:
                return False
        case 1:
            if (board[3] == P and board[5] == P) or (board[8] == P and board[17] == P):
                return True
            else:
                return False
        case 2:
            if board[0] == P and board[4] == P:
                return True
            else:
                return False
        case 3:
            if (board[1] == P and board[5] == P) or (board[7] == P and board[14] == P):
                return True
            else:
                return False
        case 4:
            if board[0] == P and board[2] == P:
                return True
            else:
                return False
        case 5:
            if (board[1] == P and board[3] == P) or (board[6] == P and board[11] == P):
                return True
            else:
                return False
        case 6:
            if (board[5] == P and board[11] == P) or (board[7] == P and board[8] == P):
                return True
            else:
                return False
        case 7:
            if (board[6] == P and board[8] == P) or (board[3] == P and board[14] == P):
                return True
            else:
                return False
        case 8:
            if (board[6] == P and board[7] == P) or (board[1] == P and board[17] == P):
                return True
            else:
                return False
        case 9:
            if (board[10] == P and board[11] == P) or (board[12] == P and board[15] == P):
                return True
            else:
                return False
        case 10:
            if (board[9] == P and board[11] == P) or (board[13] == P and board[16] == P):
                return True
            else:
                return False
        case 11:
            if (board[9] == P and board[10] == P) or (board[5] == P and board[6] == P) or (board[14] == P and board[17] == P):
                return True
            else:
                return False
        case 12:
            if (board[9] == P and board[15] == P) or (board[13] == P and board[14] == P):
                return True
            else:
                return False
        case 13:
            if (board[10] == P and board[16] == P) or (board[12] == P and board[14] == P):
                return True
            else:
                return False
        case 14:
            if (board[12] == P and board[13] == P) or (board[11] == P and board[17] == P) or (board[3] == P and board[7] == P):
                return True
            else:
                return False
        case 15:
            if (board[9] == P and board[12] == P) or (board[16] == P and board[17] == P):
                return True
            else:
                return False
        case 16:
            if (board[10] == P and board[13] == P) or (board[15] == P and board[17] == P):
                return True
            else:
                return False
        case 17:
            if (board[1] == P and board[8] == P) or (board[11] == P and board[14] == P) or (board[15] == P and board[16] == P):
                return True
            else:
                return False


# Function to inverse the coins in the board when black is the Maximizer
def inverse_board(board):
    board_copy = board.copy()
    for i in range(len(board)):
        if board[i] == 'W':
            board_copy[i] = 'B'
        elif board[i] == 'B':
            board_copy[i] = 'W'
    return board_copy


# Function to find the static estimate for leaf nodes, original function provided by professor
def static_estimation(board, phase):
    count_white = board.count('W')
    count_black = board.count('B')

    if phase == 'opening':
        return count_white - count_black

    else:
        game_list = generate_midgame_endgame_black(board)
        black_moves = len(game_list)

        if count_black <= 2:
            return 10000
        elif count_white <= 2:
            return -10000
        elif black_moves == 0:
            return 10000
        else:
            return 1000 * (count_white - count_black) - black_moves


# Function to determine static estimation of leaf nodes when black is the Maximizer
def static_estimation_black(board, phase):
    new_board = inverse_board(board)
    return static_estimation(new_board, phase)


# Function to count the number of possible mills 2 moves ahead of current move
# We are counting the possible number of mills that the player can make in future with the current position of board
def mill_count(board):
    mills = 0
    for position in range(len(board)):
        if board[position] == 'W':
            mills += close_mill_improved(position, board)
    return mills


# Functions to count all possible mills that a player can make in next move
def close_mill_improved(position, board):
    P = board[position]
    count = 0
    match position:
        case 0:
            if (board[2] == P or board[2] == 'x') and (board[4] == P or board[4] == 'x'):
                count += 1
        case 1:
            if (board[3] == P or board[3] == 'x') and (board[5] == P or board[5] == 'x'):
                count += 1
            if (board[8] == P or board[8] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
        case 2:
            if (board[0] == P or board[0] == 'x') and (board[4] == P or board[4] == 'x'):
                count += 1
        case 3:
            if (board[1] == P or board[1] == 'x') and (board[5] == P or board[5] == 'x'):
                count += 1
            if (board[7] == P or board[7] == 'x') and (board[14] == P or board[14] == 'x'):
                count += 1
        case 4:
            if (board[0] == P or board[0] == 'x') and (board[2] == P or board[2] == 'x'):
                count += 1
        case 5:
            if (board[1] == P or board[1] == 'x') and (board[3] == P or board[3] == 'x'):
                count += 1
            if (board[6] == P or board[6] == 'x') and (board[11] == P or board[11] == 'x'):
                count += 1
        case 6:
            if (board[5] == P or board[5] == 'x') and (board[11] == P or board[11] == 'x'):
                count += 1
            if (board[7] == P or board[7] == 'x') and (board[8] == P or board[8] == 'x'):
                count += 1
        case 7:
            if (board[6] == P or board[6] == 'x') and (board[8] == P or board[8] == 'x'):
                count += 1
            if (board[3] == P or board[3] == 'x') and (board[14] == P or board[14] == 'x'):
                count += 1
        case 8:
            if (board[6] == P or board[6] == 'x') and (board[7] == P or board[7] == 'x'):
                count += 1
            if (board[1] == P or board[1] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
        case 9:
            if (board[10] == P or board[10] == 'x') and (board[11] == P or board[11] == 'x'):
                count += 1
            if (board[12] == P or board[12] == 'x') and (board[15] == P or board[15] == 'x'):
                count += 1
        case 10:
            if (board[9] == P or board[9] == 'x') and (board[11] == P or board[11] == 'x'):
                count += 1
            if (board[13] == P or board[13] == 'x') and (board[16] == P or board[16] == 'x'):
                count += 1
        case 11:
            if (board[9] == P or board[9] == 'x') and (board[10] == P or board[10] == 'x'):
                count += 1
            if (board[6] == P or board[6] == 'x') and (board[5] == P or board[5] == 'x'):
                count += 1
            if (board[14] == P or board[14] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
        case 12:
            if (board[9] == P or board[9] == 'x') and (board[15] == P or board[15] == 'x'):
                count += 1
            if (board[13] == P or board[13] == 'x') and (board[14] == P or board[14] == 'x'):
                count += 1
        case 13:
            if (board[10] == P or board[10] == 'x') and (board[16] == P or board[16] == 'x'):
                count += 1
            if (board[12] == P or board[12] == 'x') and (board[14] == P or board[14] == 'x'):
                count += 1
        case 14:
            if (board[12] == P or board[12] == 'x') and (board[13] == P or board[13] == 'x'):
                count += 1
            if (board[11] == P or board[11] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
            if (board[3] == P or board[3] == 'x') and (board[7] == P or board[7] == 'x'):
                count += 1
        case 15:
            if (board[9] == P or board[9] == 'x') and (board[12] == P or board[12] == 'x'):
                count += 1
            if (board[16] == P or board[16] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
        case 16:
            if (board[10] == P or board[10] == 'x') and (board[13] == P or board[13] == 'x'):
                count += 1
            if (board[15] == P or board[15] == 'x') and (board[17] == P or board[17] == 'x'):
                count += 1
        case 17:
            if (board[1] == P or board[1] == 'x') and (board[8] == P or board[8] == 'x'):
                count += 1
            if (board[11] == P or board[11] == 'x') and (board[14] == P or board[14] == 'x'):
                count += 1
            if (board[16] == P or board[16] == 'x') and (board[15] == P or board[15] == 'x'):
                count += 1
    return count


# Function to find the static estimation for leaf nodes
# This is the improved version where we are modifying 2 things.
# First, predicting the number of mills the player can make in the future,
# This way future mills are given higher weights,
# and positions like f5, which has three possible mill positions will have more weights too.
# Second, since the game tree that we are generating would not be a complete tree,
# leaf nodes can be present in any depth, and they should not carry the same weights.
# Closer the leaf node from the root, higher should be its weight as the Maximizer can win sooner if it reaches it.
# Hence, the depth at which the leaf node occurs needs to considered, lower the depth higher the weight
def static_estimation_improved(board, phase, depth):
    count_white = board.count('W')
    count_black = board.count('B')

    count_mills = mill_count(board)

    if phase == 'opening':
        return count_white - count_black - depth + count_mills

    else:
        game_list = generate_midgame_endgame_black(board)
        black_moves = len(game_list)

        if count_black <= 2:
            return 10000
        elif count_white <= 2:
            return -10000
        elif black_moves == 0:
            return 10000
        else:
            return 1000 * (count_white - count_black) - depth + count_mills - black_moves


# Class to hold the number of nodes visited, their static estimate value, and the board position
class OutputC(object):
    positions_count = 0
    value = 0
    final_position = []

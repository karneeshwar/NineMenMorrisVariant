import ALPHABETA

# Part II: ALPHA-BETA. Program: ABOpening.py
# It gets user input for input file name, output file name, and depth for the game
# It uses AlphaBeta pruning algorithm to compute the best possible opening move for the Maximizer (White)
# It can read and write multiple lines of board positions, personally made for my own bulk testing purposes
if __name__ == '__main__':
    user_input = input("Please enter the details in the following format,\ninput_file_name.txt output_file_name.txt depth: ")
    input_list = user_input.split(' ')
    input_positions = ALPHABETA.MorrisVariant.read_input(input_list[0])
    game_phase = 'opening'
    print()

    write_position = []
    for position in input_positions:
        result = ALPHABETA.alphabeta('W', int(input_list[2]), position, game_phase, 0, float('-inf'), float('inf'))
        print('INPUT:')
        print('Board Position: ', ''.join(position))
        print('OUTPUT:')
        print('Board Position: ', ''.join(result.final_position))
        print('Positions evaluated by static estimation: ', result.positions_count)
        print('AlphaBeta estimate: ', result.value, '\n')
        write_position.append(''.join(result.final_position))

    ALPHABETA.MorrisVariant.write_output(write_position, input_list[1])
    print('Board Position written to file', input_list[1])

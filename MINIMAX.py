import MorrisVariant


def minimax(player, d, board, phase, counter):
    current = MorrisVariant.OutputC()
    # If leaf node do static estimation else continue
    if counter == d:
        current.value = MorrisVariant.static_estimation(board, phase)
        current.positions_count += 1
        current.final_position = board
    else:
        # If maximizer set current value to -infinity else set current value to +infinity
        if player == 'W':
            current.value = float('-inf')
            # If opening game, get all possible opening positions else get all game positions
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame(board)
        else:
            current.value = float('inf')
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add_black(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame_black(board)

        # If the generated positions is null/empty, then its leaf node do static estimation, else continue
        if not board_positions:
            current.value = MorrisVariant.static_estimation(board, phase)
            current.positions_count += 1
            current.final_position = board

        # for positions in board_positions:
        #     if player == 'W':
        #         previous = minimax('B', d, positions, phase, counter+1)
        #         current.value = max(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count
        #     else:
        #         previous = minimax('W', d, positions, phase, counter+1)
        #         current.value = min(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count

        else:
            # for each positions in generated list perform next move
            for positions in board_positions:
                # If maximizer recursively call the algorithm to perform minimizer move
                if player == 'W':
                    previous = minimax('B', d, positions, phase, counter + 1)
                    # check if previous value is more than current value, then set current value as previous value
                    if previous.value > current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                # else recursively call the algorithm to perform maximizer move
                else:
                    # check if previous value is less than current value, then set current value as previous value
                    previous = minimax('W', d, positions, phase, counter + 1)
                    if previous.value < current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count

    # return the current class data
    return current


def minimax_black(player, d, board, phase, counter):
    current = MorrisVariant.OutputC()
    # If leaf node do static estimation else continue
    if counter == d:
        current.value = MorrisVariant.static_estimation_black(board, phase)
        current.positions_count += 1
        current.final_position = board
    else:
        # If maximizer set current value to -infinity else set current value to +infinity
        if player == 'B':
            current.value = float('-inf')
            # If opening game, get all possible opening positions else get all game positions
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add_black(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame_black(board)
        else:
            current.value = float('inf')
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame(board)

        # If the generated positions is null/empty, then its leaf node do static estimation, else continue
        if not board_positions:
            current.value = MorrisVariant.static_estimation_black(board, phase)
            current.positions_count += 1
            current.final_position = board

        # for positions in board_positions:
        #     if player == 'B':
        #         previous = minimax_black('W', d, positions, phase, counter+1)
        #         current.value = max(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count
        #     else:
        #         previous = minimax_black('B', d, positions, phase, counter+1)
        #         current.value = min(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count

        else:
            # for each positions in generated list perform next move
            for positions in board_positions:
                # If maximizer recursively call the algorithm to perform minimizer move
                if player == 'B':
                    previous = minimax_black('W', d, positions, phase, counter + 1)
                    # check if previous value is more than current value, then set current value as previous value
                    if previous.value > current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                # else recursively call the algorithm to perform maximizer move
                else:
                    previous = minimax_black('B', d, positions, phase, counter + 1)
                    # check if previous value is less than current value, then set current value as previous value
                    if previous.value < current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count

    # return the current class data
    return current


def minimax_improved(player, d, board, phase, counter):
    current = MorrisVariant.OutputC()
    if counter == d:
        current.value = MorrisVariant.static_estimation_improved(board, phase, counter)
        current.positions_count += 1
        current.final_position = board
    else:
        # If maximizer set current value to -infinity else set current value to +infinity
        if player == 'W':
            current.value = float('-inf')
            # If opening game, get all possible opening positions else get all game positions
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame(board)
        else:
            current.value = float('inf')
            if phase == 'opening':
                board_positions = MorrisVariant.generate_add_black(board)
            else:
                board_positions = MorrisVariant.generate_midgame_endgame_black(board)

        # If the generated positions is null/empty, then its leaf node do static estimation, else continue
        if not board_positions:
            current.value = MorrisVariant.static_estimation_improved(board, phase, counter)
            current.positions_count += 1
            current.final_position = board

        # for positions in board_positions:
        #     if player == 'W':
        #         previous = minimax_improved('B', d, positions, phase, counter+1)
        #         current.value = max(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count
        #     else:
        #         previous = minimax_improved('W', d, positions, phase, counter+1)
        #         current.value = min(previous.value, current.value)
        #         current.final_position = positions
        #         current.positions_count += previous.positions_count

        else:
            # for each positions in generated list perform next move
            for positions in board_positions:
                # If maximizer recursively call the algorithm to perform minimizer move
                if player == 'W':
                    previous = minimax_improved('B', d, positions, phase, counter + 1)
                    # check if previous value is more than current value, then set current value as previous value
                    if previous.value > current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                # else recursively call the algorithm to perform maximizer move
                else:
                    previous = minimax_improved('W', d, positions, phase, counter + 1)
                    # check if previous value is less than current value, then set current value as previous value
                    if previous.value < current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count

    # return the current class data
    return current

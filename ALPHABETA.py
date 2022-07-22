import MorrisVariant


def alphabeta(player, d, board, phase, counter, a, b):
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

        else:
            # for each positions in generated list perform next move
            for positions in board_positions:
                # If maximizer recursively call the algorithm to perform minimizer move
                if player == 'W':
                    previous = alphabeta('B', d, positions, phase, counter + 1, a, b)
                    # check if previous value is more than current value, then set current value as previous value
                    if previous.value > current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                    # set alpha to max value
                    a = max(a, current.value, previous.value)
                # else recursively call the algorithm to perform maximizer move
                else:
                    previous = alphabeta('W', d, positions, phase, counter + 1, a, b)
                    # check if previous value is less than current value, then set current value as previous value
                    if previous.value < current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                    # set beta to max value
                    b = min(b, current.value, previous.value)

                # If alpha is greater or equal to beta, we found a contradiction break and skip rest of the tree
                if a >= b:
                    break

    # return the current class data
    return current


def alphabeta_improved(player, d, board, phase, counter, a, b):
    current = MorrisVariant.OutputC()
    # If leaf node do static estimation else continue
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

        else:
            # for each positions in generated list perform next move
            for positions in board_positions:
                # If maximizer recursively call the algorithm to perform minimizer move
                if player == 'W':
                    previous = alphabeta_improved('B', d, positions, phase, counter + 1, a, b)
                    # check if previous value is more than current value, then set current value as previous value
                    if previous.value > current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                    # set alpha to max value
                    a = max(a, current.value, previous.value)
                # else recursively call the algorithm to perform maximizer move
                else:
                    previous = alphabeta_improved('W', d, positions, phase, counter + 1, a, b)
                    # check if previous value is less than current value, then set current value as previous value
                    if previous.value < current.value:
                        current.value = previous.value
                        current.final_position = positions
                    current.positions_count += previous.positions_count
                    # set beta to max value
                    b = min(b, current.value, previous.value)

                # If alpha is greater or equal to beta, we found a contradiction break and skip rest of the tree
                if a >= b:
                    break

    # return the current class data
    return current


true_predecessors = [
    # One true
    [[False, False], [False, True]],
    [[False, False], [True, False]],
    [[True, False], [False, False]],
    [[False, True], [False, False]],
]

false_predecessors = [
    # All false
    [[False, False], [False, False]],
    # Two false
    [[False, True], [True, False]],
    [[False, True], [False, True]],
    [[True, False], [True, False]],
    [[True, False], [False, True]],
    [[True, True], [False, False]],
    [[False, False], [True, True]],
    # One false
    [[False, True], [True, True]],
    [[True, False], [True, True]],
    [[True, True], [False, True]],
    [[True, True], [True, False]],
    # All true
    [[True, True], [True, True]],
]

def solution(g):
    current_state = g
    # Creating the array for the previous state, where the dimensions are the same as the current state's dimensions + 1
    previous_state = []

    for i in range(len(current_state) + 1):
        previous_state.append([None] * (len(current_state[0]) + 1))

    # Now we will check the first column of the current state and fill the first two columns of the previous state accordingly
    possible_previous_states = []

    if current_state[0][0]:
        for predecessor in true_predecessors:
            previous_state[0][0] = predecessor[0][0]
            previous_state[1][0] = predecessor[1][0]
            previous_state[0][1] = predecessor[0][1]
            previous_state[1][1] = predecessor[1][1]
            possible_previous_states.append([list(sublist) for sublist in previous_state])
    else:
        for predecessor in false_predecessors:
            previous_state[0][0] = predecessor[0][0]
            previous_state[1][0] = predecessor[1][0]
            previous_state[0][1] = predecessor[0][1]
            previous_state[1][1] = predecessor[1][1]
            possible_previous_states.append([list(sublist) for sublist in previous_state])

    # Now we check current_state[1][0] and depending on the values in the possible_previous_states we will make a decision from predessors

    for i in range(1, len(current_state)):
        new_possible_previous_states = []
        for previous_state in possible_previous_states:
            common_row = [previous_state[i][0], previous_state[i][1]]
            if current_state[i][0]:
                for predecessor in true_predecessors:
                    if predecessor[0] == common_row:
                        new_state = [list(sublist) for sublist in previous_state] 
                        new_state[i + 1][0] = predecessor[1][0] 
                        new_state[i + 1][1] = predecessor[1][1] 
                        new_possible_previous_states.append(new_state)
            else:
                for predecessor in false_predecessors:
                    if predecessor[0] == common_row:
                        new_state = [list(sublist) for sublist in previous_state] 
                        new_state[i + 1][0] = predecessor[1][0] 
                        new_state[i + 1][1] = predecessor[1][1] 
                        new_possible_previous_states.append(new_state)
        possible_previous_states = new_possible_previous_states

    # Now we will do the same thing until we reach the last column of the current state
    # We need to do this without hardcoding the indexes, since the dimensions of the current state can change
    # But there is a trick here,
    # While generating the third column, if we are genearting the first step (first two rows), checking the common column will be enough
    # But if we are generating the other rows we need to check the other three

    for i in range(len(current_state[0])):
        for j in range(len(current_state)):
            new_possible_previous_states = []
            if j == 0:
                for previous_state in possible_previous_states:
                    common_column = [previous_state[j][i], previous_state[j+1][i]]
                    if current_state[j][i]:
                        for predecessor in true_predecessors:
                            if predecessor[0][1] == common_column[0] and predecessor[1][1] == common_column[1]:
                                new_state = [list(sublist) for sublist in previous_state] 
                                new_state[j][i+1] = predecessor[0][0]
                                new_state[j+1][i+1] = predecessor[1][0]
                                new_possible_previous_states.append(new_state)
                    else:
                        for predecessor in false_predecessors:
                            if predecessor[0][1] == common_column[0] and predecessor[1][1] == common_column[1]:
                                new_state = [list(sublist) for sublist in previous_state] 
                                new_state[j][i+1] = predecessor[0][0]
                                new_state[j+1][i+1] = predecessor[1][0]
                                new_possible_previous_states.append(new_state)
                possible_previous_states = new_possible_previous_states
            else:
                for previous_state in possible_previous_states:
                    common_elements = [previous_state[j][i], previous_state[j+1][i], previous_state[j][i+1]]
                    if current_state[j][i]:
                        for predecessor in true_predecessors:
                            if predecessor[0][1] == common_elements[0] and predecessor[1][1] == common_elements[1] and predecessor[0][0] == common_elements[2]:
                                new_state = [list(sublist) for sublist in previous_state] 
                                new_state[j][i+1] = predecessor[0][0]
                                new_state[j+1][i+1] = predecessor[1][0]
                                new_possible_previous_states.append(new_state)
                    else:
                        for predecessor in false_predecessors:
                            if predecessor[0][1] == common_elements[0] and predecessor[1][1] == common_elements[1] and predecessor[0][0] == common_elements[2]:
                                new_state = [list(sublist) for sublist in previous_state] 
                                new_state[j][i+1] = predecessor[0][0]
                                new_state[j+1][i+1] = predecessor[1][0]
                                new_possible_previous_states.append(new_state)
                possible_previous_states = new_possible_previous_states

    # Removing the states appearing more than once
    possible_previous_states = list(set([tuple([tuple(sublist) for sublist in result]) for result in possible_previous_states]))

    return len(possible_previous_states)
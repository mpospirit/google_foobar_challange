from fractions import Fraction

def create_transition_matrix(m):
    """
    Converts the given matrix to a transition matrix with probabilities.

    Creates the form
    I | 0
    --|--
    R | Q
    where I is the identity matrix, 0 is the zero matrix, R and Q are the submatrices.
    
    To achieve the desired form, we need to do the following:
    1. Convert the given numbers to probabilities by dividing each number by the sum of the row.
    2. Determine the terminal states (rows with all zeros).
    3. Convert the 0 in the self directed positions to 1.
    4. Reorder the columns and rows where the terminal states are first.
    """

    # Convert the given numbers to probabilities
    for i in range(len(m)):
        row_sum = sum(m[i])
        for j in range(len(m[i])):
            m[i][j] /= row_sum if row_sum != 0 else 1

    # Determine the terminal states
    terminal_states = []
    non_terminal_states = []
    for i in range(len(m)):
        if sum(m[i]) == 0:
            terminal_states.append(i)
        else:
            non_terminal_states.append(i)

    # Convert the 0 in the self directed positions to 1
    for i in range(len(m)):
        if i in terminal_states:
            m[i][i] = 1

    # Reorder the columns and rows where the terminal states are first
    new_m = []
    for i in terminal_states:
        new_m.append([m[i][j] for j in terminal_states + non_terminal_states])
    for i in non_terminal_states:
        new_m.append([m[i][j] for j in terminal_states + non_terminal_states])

    # Return the transition matrix and the number of terminal states
    return new_m, len(terminal_states)

def inverse_matrix(matrix):
    """
    Returns the inverse of the given matrix using the Gauss-Jordan elimination method.
    """
    size = len(matrix)
    inverse = [[0 if row != column else 1 for column in range(size)] for row in range(size)]

    for i in range(size):
        if matrix[i][i] == 0:
            for j in range(i + 1, size):
                if matrix[j][i] != 0:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    inverse[i], inverse[j] = inverse[j], inverse[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i + 1, size):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(size):
                matrix[j][k] -= ratio * matrix[i][k]
                inverse[j][k] -= ratio * inverse[i][k]
    for i in range(size - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(size):
                matrix[j][k] -= ratio * matrix[i][k]
                inverse[j][k] -= ratio * inverse[i][k]
        div = matrix[i][i]
        for k in range(size):
            matrix[i][k] /= div
            inverse[i][k] /= div
    return inverse

def calculate_fr(transition_matrix, terminal_states):
    """
    Calculates the fundamental matrix and the absorbing matrix from the given transition matrix.
    """
    # Split the transition matrix into the fundamental matrix and the absorbing matrix
    Q = []
    R = []

    # The matrix is in the form of
    # I | 0
    # --|--
    # R | Q
    # so R is on the bottom left and Q is on the bottom right
    
    # Q is the submatrix of transition_matrix containing transitions between non-terminal states
    # R is the submatrix of transition_matrix containing transitions from non-terminal states to terminal states
    for i in range(terminal_states, len(transition_matrix)):
        Q.append(transition_matrix[i][terminal_states:])
        R.append(transition_matrix[i][:terminal_states])

    # Calculate the fundamental matrix
    I = []
    for i in range(len(Q)):
        I.append([0] * len(Q))
        I[i][i] = 1

    # F = (I - Q)^-1
    F = []
    for i in range(len(Q)):
        F.append([I[i][j] - Q[i][j] for j in range(len(Q))])

    F = inverse_matrix(F)

    # Calculate the absorbing matrix which is F*R
    FR = []
    for i in range(len(F)):
        FR.append([0] * len(R[0]))
        for j in range(len(R[0])):
            for k in range(len(R)): 
                FR[i][j] += F[i][k] * R[k][j]

    return FR

def greates_common_divisor(list_of_numbers):
    """
    Returns the greatest common divisor of the given numbers.
    """
    if len(list_of_numbers) == 2:
        a, b = list_of_numbers
        while b:
            a, b = b, a % b
        return a
    else:
        return greates_common_divisor([list_of_numbers[0], greates_common_divisor(list_of_numbers[1:])])

def least_common_multiple(list_of_numbers):
    """
    Returns the least common multiple of the given numbers.
    """
    lcm = list_of_numbers[0]
    for i in list_of_numbers[1:]:
        lcm = lcm * i // greates_common_divisor([lcm, i])
    return lcm

def solution(m):
    if len(m) == 1:
        return [1, 1]
    
    # Convert the given matrix to a transition matrix with probabilities
    transition_matrix, terminal_states_count = create_transition_matrix(m)

    # Calculate the fundamental matrix and the absorbing matrix from the given transition matrix
    FR = calculate_fr(transition_matrix, terminal_states_count)

    # Converting the probabilities to fractions
    FR = [[Fraction(x).limit_denominator() for x in FR[i]] for i in range(len(FR))]

    # Since the starting state is 0, we can directly return the first row of the absorbing matrix
    probabilities = FR[0]

    # Now we need to find the least common multiple of the denominators
    denominators = [x.denominator for x in probabilities]
    lcm = least_common_multiple(denominators)

    # Return the result
    result = [x.numerator * (lcm // x.denominator) for x in probabilities] + [lcm]
    
    return result
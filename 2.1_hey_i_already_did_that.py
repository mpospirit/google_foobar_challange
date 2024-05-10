def to_base_b(n, b):
    """
    Converts an integer n to a string in base b.
    """
    if n == 0:
        return '0'

    numbers = []

    while n:
        n, r = divmod(n, b)
        numbers.append(str(r))

    return ''.join(reversed(numbers))

def solution(n, b):
    list_of_z = []

    while True:
        # Converting n to a string
        n = str(n)

        # Creating x by sorting n in descending order
        x = ''.join(sorted(n, reverse=True))

        # Creating y by sorting n in ascending order
        y = ''.join(sorted(n))

        # Converting x and y to base b
        x = int(x, b)
        y = int(y, b)

        # Calculating z
        z = x - y

        # Converting z to base b
        z = to_base_b(z, b)

        # Adding leading zeros to z to maintain length k if necessary
        while len(z) < len(n):
            z = '0' + z

        # Checking if z is in the list of z's
        if z in list_of_z:
            return len(list_of_z) - list_of_z.index(z)
        else:
            list_of_z.append(z)
            n = z
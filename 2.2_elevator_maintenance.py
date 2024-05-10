def sort_key(s):
    """
    Splits the string on the '.' character, 
    converts each part of the split string to an integer,
    and returns the list of integer parts.
    """
    # Splitting the string on the '.' character
    split_string = s.split('.')

    # Converting each part of the split string to an integer
    integer_parts = map(int, split_string)

    return list(integer_parts)

def solution(l):
    # Sorting the list using the defined key function
    l.sort(key=sort_key)

    # Returning the sorted list
    return l
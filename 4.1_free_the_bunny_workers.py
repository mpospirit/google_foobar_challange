from itertools import combinations

def solution(num_buns, num_required):
    # Tricky part is to figure out how many copies of each key to give to the bunnies
    replicas = num_buns - num_required + 1
    
    key_pairs = list(combinations(range(num_buns), replicas))

    # Creating a dictionary to store the keys for each bunny
    keys = {}
    for i in range(num_buns):
        keys[i] = []

    # Assigning the keys to the bunnies
    for i in range(len(key_pairs)):
        for j in key_pairs[i]:
            keys[j].append(i)

    # Creating a list of the keys for each bunny
    key_list = []
    for i in range(num_buns):
        key_list.append(keys[i])

    return key_list
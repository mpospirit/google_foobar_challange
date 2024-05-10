def astar(map):
    """
    A* algorithm to find the shortest path in a binary maze,
    starting from the top left and ending at the bottom right.
    """
    start = (0, 0)
    goal = (len(map) - 1, len(map[0]) - 1)

    # Defining movement directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initializing open and closed lists
    open_list = []
    closed_set = set()

    # Adding start node to open list
    open_list.append((0, start, 0))  # (total_cost, node, g_cost)

    while open_list:
        open_list.sort(key=lambda x: x[0])  # Sort by total_cost
        total_cost, current_node, g_cost = open_list.pop(0)
        closed_set.add(current_node)

        # Checking if current node is goal node
        if current_node == goal:
            return g_cost + 1

        # Generating successors (neighbors) of current node
        for dr, dc in directions:
            neighbor_row, neighbor_col = current_node[0] + dr, current_node[1] + dc

            # Checking if neighbor is within bounds and not a wall
            if 0 <= neighbor_row < len(map) and 0 <= neighbor_col < len(map[0]) and map[neighbor_row][neighbor_col] == 0:
                neighbor_node = (neighbor_row, neighbor_col)
                # Calculating heuristic (h value)
                heuristic = abs(neighbor_row - goal[0]) + abs(neighbor_col - goal[1])
                # Calculating total cost (f value)
                total_cost = g_cost + 1 + heuristic  # Cost to move to neighbor is 1
                # Checking if neighbor is already in closed set
                if neighbor_node in closed_set:
                    continue
                # Checking if neighbor is already in open list and has a lower total cost
                for i, (tc, n, _) in enumerate(open_list):
                    if n == neighbor_node and total_cost >= tc:
                        break
                else:
                    open_list.append((total_cost, neighbor_node, g_cost + 1))

    # If no path found
    return len(map) * len(map[0])

def wall_breaker(map):
    """
    For a given map, generates all possible maps with
    breaking one wall at a time (Converting 1 to 0) and returns the dictionary
    of the newly generated maps.
    """
    new_maps = {}
    # Before creating new maps, we append the original map to the dictionary
    new_maps["original_map"] = map

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                new_map = [row[:] for row in map]
                new_map[i][j] = 0
                new_maps["map_{0}_{1}".format(i, j)] = new_map

    return new_maps

def solution(map):
    # Get all possible maps by breaking one wall at a time
    new_maps = wall_breaker(map)

    # Finding the shortest path for each map
    shortest_paths = {}

    for key, value in new_maps.items():
        shortest_paths[key] = astar(value)

    # Returning the minimum path length
    return min(shortest_paths.values())
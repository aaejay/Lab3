# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Dhfh3BDzLLT5Znv5yq4XEtJVab3srgQp
"""

from collections import deque

def find_shortest_path(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    start, end = (1, 1), (4, 4)

    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == end:
            return path  # Shortest path found

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == 0 and (nx, ny) not in visited:
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None  # No path found

# Example usage
matrix = [[0]*6 for _ in range(6)]  # Replace with actual grid
print(find_shortest_path(matrix))

"""# New Section"""

import time

def state_to_tuple(state):
    return tuple(state)

def get_moves(state):
    moves = []
    zero_index = state.index('0')
    row, col = zero_index // 3, zero_index % 3
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

    for move, (dr, dc) in directions.items():
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_index = nr * 3 + nc
            new_state = list(state)
            new_state[zero_index], new_state[new_index] = new_state[new_index], new_state[zero_index]
            moves.append(tuple(new_state))

    return moves

def dfs(start_state, goal_state):
    stack = [(start_state, [])]
    visited = set()

    while stack:
        current_state, path = stack.pop()

        if current_state == goal_state:
            return path

        visited.add(current_state)

        for move in get_moves(current_state):
            if move not in visited:
                stack.append((move, path + [move]))

    return None  # No solution found

def main():
    start_state = input("Enter start State: ")
    goal_state = input("Enter goal State: ")

    start_tuple, goal_tuple = state_to_tuple(start_state), state_to_tuple(goal_state)

    start_time = time.time()
    solution_path = dfs(start_tuple, goal_tuple)
    end_time = time.time()

    if solution_path:
        print("Time taken:", end_time - start_time, "seconds")
        print("Path Cost:", len(solution_path))
        print("No of Nodes Visited:", len(solution_path) + 1)
        for state in solution_path:
            for i in range(0, 9, 3):
                print(' '.join(state[i:i+3]))
            print("------")
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()

"""# New Section"""

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list.get(v, [])

    def h(self, n):
        H = {'The': 4, 'cat': 3, 'dog': 3, 'runs': 2, 'fast': 1}
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        open_list, closed_list = set([start_node]), set([])
        g, parents = {start_node: 0}, {start_node: start_node}

        while open_list:
            n = min(open_list, key=lambda node: g[node] + self.h(node))
            if n == stop_node:
                path = []
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
                path.append(start_node)
                return path[::-1], g[stop_node]

            open_list.remove(n)
            closed_list.add(n)

            for (m, cost) in self.get_neighbors(n):
                if m in closed_list:
                    continue
                if m not in open_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + cost
                elif g[m] > g[n] + cost:
                    g[m] = g[n] + cost
                    parents[m] = n

        print("Path does not exist!")
        return None, None

adjacency_list = {
    'The': [('cat', 1), ('dog', 2)],
    'cat': [('runs', 1)],
    'dog': [('runs', 2)],
    'runs': [('fast', 2)],
    'fast': []
}

graph1 = Graph(adjacency_list)
path, cost = graph1.a_star_algorithm('The', 'fast')

if path:
    print("Sentence:", " ".join(path))
    print("Total cost:", cost)
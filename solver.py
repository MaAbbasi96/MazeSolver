# depth-limited dfs
from math import sqrt
from heapq import heappush, heappop

def dls_solver(maze, limit):
    parent = {}
    path = []
    stack = []
    stack.append(maze.start)
    goal = maze.start
    discovered = {}
    distance = {}
    distance[maze.start] = 0
    while stack:
        cell = stack.pop(-1)
        count = distance[cell]
        if cell == maze.goal:
            break
        if discovered.setdefault(cell, False) or count >= limit:
            continue
        discovered[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discovered.setdefault(ncell, False):
                stack.append(ncell)
                goal = ncell
                distance[ncell] = count + 1
                parent[ncell] = cell
    path.append(goal)
    while not path[0] == maze.start:
        path.insert(0, parent[goal])
        goal = parent[goal]
    return path


def iterative_dfs_solver(maze):
    for limit in range(10000):
        path = dls_solver(maze, limit)
        if path[-1] == maze.goal:
            return path
    return []

def dfs_solver(maze):
    parent = {}
    path = []
    stack = []
    stack.append(maze.start)
    goal = maze.start
    discovered = {}
    while stack:
        cell = stack.pop(-1)
        if cell == maze.goal:
            break
        if(discovered.setdefault(cell, False)):
            continue
        discovered[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discovered.setdefault(ncell, False):
                parent[ncell] = cell
                stack.append(ncell)
                goal = ncell
    path.append(goal)
    while not path[0] == maze.start:
        path.insert(0, parent[goal])
        goal = parent[goal]
    return path


def bfs_solver(maze):
    parent = {}
    path = []
    queue = []
    goal = maze.start
    queue.append(maze.start)
    discovered = {}
    while queue:
        cell = queue.pop(0)
        goal = cell
        if cell == maze.goal:
            break
        if(discovered.setdefault(cell, False)):
            continue
        discovered[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discovered.setdefault(ncell, False):
                queue.append(ncell)
                parent[ncell] = cell
    path.append(goal)
    while not path[0] == maze.start:
        path.insert(0, parent[goal])
        goal = parent[goal]
    return path


def astar_heuristic(maze, cell):
    return abs(maze.goal[0] - cell[0]) + abs(maze.goal[1] - cell[1])


def astar_solver(maze):
    parent = {}
    path = []
    heap = []
    cell_map = {}
    discovered = {}
    distance = astar_heuristic(maze, maze.start)
    goal = maze.start
    heappush(heap, distance)
    cell_map.setdefault(distance, []).append(maze.start)
    while True:
        cell = cell_map[heappop(heap)].pop()
        if cell == maze.goal:
            break
        if(discovered.setdefault(cell, False)):
            continue
        discovered[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discovered.setdefault(ncell, False):
                distance = astar_heuristic(maze, ncell)
                heappush(heap, distance)
                cell_map.setdefault(distance, []).append(ncell)
                goal = ncell
                parent[goal] = cell
    path.append(goal)
    while not path[0] == maze.start:
        path.insert(0, parent[goal])
        goal = parent[goal]
    return path

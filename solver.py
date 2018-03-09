# depth-limited dfs
from math import sqrt
from heapq import heappush, heappop

def dls_solver(maze, limit):
    path = []
    stack = []
    stack.append(maze.start)
    path.append(maze.start)
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
                path.append(ncell)
                distance[ncell] = count + 1
    return path


def iterative_dfs_solver(maze):
    for limit in range(10000):
        path = dls_solver(maze, limit)
        if path[-1] == maze.goal:
            return path
    return []

def dfs_solver(maze):
    path = []
    stack = []
    stack.append(maze.start)
    path.append(maze.start)
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
                stack.append(ncell)
                path.append(ncell)
    return path


def bfs_solver(maze):
    path = []
    queue = []
    path.append(maze.start)
    queue.append(maze.start)
    discovered = {}
    while queue:
        cell = queue.pop(0)
        if cell == maze.goal:
            break
        if(discovered.setdefault(cell, False)):
            continue
        discovered[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discovered.setdefault(ncell, False):
                queue.append(ncell)
                path.append(ncell)
    return path


def astar_heuristic(maze, cell, cost):
    return 0 * cost + sqrt((maze.goal[0] - cell[0]) * (maze.goal[0] - cell[0]) + (maze.goal[1] - cell[1]) * (maze.goal[1] - cell[1]))


def astar_solver(maze):
    path = []
    heap = []
    cell_map = {}
    discovered = {}
    distance = astar_heuristic(maze, maze.start, len(path))
    path.append(maze.start)
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
                distance = astar_heuristic(maze, ncell, len(path))
                heappush(heap, distance)
                cell_map.setdefault(distance, []).append(ncell)
                path.append(ncell)
    return path

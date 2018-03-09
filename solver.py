# depth-limited dfs
def dls_solver(maze, limit):
    return []


def iterative_dfs_solver(maze):
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
    print(path)
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
    print(path)
    return path


def astar_heuristic(maze, cell):
    return 0


def astar_solver(maze):
    return []

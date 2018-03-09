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
    discoverd = {}
    while len(stack) > 0:
        cell = stack[-1]
        if cell == maze.goal:
            break
        stack.pop()
        if(discoverd.setdefault(cell, False)):
            continue
        discoverd[cell] = True
        for ncell in maze.get_neighbors(cell):
            if not discoverd.setdefault(ncell, False):
                stack.append(ncell)
                path.append(ncell)
    print(path)
    return path


def bfs_solver(maze):
    return []


def astar_heuristic(maze, cell):
    return 0


def astar_solver(maze):
    return []

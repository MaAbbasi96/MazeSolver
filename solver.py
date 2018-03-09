# depth-limited dfs
def dls_solver(maze, limit):
    return []


def iterative_dfs_solver(maze):
    return []

def dfs(maze, path, discoverd):
    if path[-1] == maze.goal:
        return
    discoverd[path[-1]] = True
    for cell in maze.get_neighbors(path[-1]):
        if not discoverd.setdefault(cell, False):
            path.append(cell)
            dfs(maze, path, discoverd)

def dfs_solver(maze):
    path = []
    stack = []
    path.append(maze.start)
    while path.count() > 0 or finished:
        cell = path[-1]
        path.pop()
        if discoverd.setdefault(cell, False):
            continue
        discoverd[cell] = True
        print(cell)
        for adj in maze.get_neighbors(cell):
            if discoverd.setdefault(adj, False):
                path.append(adj)
    return path


def bfs_solver(maze):
    return []


def astar_heuristic(maze, cell):
    return 0


def astar_solver(maze):
    return []

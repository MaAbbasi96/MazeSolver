# depth-limited dfs
from math import sqrt
from heapq import heappush, heappop
import numpy as np
import random


UP = 0
RIGHT = 1
LEFT = 2
DOWN = 3
ACTIONS = [UP, RIGHT, LEFT, DOWN]
ACTIONS_LEN = 4

x = 0
y = 1

q_dict = {}


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


def new_position(cell, action):
    if action == UP:
        ncell = (cell[x], cell[y]-1)
    elif action == DOWN:
        ncell = (cell[x], cell[y]+1)
    elif action == LEFT:
        ncell = (cell[x]-1, cell[y])
    elif action == RIGHT:
        ncell = (cell[x]+1, cell[y])
    return ncell


def take_action(maze, cell, action):
    ncell = new_position(cell, action)
    is_valid = True
    if not maze.cell_is_valid(ncell):
        reward = -100
        is_finished = False
        ncell = cell
        is_valid = False
    elif maze.check_wall(cell, ncell) != 0:
        reward = -100
        is_finished = False
        ncell = cell
        is_valid = False
    elif ncell == maze.goal:
        reward = 1000
        is_finished = True
    else:
        reward = -1
        is_finished = False
    return ncell, reward, is_finished, is_valid


def q(cell, action=None):
    if cell not in q_dict:
        q_dict[cell] = np.zeros(ACTIONS_LEN)    
    if action is None:
        return q_dict[cell]
    return q_dict[cell][action]


def make_action(cell, eps):
    if random.uniform(0, 1) < eps:
        return random.choice(ACTIONS) 
    else:
        return np.argmax(q(cell))

def q_learning(maze):
    N_STATES = 4
    N_EPISODES = 500
    MIN_ALPHA = 0.02
    eps = 0.3
    MAX_EPISODE_STEPS = maze.nrows * maze.ncols * 3
    heap = []
    alphas = np.linspace(1.0, MIN_ALPHA, N_EPISODES)
    for i in range(N_EPISODES):
        cell = maze.start
        total_reward = 0
        alpha = alphas[i]
        count = 0
        for j in range(MAX_EPISODE_STEPS):
            action = make_action(cell, eps)
            ncell, reward, is_finished, is_valid = take_action(maze, cell, action)
            total_reward += reward
            if is_valid:
                count += 1
            q(cell)[action] = q(cell, action) + alpha * (reward + np.max(q(ncell)) - q(cell, action))
            cell = ncell
            if is_finished:
                print('Goal Reached.....!')
                break
        heappush(heap, count)
        print("Episode {}: total reward: {}, cost: {}".format(i, total_reward, count))
    print('Best path cost: {}'.format(heappop(heap)))
    return []

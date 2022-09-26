from collections import deque

maze = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0]]

# This is a 2D list in Python. Note that the first row in the 2D list is the y = 0 row (i.e. bottom-most row in the maze figure). 
# '1' indicates that the node is blocked, '0' indicates that it is free.
path = []
finalPath = []

def backtrack(parent, start, end):
    path = []
    path.append(end)
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return path

def dfs(starti, startj, end):
    parent = {}
    # return if edge of maze
    if starti > len(maze[0]) - 1 or startj > len(maze) - 1 or starti < 0 or startj < 0:
        return
    
    stack = []
    stack.append((starti, startj))

    leaves = [(-1,0),(0,1),(1,0),(0,-1)]

    while stack:
        current = stack.pop()
        path.append(current)

        if current[0] == end[0] and current[1] == end[1]:
            finalPath = backtrack(parent, (starti, startj), (end[0], end[1]))
            print("DFS 2 path:", finalPath, " Cost:", len(finalPath), " Nodes explored:", len(path))
            path.clear()
            finalPath.clear()
            return
        
        for x,y in leaves:
            i = current[0] + x
            j = current[1] + y
            if not (i > len(maze[0]) - 1 or j > len(maze) - 1 or i < 0 or j < 0) and maze[i][j] == 0 and (i, j) not in path:
                stack.append((i, j))
                parent[(i, j)] = current

    return

def bfs(starti, startj, end):
    parent = {}
    # return if edge of maze
    if starti > len(maze[0]) - 1 or startj > len(maze) - 1 or starti < 0 or startj < 0:
        return
    
    queue = deque()
    queue.append((starti, startj))

    leaves = [(-1,0),(0,1),(1,0),(0,-1)]

    while queue:
        current = queue.popleft()
        path.append(current)

        if current[0] == end[0] and current[1] == end[1]:
            finalPath = backtrack(parent, (starti, startj), (end[0], end[1]))
            print("BFS path:", finalPath, " Cost:", len(finalPath), " Nodes explored:", len(path))
            path.clear()
            finalPath.clear()
            return
        
        for x,y in leaves:
            i = current[0] + x
            j = current[1] + y
            if not (i > len(maze[0]) - 1 or j > len(maze) - 1 or i < 0 or j < 0) and maze[i][j] == 0 and (i, j) not in path and (i, j) not in queue:
                queue.append((i, j))
                parent[(i, j)] = current

    return

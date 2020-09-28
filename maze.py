import random

def gen_maze(x,y):
    maze = []
    for n in range(1, x+1):
        maze1 = []
        for m in range(1, y+1):
            maze1.append("0")
        maze.append(maze1)
    return maze

def logic(maze):
    for i in range(1, x+1):
        for j in range(1, y+1):
            wall = random.randint(0,1)
            if i == 1:
                maze[i-1][j-1] = "0"
            elif j == y+1:
                maze[i-2][j-1] = "0"
            elif wall == 0:
                maze[i-2][j-1] = "0"
            elif wall == 1:
                maze[i-1][j-2] = "1"
    return maze

x = int(input())
y = int(input())
maze_n = gen_maze(x,y)
maze_m = logic(maze_n)
for q in maze_m:
    print(q)

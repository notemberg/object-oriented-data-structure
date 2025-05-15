# Explanation:
# The solve_maze function recursively explores all possible paths through the maze.
# The base case handles out-of-bounds conditions, walls, and the end of the maze.
# Recursive calls explore all directions. If a path is found, it prints the path and returns True.
# Backtracking occurs if a dead-end is reached, ensuring other paths are explored.

def solve_maze(maze, x, y, path=None):
    if path is None:
        path = []
    
    # Base case: if out of bounds or hitting a wall (denoted by 1)
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == 1:
        return False
    
    # Check if we've reached the end of the maze (denoted by 9)
    if maze[x][y] == 9:
        path.append((x, y))
        print("Path found:", path)
        return True
    
    # Mark the current cell as part of the path
    path.append((x, y))
    maze[x][y] = 1  # Mark as visited
    
    # Explore the 4 directions (down, up, right, left)
    if (solve_maze(maze, x+1, y, path) or  # down
        solve_maze(maze, x-1, y, path) or  # up
        solve_maze(maze, x, y+1, path) or  # right
        solve_maze(maze, x, y-1, path)):   # left
        return True
    
    # Backtrack
    path.pop()
    return False

# Example usage:
maze = [
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 9],
    [0, 0, 0, 1, 1]
]
solve_maze(maze, 0, 0)

# Explanation:
# The function flood_fill recursively changes the color of the target cell and all connected cells with the same color.
# The base case ensures that recursion stops when the cell is out of bounds or does not match the target color.
# Recursive calls are made in four directions, allowing the function to traverse the matrix and fill all connected cells.

def flood_fill(matrix, x, y, target_color, new_color):
    # Base case: if out of bounds or the color is not the target color
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]):
        return
    if matrix[x][y] != target_color:
        return
    
    # Change the color
    matrix[x][y] = new_color
    
    # Recursive calls in 4 directions (up, down, left, right)
    flood_fill(matrix, x+1, y, target_color, new_color)  # down
    flood_fill(matrix, x-1, y, target_color, new_color)  # up
    flood_fill(matrix, x, y+1, target_color, new_color)  # right
    flood_fill(matrix, x, y-1, target_color, new_color)  # left

# Example usage:
matrix = [
    [1, 1, 1, 2],
    [1, 2, 1, 2],
    [1, 1, 2, 2],
    [2, 2, 2, 2]
]
flood_fill(matrix, 1, 1, 2, 3)
print(matrix)



# In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20 x 20 grid?
# Read the grid from the text file
grid = []
with open('Problem 11 Largest Product in a Grid.txt', 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split()))
        grid.append(row)

# Function to calculate the product of four adjacent numbers in a given direction
def calculate_product(row, col, dx, dy):
    product = 1
    for i in range(4):
        product *= grid[row + i * dx][col + i * dy]
    return product

# Initialize variables to store the maximum product and its corresponding position
max_product = 0
max_position = None

# Iterate over each position in the grid
for row in range(len(grid)):
    for col in range(len(grid[row])):
        # Calculate the product in each direction: right, down, diagonal down-right, diagonal down-left
        directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for dx, dy in directions:
            if row + 3 * dx < len(grid) and col + 3 * dy < len(grid[row]):
                product = calculate_product(row, col, dx, dy)
                if product > max_product:
                    max_product = product

# Print the result
print("The greatest product of four adjacent numbers is:", max_product)
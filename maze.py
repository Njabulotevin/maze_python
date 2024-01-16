import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Maze Generator")
robot = turtle.Turtle()



# Set up the turtle
turtle.speed(0)
turtle.penup()
turtle.pensize(2)

# Maze dimensions
rows = 80
columns = 40
cell_size = 10

# Create a 2D list to represent the maze
maze = [[0] * columns for _ in range(rows)]


# Function to draw a rectangle at given coordinates
def draw_rectangle(x, y, color):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.fillcolor(color)
    for _ in range(4):
        turtle.forward(cell_size)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()


# Function to draw the maze
def draw_maze():
    for row in range(rows):
        for col in range(columns):
            if maze[row][col] == 1:
                draw_rectangle(col * cell_size, -row * cell_size, "black")

# Recursive backtracking algorithm to generate the maze
def generate_maze(row, col):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)

    for dr, dc in directions:
        new_row, new_col = row + 2 * dr, col + 2 * dc

        if 0 <= new_row < rows and 0 <= new_col < columns and maze[new_row][new_col] == 0:
            maze[row + dr][col + dc] = 1
            maze[new_row][new_col] = 1
            generate_maze(new_row, new_col)

# Generate the maze starting from the top-left corner
generate_maze(-100, 200)



turtle.done()



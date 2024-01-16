import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Maze Generator")
robot = turtle.Turtle('square')
robot.color("yellow")
robot.shapesize(stretch_wid=0.3, stretch_len=0.3)

# Set up the turtle
turtle.penup()



robot._tracer(0, 0)
# Maze dimensions
rows = 20
columns = 20
cell_size = 10


start_x = -100
start_y = 100

neg_co = -1*cell_size

avoid_coordinates = [(0, 0), (cell_size, neg_co), (neg_co, cell_size), (0, cell_size)]
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
                draw_rectangle(start_x + col * cell_size, start_y - row * cell_size, "red")


# Recursive backtracking algorithm to generate the maze
def generate_maze(row, col):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    random.shuffle(directions)
    for dr, dc in directions:
        new_row, new_col = row + 2 * dr, col + 2 * dc
        
        if 0 <= new_row < rows and 0 <= new_col < columns and maze[new_row][new_col] == 0:
            new_coordinates = (new_row * cell_size, -new_col * cell_size)
            if new_coordinates in avoid_coordinates:
                # Skip the specified coordinates
                continue
            maze[row + dr][col + dc] = 1
            maze[new_row][new_col] = 1
            generate_maze(new_row, new_col)



# Generate the maze starting from the top-left corner
generate_maze(0, 0)

# Draw the generated maze
draw_maze()
robot._update()
robot.goto(0,-10)
# Hide the turtle and display the window


turtle.hideturtle()
screen.mainloop()

import pygame
import sys
import tkinter as tk
from tkinter import ttk

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
CELL_SIZE = 40
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLAYER_COLOR = (0, 128, 255)
END_COLOR = (255, 0, 0)

# Maze representation (0 represents a wall, 1 represents a path)
MAZE = [
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")
clock = pygame.time.Clock()

# Initial player position
player_x, player_y = 0, 0

# End position
end_x, end_y = len(MAZE[0]) - 5, len(MAZE) - 9

# Function queue
function_queue = []

# Function to move player one pixel left
def move_left():
    global player_x
    if player_x > 0 and MAZE[player_y][player_x - 1] == 1:
        player_x -= 1

# Function to move player one pixel right
def move_right():
    global player_x
    if player_x < len(MAZE[0]) - 1 and MAZE[player_y][player_x + 1] == 1:
        player_x += 1

# Function to move player one pixel up
def move_up():
    global player_y
    if player_y > 0 and MAZE[player_y - 1][player_x] == 1:
        player_y -= 1

# Function to move player one pixel down
def move_down():
    global player_y
    if player_y < len(MAZE) - 1 and MAZE[player_y + 1][player_x] == 1:
        player_y += 1

# Create tkinter window
root = tk.Tk()
root.title("Maze Solver")

# Create a text entry area for code input
code_entry = tk.Text(root, height=10, width=50)
code_entry.pack()

# Function to handle "Run Code" button click
def run_code():
    code = code_entry.get("1.0", tk.END)
    lines = code.split('\n')
    for line in lines:
        try:
            function_queue.append(line)
        except Exception as e:
            print(f"Error: {e}")

# Create "Run Code" button
run_button = ttk.Button(root, text="Run Code", command=run_code)
run_button.pack()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Execute the functions in the queue
    if function_queue:
        line = function_queue.pop(0)
        try:
            exec(line)
        except Exception as e:
            print(f"Error: {e}")
        clock.tick(10)  # Introduce a delay between movements

    # Check if the player reached the end
    if player_x == end_x and player_y == end_y:
        print("Congratulations! You reached the end.")
        pygame.quit()
        sys.exit()

    # Clear the screen
    screen.fill(WHITE)

    # Draw the maze
    for y, row in enumerate(MAZE):
        for x, cell in enumerate(row):
            if cell == 0:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the player
    pygame.draw.rect(screen, PLAYER_COLOR, (player_x * CELL_SIZE, player_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Draw the end
    pygame.draw.rect(screen, END_COLOR, (end_x * CELL_SIZE, end_y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

    # Update tkinter window
    root.update()

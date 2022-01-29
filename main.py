import random
import sys
import time
import pygame
import tkinter as tk

pygame.init()

# Constants
WHITE = (255, 255, 255)  # background

# List of colors used for the digits
"""
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (252, 232, 3)
ORANGE = (0, 255, 255)
PINK = (255, 0, 255)
GRAY = (192, 192, 192)
PURPLE = (255, 139, 0)
BROWN = (128, 0, 0)
"""
""" New color scheme
BLACK = (0, 0, 0)
RED = (173, 35, 35)
GREEN = (29, 105, 20)
BLUE = (42, 75, 215)
YELLOW = (255, 238, 51)
ORANGE = (255, 146, 51)
GRAY = (87, 87, 87)
PINK = (255, 205, 243)
PURPLE = (129, 38, 192)
BROWN = (129, 74, 25)
"""
BLACK = (0, 0, 0)
RED = (230, 25, 75)
GREEN = (60, 180, 75)
BLUE = (0, 130, 200)
YELLOW = (255, 225, 25)
ORANGE = (245, 130, 48)
GRAY = (128, 128, 128)
PINK = (255, 155, 200)  # (255, 205, 243)
PURPLE = (145, 30, 180)
BROWN = (170, 110, 40)

COLORS = [BLACK, RED, GREEN, BLUE, YELLOW, ORANGE, GRAY, PINK, PURPLE, BROWN]
random.shuffle(COLORS)

# SCREEN_HEIGHT = 768
# SCREEN_WIDTH = 1366
FONT_SIZE = 128
FONT_NAME = "Arial"
FONT_RATIO = 1 - 0.46  # change the second number to what you find on Google
font_obj = pygame.font.SysFont(FONT_NAME, FONT_SIZE)
TIME_AFTER_SPACE = 0.1
SHOW_TIME = 0.5  # the amount of seconds for which the digits will be presented
LENGTH = 8  # length of the sequence
TRIALS = 30  # amount of successive trials
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
WRITE_MODE = 1  # use 0 for not recording the results

# --- THESE ARE THE ONLY ONES YOU SHOULD CHANGE
GAME_MODE = "RANDOM"  # "ASSIGNED" for assigned colors, "RANDOM" for random colors
SUBJECT_NUMBER = 20  # use current participant number


def wait_for_spacebar():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return


def draw_it(numbers):
    random_colors = [BLACK, RED, GREEN, BLUE, YELLOW, ORANGE, GRAY, PINK, PURPLE, BROWN]
    random.shuffle(random_colors)
    for i in range(LENGTH):
        # Create a random font color
        if GAME_MODE == "ASSIGNED":
            font_color = COLORS[int(numbers[i])]
        else:
            font_color = random.choice(random_colors)
            random_colors.remove(font_color)
        # Create a random font surface
        font_surface = font_obj.render(numbers[i], True, font_color)
        # Font position
        font_position = (SCREEN_WIDTH / 2 - LENGTH * FONT_SIZE / 2 * FONT_RATIO + i * FONT_SIZE * FONT_RATIO,
                         SCREEN_HEIGHT / 2 - FONT_SIZE / 2)
        # Draw the font surface on the screen
        screen.blit(font_surface, font_position)


def get_numbers():
    numbers = DIGITS
    random.shuffle(numbers)
    numbers = numbers[:LENGTH]
    return numbers


def show_it():
    time.sleep(TIME_AFTER_SPACE)
    pygame.display.flip()
    time.sleep(SHOW_TIME)
    screen.fill(WHITE)
    pygame.display.flip()


# Set the width and height of the screen [width, height]
root = tk.Tk()
SCREEN_WIDTH = root.winfo_screenwidth()
SCREEN_HEIGHT = root.winfo_screenheight()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BSS Experiment")

numbers = []  # get an empty array
if WRITE_MODE == 1:  # open a new text document
    f = open(str(SUBJECT_NUMBER) + "_" + GAME_MODE + '.csv', 'w')
done = False  # Loop until the user clicks the close button.
clock = pygame.time.Clock()  # Used to manage how fast the screen updates

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Here, we clear the screen to white. Don't put other drawing commands, they would be erased.
    screen.fill(WHITE)
    pygame.display.flip()

    # --- Loop for showing the digits
    for k in range(0, TRIALS):
        numbers = get_numbers()
        if WRITE_MODE == 1:
            f.write(str(numbers) + '\n')
        draw_it(numbers)
        wait_for_spacebar()
        show_it()

    # Close the window, close file and quit.
    if WRITE_MODE == 1:
        f.close()
    pygame.quit()
    sys.exit()

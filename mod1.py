import pygame
from pygame.locals import *
import sys

pygame.init()





# CHANGE THESE -----------------------------------------------------------------------------
# Colors (Red, Blue, Green) MAX Number is 255
background_color = (0, 0, 0)
bar_color = (255, 255, 255)
line_color = (255, 255, 255)


# Sizes/Lengths
screen_size = (640, 480)
bar_size = (5, 50)
circle_size = (8, 8)
frame_size = (630, 470)
line_length = 15
line_width = 1


# Speed
bar_speed = 250.0
circle_speed = 250.0
speed_x = 250.0
speed_y = 250.0
speed_2_circ = 250.0


# -----------------------------------------------------------------------------------------










bar1_score = 0
bar2_score = 0
screen = pygame.display.set_mode(screen_size, 0, 32)
pygame.display.set_caption("Pong Lesson")

back = pygame.Surface((screen_size[0], screen_size[1]))
background = back.convert()
background.fill(background_color)

bar = pygame.Surface(bar_size)
bar1 = bar.convert()
bar2 = bar.convert()
bar1.fill(bar_color)
bar2.fill(bar_color)

circ_sur = pygame.Surface(circle_size)
circ_sur.fill(background_color)
circ = pygame.draw.circle(circ_sur, bar_color, (circle_size[0] // 2, circle_size[1] // 2), circle_size[0] // 2)
circle = circ_sur.convert()
circle.set_colorkey(background_color)

# some definitions
bar1_x, bar2_x = 10.0, screen_size[0] - bar_size[0] - 10.0
bar1_y, bar2_y = 215.0, 215.0
circle_x, circle_y = screen_size[0] // 2, screen_size[1] // 2
bar1_move, bar2_move = 0.0, 0.0

# clock and font objects
clock = pygame.time.Clock()
font = pygame.font.SysFont("calibri", 40)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Get the current mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Update the player paddle position based on the mouse y-coordinate
    bar1_y = mouse_y - bar1.get_height() // 2

    # Ensure the player paddle stays within the screen boundaries
    if bar1_y < 10:
        bar1_y = 10
    elif bar1_y > screen_size[1] - bar1.get_height() - 10:
        bar1_y = screen_size[1] - bar1.get_height() - 10

    score1 = font.render("" + str(bar1_score), True, bar_color)
    score2 = font.render("" + str(bar2_score), True, bar_color)

    screen.blit(background, (0, 0))
    frame = pygame.draw.rect(screen, line_color, Rect((5, 5), frame_size), line_width)

    dash_length = 5
    dash_gap = 5
    dash_count = int(frame_size[1] / (dash_length + dash_gap))

    for i in range(dash_count):
        y_pos = 5 + i * (dash_length + dash_gap)
        pygame.draw.aaline(screen, line_color, (screen_size[0] / 2, y_pos), (screen_size[0] / 2, y_pos + dash_length))

       
    screen.blit(bar1, (bar1_x, bar1_y))
    screen.blit(bar2, (bar2_x, bar2_y))
    screen.blit(circle, (circle_x, circle_y))
    screen.blit(score1, (250., 210.))
    screen.blit(score2, (380., 210.))

    bar1_y += bar1_move

    # movement of circle
    time_passed = clock.tick(30)
    time_sec = time_passed / 1000.0

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec
    ai_speed = speed_2_circ * time_sec
    # AI of the computer.
    if circle_x >= 305.:
        if not bar2_y == circle_y + 7.5:
            if bar2_y < circle_y + 7.5:
                bar2_y += ai_speed
            if bar2_y > circle_y - 42.5:
                bar2_y -= ai_speed
        else:
            bar2_y == circle_y + 7.5

    if bar1_y >= 420.:
        bar1_y = 420.
    elif bar1_y <= 10.:
        bar1_y = 10.
    if bar2_y >= 420.:
        bar2_y = 420.
    elif bar2_y <= 10.:
        bar2_y = 10.
    # since I don't know anything about collision, ball hitting bars goes like this.
    if circle_x <= bar1_x + 10.:
        if circle_y >= bar1_y - 7.5 and circle_y <= bar1_y + 42.5:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= bar2_x - 15.:
        if circle_y >= bar2_y - 7.5 and circle_y <= bar2_y + 42.5:
            circle_x = 605.
            speed_x = -speed_x
    if circle_x < 5.:
        bar2_score += 1
        circle_x, circle_y = 320., 232.5
        bar1_y, bar_2_y = 215., 215.
    elif circle_x > 620.:
        bar1_score += 1
        circle_x, circle_y = 307.5, 232.5
        bar1_y, bar2_y = 215., 215.
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    pygame.display.update()

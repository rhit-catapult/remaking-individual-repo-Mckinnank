import pygame
import sys

pygame.init()
pygame.display.set_caption("McKinnan")
screen = pygame.display.set_mode((1000, 800))
# TODO 05: Change the window size, make sure your circle code still works.

while True:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            sys.exit()

    # TODO 01: Make the background white by uncommenting the line below
    screen.fill(pygame.Color("Gray"))

    # Draw things on the screen

    # TODO 02: Try to draw a circle (any size, any color, anywhere)
    pygame.draw.circle(screen, pygame.Color("Yellow"), (50,50), 25)

    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    pygame.draw.circle(screen, pygame.Color("Red"), (screen.get_width() / 2, screen.get_height() / 2), 100)

    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    pygame.draw.circle(screen, (255, 255, 0), (0, screen.get_height()), 10)

    pygame.display.update()
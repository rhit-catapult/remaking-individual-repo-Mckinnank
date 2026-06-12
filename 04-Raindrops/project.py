import pygame
import sys
import time  # Note this!
import random  # Note this!
import cloud_module
import hero_module


def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # Done 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption("Rainy Day")
    # Done 2: Make a Clock
    clock = pygame.time.Clock()

    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    
    cloud = cloud_module.Cloud(screen, 300, 50, "Cloud.png")

    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    # Done 3: Enter the game loop, with a clock tick of 60 (or so) at each iteration.
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(pygame.Color("white"))  # white

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            cloud.y -= 10
        if pressed_keys[pygame.K_DOWN]:
            cloud.y += 10
        if pressed_keys[pygame.K_LEFT]:
            cloud.x -= 10
        if pressed_keys[pygame.K_RIGHT]:
            cloud.x += 10

        # Done 4:   Make the pygame.QUIT event stop the game.
        
        # 
        # Done 27: Inside the game loop (AFTER the events loop above), get the list of keys that are currently pressed.
        #     Arrange so that the Cloud moves:
        #       5 pixels (or 10 pixels) to the right if the Right Arrow key (pygame.K_RIGHT) is pressed.
        #       5 pixels (or 10 pixels) to the left  if the Left  Arrow key (pygame.K_LEFT)  is pressed.
        #       5 pixels (or 10 pixels) up           if the Up    Arrow key (pygame.K_UP)    is pressed.
        #       5 pixels (or 10 pixels) down         if the Down  Arrow key (pygame.K_DOWN)  is pressed.
        # DISCUSS: If you want something to happen once per key press, put it in the events loop above
        #          If you want something to continually happen while holding the key, put it after the events loop.

        # Done 5: Inside the game loop, draw the screen (fill with white)

        # Done 26: Draw the Cloud.
        cloud.draw()

        cloud.rain()
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()
                cloud.raindrops.remove(raindrop)
            if raindrop.off_screen():
                cloud.raindrops.remove(raindrop)

        # Done 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # Done: Make the Cloud "rain", then:
        # Doen    For each Raindrop in the Cloud's list of raindrops:
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # Done  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.

        # Done 18: Draw the Heroes (Mike and Alyssa)
        mike.draw()
        alyssa.draw()
        # Done 6: Update the display and remove the pass statement below
        pygame.display.update()
    


# Done 0: Call main.
main()

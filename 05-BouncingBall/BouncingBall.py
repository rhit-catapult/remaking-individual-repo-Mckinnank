import pygame
import sys
import random
import time


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball:
    def __init__(self, screen: pygame.Surface):
        self.radius = random.randint(20, 40)
        self.screen = screen
        self.x = random.randint(self.radius, screen.get_width() - self.radius)
        self.y = random.randint(self.radius, screen.get_height() - self.radius)
        
        self.color = (random.randint(0, 255), random.randint(0, 255),random.randint(0, 255))
        self.speed_x = random.randint(1, 5)
        self.speed_y = random.randint(1, 5)

    def draw(self):
        pygame.draw.circle (self.screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def bottom(self):
        return self.y > self.screen.get_height() - self.radius
    
    def top(self):
        return self.y < self.radius
    
    def right(self):
        return self.x > self.screen.get_width() - self.radius
    
    def left(self):
        return self.x < self.radius


num_balls = 50

def main():
    pygame.init()
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    balls = [Ball(screen) for _ in range(num_balls)]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        for ball in balls:
            ball.draw()
            ball.move()


            if ball.top():
                ball.speed_y = -ball.speed_y

            if ball.bottom():
                ball.speed_y = -ball.speed_y

            if ball.left():
                ball.speed_x = -ball.speed_x

            if ball.right(): 
                ball.speed_x = -ball.speed_x
            
        #ball.draw()
        #ball.move()



        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball

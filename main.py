# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen width: {SCREEN_HEIGHT}")
    # https://www.pygame.org/docs/ref/pygame.html#pygame.init
    pygame.init()
    # Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0), rect=None, special_flags=0)
        pygame.display.flip()

# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. 
if __name__ == "__main__":
    main()
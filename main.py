# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import player
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen width: {SCREEN_HEIGHT}")
    # https://www.pygame.org/docs/ref/pygame.html#pygame.init
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    # Use pygame's display.set_mode() to get a new GUI window:
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    game_loop(screen, clock, dt, player1)

def game_loop(screen, clock, dt, player1):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0), rect=None, special_flags=0)
        player1.update(dt)
        player1.draw(screen)
        dt = (clock.tick(60)/1000)
        pygame.display.flip()

# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. 
if __name__ == "__main__":
    main()
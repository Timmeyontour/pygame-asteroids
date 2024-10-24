# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
import player
import shot
import asteroid
import asteroidfield
from constants import *

# The Group class is a container that holds and manages multiple game objects. We can organize our objects into various groups to track them more easily.
updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()

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
    # setup group memberships (venn diagram)
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (shots, updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    player1 = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield1 = asteroidfield.AsteroidField()
    game_loop(screen, clock, dt, player1)

def game_loop(screen, clock, dt, player1):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0,0,0), rect=None, special_flags=0)
        dt = (clock.tick(60)/1000)

        for obj in updatable:
            obj.update(dt)
        
        for obj in asteroids:

            if obj.collCheck(player1):
                print("Game over")
                sys.exit()

            for bullet in shots:

                if bullet.collCheck(obj):
                    print("Coll detected")
                    obj.split()
                    bullet.kill()

        for obj in drawable:
            obj.draw(screen)

        # cls
        pygame.display.flip()

# This line ensures the main() function is only called when this file is run directly; 
# it won't run if it's imported as a module. It's considered the "pythonic" way to structure an executable program in Python. 
if __name__ == "__main__":
    main()
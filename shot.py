import pygame
import circleshape
from constants import SHOT_RADIUS

class Shot(circleshape.CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, (255,255,255), self.position, 2)

    def update(self, dt):
        self.position += self.velocity * dt
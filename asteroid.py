import pygame
from circleshape import CircleShape
import constants
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = self.velocity = pygame.Vector2(0, 0)
        
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
            
    def update(self, dt):
        self.position += self.velocity * dt
        
    def split(self):
        pygame.sprite.Sprite.kill(self)
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50) # nosec
            new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, random_angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -random_angle)*1.2
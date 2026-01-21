import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        # if the asteroid is large enough to split, log the event
        log_event("asteroid_split")

        split_angle = random.uniform(20, 50)

        first_asteroid_split = self.velocity.rotate(split_angle)
        second_asteroid_split = self.velocity.rotate(-split_angle)

        new_asteroid_radius = self.radius - ASTEROID_MIN_RADIUS
     
        new_asteroid_one = Asteroid(self.position.x,self.position.y, new_asteroid_radius)
        new_asteroid_two = Asteroid(self.position.x, self.position.y, new_asteroid_radius)

        new_asteroid_one.velocity = first_asteroid_split * 1.2
        new_asteroid_two.velocity = second_asteroid_split * 1.2

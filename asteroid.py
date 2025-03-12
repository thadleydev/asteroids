import circleshape
import pygame
import constants as c
import random


class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen, "white", (self.position.x, self.position.y), self.radius, 2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            first = Asteroid(
                self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS
            )
            second = Asteroid(
                self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS
            )
            first.velocity = self.velocity.rotate(angle)
            second.velocity = self.velocity.rotate(-angle)

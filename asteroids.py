from constants import *
from circleshape import *
import random


class Asteroids(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.happiness = 30

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        if self.happiness < 0:
            self.kill()
        self.happiness -= dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            return
        else:
            split_angle = random.uniform(20, 50)
            new_vector1 = self.velocity.rotate(-split_angle)
            new_vector2 = self.velocity.rotate(split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_astero1 = Asteroids(self.position.x, self.position.y, new_radius)
            new_astero2 = Asteroids(self.position.x, self.position.y, new_radius)

            new_astero1.velocity = new_vector1 * 1.2
            new_astero2.velocity = new_vector2 * 1.2

            self.kill()



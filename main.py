import pygame
import constants
import player as p
import asteroid as a
import asteroidfield as af
import shot as s
import sys


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {constants.SCREEN_WIDTH}")
    print(f"Screen height: {constants.SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    field = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    p.Player.containers = (drawable, updatable)
    a.Asteroid.containers = (asteroids, drawable, updatable)
    af.AsteroidField.containers = updatable
    s.Shot.containers = (shots, drawable, updatable)

    player = p.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
    af.AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        color = pygame.Color(0, 0, 0)
        pygame.Surface.fill(screen, color)
        updatable.update(dt)

        for item in drawable:
            item.draw(screen)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.check_collision(asteroid):
                    shot.kill()
                    asteroid.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()

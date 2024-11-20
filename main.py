import sys

import pygame

from asteroid import Asteroid
from asteroidField import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)

    AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("game over")
                sys.exit()

            for shot in shots:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        # limit the framerate to 144 FPS
        dt = clock.tick(144) / 1000


if __name__ == "__main__":
    main()

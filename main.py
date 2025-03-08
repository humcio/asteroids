import pygame
from constants import *
from player import *
from asteroids import *
from asteroidfield import *
from shooting import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroidsGroup = pygame.sprite.Group()
    backshots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroids.containers = (asteroidsGroup, drawable, updatable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, backshots)
    




    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    playerUnit = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    new_field = AsteroidField()
    #################### MAIN LOOP STARTS HERE ############################

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        
        for item in drawable:
            item.draw(screen)


        updatable.update(dt)

        for astero in asteroidsGroup:
            if astero.collision(playerUnit) is True:
                print("Game Over!")
                sys.exit()
        for astero in asteroidsGroup:
            for backshot in backshots:
                if astero.collision(backshot):
                    astero.split()
                    backshot.kill()





        #playerUnit.draw(screen)
        #playerUnit.update(dt)


        pygame.display.flip()
        dt = clock.tick(60)/1000
        
        











if __name__ == "__main__":
    main()
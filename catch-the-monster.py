import pygame
import random

from hero import Hero
from monster import Monster

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275




def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch The Monster!')
    clock = pygame.time.Clock()

    monster = Monster('images/monster.png', 100, 100)
    hero = Hero('images/hero.png', 255, 235)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    
    # Game initialization

    stop_game = False

    while not stop_game:

        # Monster Movement 
        """
         move this logic into a method of the monster class
         and call that method here

        """
        if monster.x > width:
            monster.x = 0
        if monster.y > height:
            monster.y = 0
        if monster.x < 0:
            monster.x = width
        if monster.y < 0:
            monster.y = height


        for event in pygame.event.get():
        # Hero movement from keyboard keys

            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero.key_direction_y = 4
                elif event.key == KEY_UP:
                    hero.key_direction_y = -4
                if event.key == KEY_LEFT:
                    hero.key_direction_x = -4
                elif event.key == KEY_RIGHT:
                    hero.key_direction_x = 4
            elif event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    hero.key_direction_y = 0
                elif event.key == KEY_UP:
                    hero.key_direction_y = 0
                if event.key == KEY_LEFT:
                    hero.key_direction_x = 0
                elif event.key == KEY_RIGHT:
                    hero.key_direction_x = 0

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        monster.move_and_loop(width, height)
        monster.determine_new_direction()
        hero.move_position()
        hero.confine_to_bushes(width, height, 62, 32)
        if hero.collision(32, monster):
            print("collision!")

        # Game display
        screen.blit(background_image, (0,0))
        monster.render(screen)
        hero.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

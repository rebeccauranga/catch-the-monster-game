import pygame
import random

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    monster_x = 100
    monster_y = 100

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch The Monster!')
    clock = pygame.time.Clock()
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()
    change_dir_countdown = 120
    change_direction = 1
    x_dir = 3
    y_dir = 3


    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
    
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        # monster_x += 5
        # monster_y += 5
        # monster_x -= 5
        # monster_y -= 5

        if monster_x > width:
            monster_x = 0
        if monster_y > height:
            monster_y = 0
        if monster_x < 0:
            monster_x = width
        if monster_y < 0:
            monster_y = width

        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            change_dir_countdown = 120
            change_direction = random.randint(0,3)
            print(change_direction)
        if change_direction == 0:
            monster_x += x_dir
        elif change_direction == 1:
            monster_y += y_dir
        elif change_direction == 2:
            monster_x -= x_dir
        elif change_direction == 3:
            monster_y -= y_dir

        # Draw background
        screen.fill(blue_color)

        # Game display

        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (250,235))
        screen.blit(monster_image, (monster_x, monster_y))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

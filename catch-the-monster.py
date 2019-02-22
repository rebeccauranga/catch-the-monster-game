import pygame
import random

class Monster:
    def __init__(self, image_path, x, y, change_dir_countdown, change_direction, x_dir, y_dir):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.change_dir_countdown = change_dir_countdown
        self.change_direction = change_direction
        self.x_dir = x_dir
        self.y_dir = y_dir

    def move_and_loop(self, width, height):
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = width

    def determine_new_direction(self):
        self.change_dir_countdown -= 1
        if self.change_dir_countdown == 0:
            self.change_dir_countdown = 120
            self.change_direction = random.randint(0,3)
        if self.change_direction == 0:
            self.x += self.x_dir
        elif self.change_direction == 1:
            self.y += self.y_dir
        elif self.change_direction == 2:
            self.x -= self.x_dir
        elif self.change_direction == 3:
            self.y -= self.y_dir
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))


def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch The Monster!')
    clock = pygame.time.Clock()
    monster = Monster('images/monster.png', 100, 100, 120, 1, 3, 3)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
    
            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic
        
            monster.move_and_loop(width, height)
            monster.determine_new_direction()


        # Game display
        screen.blit(background_image, (0,0))
        screen.blit(hero_image, (250,235))
        monster.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

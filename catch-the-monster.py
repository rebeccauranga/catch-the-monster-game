import pygame
import random

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

class Monster:
    def __init__(self, image_path, x, y, countdown_number, change_direction, x_dir, y_dir):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.countdown_number = countdown_number
        self.change_direction = change_direction
        self.x_dir = x_dir
        self.y_dir = y_dir

    def move_and_loop(self, width, height):
        self.x += self.x_dir  
        self.y += self.y_dir
        self.x -= self.x_dir  
        self.y -= self.y_dir

    # def determine_new_direction(self):
    
    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

class Hero: 
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y
        self.key_direction_x = 0
        self.key_direction_y = 0

    def move_position(self):
        self.x += self.key_direction_x
        self.y += self.key_direction_y

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Catch The Monster!')
    clock = pygame.time.Clock()
    monster = Monster('images/monster.png', 100, 100, 120, 1, 5, 5)
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero = Hero('images/hero.png', 255, 235)
    
    # Game initialization

    stop_game = False

    while not stop_game:

        # Monster Movement 
        if monster.x > width:
            monster.x = 0
        if monster.y > height:
            monster.y = 0
        if monster.x < 0:
            monster.x = width
        if monster.y < 0:
            monster.y = width

            monster.countdown_number -= 1
        if monster.countdown_number == 0:
            monster.countdown_number = 120
            monster.change_direction = random.randint(0,3)
        if monster.change_direction == 0:
            monster.x += monster.x_dir
        elif monster.change_direction == 1:
            monster.y += monster.y_dir
        elif monster.change_direction == 2:
            monster.x -= monster.x_dir
        elif monster.change_direction == 3:
            monster.y -= monster.y_dir


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
        # monster.determine_new_direction(1)
        hero.move_position()

        # Game display
        screen.blit(background_image, (0,0))
        monster.render(screen)
        hero.render(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()

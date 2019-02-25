import pygame
from hero import Hero
from monster import Monster

width = 512
height = 480

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Catch The Monster!')
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.sound = pygame.mixer.Sound('sounds/win.wav')
        self.hero = Hero('images/hero.png', 255, 235)
        self.monster = Monster('images/monster.png', 100, 100)
        self.background_image = pygame.image.load('images/background.png').convert_alpha()
        self.game_over = False

    def start(self):
        while not self.game_over:
            self.monster.return_to_screen(width, height)
            for event in pygame.event.get():
                self.handle_event(event)

            self.monster.move_and_loop(width, height)
            self.monster.determine_new_direction()
            self.hero.move_position()
            self.hero.confine_to_bushes(width, height, 62, 32)
            if self.hero.collision(32, self.monster):
                self.sound.play()
                self.monster.dead = True
                print("collision!")

            # Game display
            self.screen.blit(self.background_image, (0,0))
            if not self.monster.dead:
                self.monster.render(self.screen)
            self.hero.render(self.screen)
            self.clock.tick(60)
            pygame.display.update()

        pygame.quit()

    def handle_event(self, event):
        KEY_UP = 273
        KEY_DOWN = 274
        KEY_LEFT = 276
        KEY_RIGHT = 275

        if event.type == pygame.KEYDOWN:
            if event.key == KEY_DOWN:
                self.hero.key_direction_y = 4
            elif event.key == KEY_UP:
                self.hero.key_direction_y = -4
            if event.key == KEY_LEFT:
                self.hero.key_direction_x = -4
            elif event.key == KEY_RIGHT:
                self.hero.key_direction_x = 4
        elif event.type == pygame.KEYUP:
            if event.key == KEY_DOWN:
                self.hero.key_direction_y = 0
            elif event.key == KEY_UP:
                self.hero.key_direction_y = 0
            if event.key == KEY_LEFT:
                self.hero.key_direction_x = 0
            elif event.key == KEY_RIGHT:
                self.hero.key_direction_x = 0

        if event.type == pygame.QUIT:
                self.game_over = True


if __name__ == "__main__":
    game = Game()
    game.start()


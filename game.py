import pygame
import random
from hero import Hero
from monster import Monster
from goblin import Goblin

width = 512
height = 480
black_color = (0, 0, 0)

class Game:
    def __init__(self):
        self.wins = 0
        self.init_new_game()

    def init_new_game(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Catch The Monster!')
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.winning_sound = pygame.mixer.Sound('sounds/win.wav')
        self.losing_sound = pygame.mixer.Sound('sounds/lose.wav')
        self.game_music = pygame.mixer.Sound('sounds/music.wav')
        self.hero = Hero('images/hero.png', 255, 235)
        self.monster = Monster('images/monster.png', random.randint(20, width-20), random.randint(20, height-20))
        self.create_goblins()
        self.background_image = pygame.image.load('images/background.png').convert_alpha()
        self.wins += 1
        self.game_over = False

    def create_goblins(self):
        self.goblins = []
        for i in range(0, self.wins + 1):
            self.goblins.append(Goblin('images/goblin.png', random.randint(20, width-20), random.randint(20, height-20)))

    def start(self):
        self.game_music.play()
        while not self.game_over:
            self.monster.return_to_screen(width, height)
            for event in pygame.event.get():
                self.handle_event(event)

            self.monster.move_and_loop(width, height)
            self.monster.determine_new_direction()
            self.hero.move_position()
            self.hero.confine_to_bushes(width, height, 62, 32)

            if not self.monster.dead and self.hero.collision(32, self.monster):
                self.winning_sound.play()
                self.monster.dead = True
                print("collision!")

            # Game display
            self.screen.blit(self.background_image, (0,0))
            # self.hero.render(self.screen)
            if not self.monster.dead:
                self.monster.render(self.screen)
            else:
                font = pygame.font.Font(None, 32)
                text = font.render('You win! Press ENTER to play again.', True, (0, 0, 0))
                self.screen.blit(text, (60, 230))

            for goblin in self.goblins: 
                goblin.move_and_loop(width, height)
                goblin.determine_new_direction()
                goblin.render(self.screen)
                if self.hero.collision(32, goblin):
                    self.hero.dead = True
                    self.losing_sound.play()
                if not self.hero.dead:
                    self.hero.render(self.screen)
                else:
                    goblin.offscreen_goblin()
                    self.monster.offscreen_monster()
                    self.monster.alive_and_move = False
                    font = pygame.font.Font(None, 32)
                    text = font.render('You lose! Press ENTER to play again.', True, (0, 0, 0))
                    self.screen.blit(text, (60, 230))
                
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
            elif event.key == pygame.K_RETURN:
                # self.wins += 1
                self.init_new_game()
                
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


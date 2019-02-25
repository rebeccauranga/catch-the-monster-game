import pygame

class Character:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.image, (self.x, self.y))

    

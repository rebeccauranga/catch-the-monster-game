import pygame
from character import Character

class Hero(Character): 
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.key_direction_x = 0
        self.key_direction_y = 0

    def move_position(self):
        self.x += self.key_direction_x
        self.y += self.key_direction_y

    def confine_to_bushes(self, width, height, pic_and_pixels, pic_size):
        if self.x >= (width - pic_and_pixels):
            self.x = (width - pic_and_pixels)
        if self.y >= (height - pic_and_pixels):
            self.y = (height - pic_and_pixels)
        if self.x <= pic_size:
            self.x = pic_size
        if self.y <= pic_size:
            self.y = pic_size

    def collision(self, pic_size, player2):
        if player2.x + pic_size < self.x:
            return False
        elif self.x + pic_size < player2.x:
            return False
        elif player2.y + pic_size < self.y:
            return False
        elif self.y + pic_size < player2.y:
            return False
        else: 
            return True



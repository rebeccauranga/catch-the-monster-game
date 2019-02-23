import pygame
import random
from character import Character

class Monster(Character):
    def __init__(self, image_path, x, y):
        super().__init__(image_path, x, y)
        self.countdown_number = 15
        self.change_direction = 1
        self.x_dir = 7
        self.y_dir = 7

    def move_and_loop(self, width, height):
        self.x += self.x_dir  
        self.y += self.y_dir
        self.x -= self.x_dir  
        self.y -= self.y_dir

    def determine_new_direction(self):
        self.countdown_number -= 1
        if self.countdown_number == 0:
            self.countdown_number = 15
            self.change_direction = random.randint(0, 3)
        if self.change_direction == 0:
            self.x += self.x_dir
        elif self.change_direction == 1:
            self.y += self.y_dir
        elif self.change_direction == 2:
            self.x -= self.x_dir
        elif self.change_direction == 3:
            self.y -= self.y_dir

    def return_to_screen(self, width, height):
        if self.x > width:
            self.x = 0
        if self.y > height:
            self.y = 0
        if self.x < 0:
            self.x = width
        if self.y < 0:
            self.y = height
    
import os
import pygame
import math

from settings import Settings


class Ball:
    def __init__(self, position_x, position_y):
        self.settings = Settings()
        self.image = pygame.image.load(os.path.join("gfx", "ball.png"))
        self.rect = pygame.Surface.get_rect(self.image)
        self.position_x = position_x - self.rect[2] / 2
        self.position_y = position_y - self.rect[3] / 2
        self.speed = 200.0
        self.direction_x = 1
        self.direction_y = 1

    def draw(self, screen):
        screen.blit(self.image, (self.position_x, self.position_y))

    def update_ball(self, time_delta):
        self.check_ball_position()
        self.position_x += self.speed * time_delta * self.direction_x
        self.position_y += self.speed * time_delta * self.direction_y

    def check_ball_position(self):
        if self.position_x < 0 or self.position_x >= self.settings.width:
            self.direction_x *= -1
        if self.position_y < 0 or self.position_y >= self.settings.height:
            self.direction_y *= -1

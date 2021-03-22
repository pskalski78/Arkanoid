import pygame

from ball import Ball
from settings import Settings


class Game:
    def __init__(self):
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.width, self.settings.height)
        )
        print(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.time_delta = 0
        self.done = False
        self.ball = Ball(self.settings.width / 2, self.settings.height / 2)
        pygame.init()
        pygame.display.set_caption("Arkanoid")

    def draw(self):
        self.screen.fill((0, 222, 255))
        self.ball.draw(self.screen)
        self.time_delta = self.clock.tick(self.fps) / 1000
        self.ball.update_ball(self.time_delta)
        pygame.display.flip()

    def eventLoop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def main_loop(self):
        while not self.done:
            self.eventLoop()
            self.draw()
        pygame.quit()

    def run(self):
        self.main_loop()

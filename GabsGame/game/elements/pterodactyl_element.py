from pygame import Surface
from game.entities.obstacle_base import Obstacle

class Bird(Obstacle):
    def __init__(self, image, game_speed: int):
        self.type = 0
        super().__init__(image, self.type, game_speed=game_speed)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN: Surface):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
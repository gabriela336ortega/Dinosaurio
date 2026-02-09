import random
from game.entities.obstacle_base import Obstacle

class LargeCactus(Obstacle):
    def __init__(self, image, game_speed: int):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type, game_speed=game_speed)
        self.rect.y = 300
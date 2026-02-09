from pygame import Surface, Rect
from game.settings import GameSettings

class Obstacle:
    def __init__(self, image: Surface, type, game_speed: int):
        self.image = image
        self.type = type
        self.game_speed = game_speed
        self.rect: Rect = self.image[self.type].get_rect()
        self.rect.x = GameSettings.SCREEN_WIDTH

    def update(self: int):
        self.rect.x -= self.game_speed
        if self.rect.x < -self.rect.width:
            return True
        return False

    def draw(self, SCREEN: Surface):
        SCREEN.blit(self.image[self.type], self.rect)
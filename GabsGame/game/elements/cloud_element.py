import random
from pygame import Surface
from game.settings import GameSettings

class Cloud:
    def __init__(self, game_speed: int):
        self.x: int = GameSettings.SCREEN_WIDTH + random.randint(800, 1000)
        self.y: int = random.randint(50, 100)
        self.image = GameSettings.CLOUD
        self.width = self.image.get_width()
        self.game_speed = game_speed

    def update(self):
        self.x -= self.game_speed
        if self.x < -self.width:
            self.x = GameSettings.SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN: Surface):
        """
        Dibuja el objeto en la pantalla.

        Args:
            SCREEN (Surface): La superficie en la que se dibujará el objeto.
        """
        SCREEN.blit(self.image, (self.x, self.y))
    
    def get_rect(self):
        """
        Obtiene el rectángulo delimitador del objeto.

        Returns:
            pygame.Rect: El rectángulo delimitador del objeto.
        """
        return self.image.get_rect(topleft=(self.x, self.y))
import pygame
import random
from game.entities.obstacle_base import Obstacle

class DownPterodactyl(Obstacle):
    """Pterodáctilo que baja para joder de vez en cuando"""
    
    def __init__(self, image, game_speed):
        self.image = image
        self.rect = image[0].get_rect()
        self.rect.x = 570
        self.rect.y = 250
        self.game_speed = game_speed
        self.index = 0
        
        # Solo 3 variables para el ataque
        self.altura_normal = self.rect.y
        self.atacando = False
        self.tiempo_ataque = random.randint(60, 120)
    
    def update(self):
        # Se mueve hacia la izquierda
        self.rect.x -= self.game_speed
        
        # Lógica simple de ataque
        self.tiempo_ataque -= 1
        
        if self.tiempo_ataque <= 0 and not self.atacando:
            self.atacando = True
            self.tiempo_ataque = random.randint(60, 120)
        
        if self.atacando:
            if self.rect.y < 325:  # Baja hasta el suelo
                self.rect.y += 10
            else:
                self.atacando = False
                self.rect.y = self.altura_normal  # Vuelve arriba
        
        # ¿Sale de pantalla?
        return self.rect.x < -self.rect.width
    
    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index//5], self.rect)
        self.index += 1
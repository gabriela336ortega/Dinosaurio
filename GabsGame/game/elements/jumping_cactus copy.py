import pygame
import random
from game.entities.obstacle_base import Obstacle

class JumpingCactus(Obstacle):
    """Cactus que salta para hacer trampas más difíciles"""
    
    def __init__(self, image, game_speed: int):
        super().__init__(image, 0, game_speed)
        
        # Posiciones iniciales (puede aparecer en 3 alturas)
        self.ground_y = 325  # Posición normal en suelo
        self.jump_y = 250    # Posición en salto
        self.current_y = self.ground_y
        self.rect.y = self.current_y
        
        # Variables de salto
        self.is_jumping = False
        self.jump_timer = 0
        self.jump_cooldown = random.randint(30, 90)  # Frames hasta próximo salto
        self.jump_duration = random.randint(20, 40)  # Frames que dura el salto
        
        # Animación de salto
        self.jump_velocity = 15
        self.current_height = 0
        
    def update(self):
        """Actualiza posición y lógica de salto"""
        # Movimiento horizontal normal
        self.rect.x -= self.game_speed
        
        # Lógica de salto
        if not self.is_jumping:
            self.jump_cooldown -= 1
            if self.jump_cooldown <= 0:
                self.start_jump()
        else:
            self.update_jump()
        
        # Retornar True si debe eliminarse (salió de pantalla)
        return self.rect.x < -self.rect.width
    
    def start_jump(self):
        """Inicia un salto"""
        self.is_jumping = True
        self.jump_timer = self.jump_duration
        self.current_height = 0
        print("🦘 ¡Cactus saltarín activado!")
    
    def update_jump(self):
        """Actualiza la física del salto"""
        self.jump_timer -= 1
        
        # Física simple del salto (parábola)
        if self.jump_timer > self.jump_duration // 2:
            # Subiendo
            self.current_height += self.jump_velocity
        else:
            # Bajando
            self.current_height -= self.jump_velocity
        
        # Aplicar altura al rectángulo
        self.rect.y = self.ground_y - self.current_height
        
        # Terminar salto
        if self.jump_timer <= 0:
            self.is_jumping = False
            self.jump_cooldown = random.randint(30, 90)
            self.rect.y = self.ground_y
            self.current_height = 0
    
    def draw(self, SCREEN):
        """Dibuja el cactus con efecto de salto"""
        # Dibujar sombra cuando salta
        if self.is_jumping:
            shadow = pygame.Surface((self.rect.width, 10), pygame.SRCALPHA)
            shadow.fill((0, 0, 0, 100))
            SCREEN.blit(shadow, (self.rect.x, self.ground_y + 10))
        
        # Dibujar cactus
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
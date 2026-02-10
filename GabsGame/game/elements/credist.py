import pygame
from game.settings.game_settings import GameSettings

def show_credits():
    """Versión simple de créditos"""
    credits_data = [
        ("DINO", 48, (255, 255, 0)),
        ("Desarrollado por 3M", 32, (255, 255, 255)),
        ("", 24, (255, 255, 255)),
        ("Programado en Python + Pygame", 28, (200, 200, 255)),
        ("Inspirado en el Dinosaurio de Chrome, cualquier parecido con realidad es pura coincidencia", 24, (200, 255, 200)),
        ("Presiona ESC para volver", 22, (150, 150, 255))
    ]
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return
        
        # Fondo
        GameSettings.SCREEN.fill((20, 20, 40))
        
        # Dibujar créditos centrados
        y = 50
        for text, size, color in credits_data:
            font = pygame.font.Font(None, size)
            surface = font.render(text, True, color)
            rect = surface.get_rect(center=(GameSettings.SCREEN_WIDTH//2, y))
            GameSettings.SCREEN.blit(surface, rect)
            y += size + 5
        
        pygame.display.update()
        pygame.time.delay(50)
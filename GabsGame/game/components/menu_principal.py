import pygame
from game.settings import GameSettings

def mostrar_menu_principal(screen):
    """
    Función que muestra el menú principal
    """
    run = True
    while run:
        # Fondo
        screen.fill((40, 40, 60))
        
        # Título del juego
        titulo_font = pygame.font.SysFont('Arial', 72, bold=True)
        titulo = titulo_font.render("DINO RUNNER", True, (255, 200, 0))
        screen.blit(titulo, (GameSettings.SCREEN_WIDTH//2 - titulo.get_width()//2, 100))
        
        
        # Instrucciones principales
        fuente = pygame.font.SysFont('Arial', 36)
        
        opciones = [
            "Presiona ESPACIO para comenzar",
            "Presiona C para Créditos",
            "Presiona ESC para salir"
        ]
        
        y = 300
        for opcion in opciones:
            texto = fuente.render(opcion, True, (255, 255, 255))
            screen.blit(texto, (GameSettings.SCREEN_WIDTH//2 - texto.get_width()//2, y))
            y += 50
        
        # Información adicional
        peque_font = pygame.font.SysFont('Arial', 20)
        info = peque_font.render("Usa las flechas o SPACE para saltar obstáculos", True, (180, 180, 180))
        screen.blit(info, (GameSettings.SCREEN_WIDTH//2 - info.get_width()//2, GameSettings.SCREEN_HEIGHT - 80))

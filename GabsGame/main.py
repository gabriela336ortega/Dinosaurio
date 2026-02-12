import pygame
import os
import random

pygame.init()

from game.settings import GameSettings
from game.components import mostrar_menu_principal
from game.elements import Cloud, Dinosaur, LargeCactus, SmallCactus, Bird, JumpingCactus, DownPterodactyl, show_credits

#FUNCIÓN DE PRUEBA PARA EL JUEGO.
screen = pygame.display.set_mode(GameSettings.SCREEN)
def main(screen=screen):
    
    if GameSettings.SCREEN is None:
        pygame.init()
        GameSettings.SCREEN = pygame.display.set_mode(
            (GameSettings.SCREEN_WIDTH, GameSettings.SCREEN_HEIGHT)
        )
        pygame.display.set_caption(GameSettings.SCREEN_TITLE) 
    
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    game_speed=1
    clock = pygame.time.Clock()
    player = Dinosaur()
    cloud = Cloud(game_speed=game_speed)
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    last_obstacle_time = pygame.time.get_ticks()
    

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        screen.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = GameSettings.BG.get_width()
        screen.blit(GameSettings.BG, (x_pos_bg, y_pos_bg))
        screen.blit(GameSettings.BG, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            screen.blit(GameSettings.BG, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.fill((255, 255, 255))
       
        obstacle_timer = 0 #Y SI LO BORRO Y EXPLOTA?
        obstacle_frequency = 1500
        current_time = pygame.time.get_ticks()

        if current_time - last_obstacle_time > obstacle_frequency:
            obstacle_type = random.randint(0, 4)

            if obstacle_type == 0:
                obstacles.append(SmallCactus(GameSettings.SMALL_CACTUS, game_speed))
            elif obstacle_type == 1:
                obstacles.append(LargeCactus(GameSettings.LARGE_CACTUS, game_speed))
            elif obstacle_type == 2:
                obstacles.append(JumpingCactus(GameSettings.JUMPING_CACTUS, game_speed))
            elif obstacle_type == 3:
                obstacles.append(DownPterodactyl(GameSettings.DOWN_PTERODACTIL, game_speed))
            else:
                obstacles.append(Bird(GameSettings.PTERODACTIL, game_speed))
            
            last_obstacle_time = current_time
            obstacle_frequency = random.randint(1000, 2500)
        
        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                player.dead()
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count, screen=screen)

        background()
        score()
        userInput = pygame.key.get_pressed()
        player.draw(screen)
        player.update(userInput)
        cloud.draw(screen)
        cloud.update()
        clock.tick(30)
        
        
        pygame.display.update()
        

def menu(death_count, screen):
    global points
    run = True
    while run:
        screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("¿Quieres seguir perdiendo? Persiona cualquier tecla", True, (0, 0, 0))

        elif death_count > 0:
            text = font.render("¿Quieres seguir perdiendo? Persiona cualquier tecla", True, (0, 0, 0))
            score = font.render("Tu récord: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (GameSettings.SCREEN_WIDTH // 2, GameSettings.SCREEN_HEIGHT // 2 + 50)
            screen.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (GameSettings.SCREEN_WIDTH // 2, GameSettings.SCREEN_HEIGHT // 2)
        screen.blit(text, textRect)
        screen.blit(GameSettings.RUNNING[0], (GameSettings.SCREEN_WIDTH // 2 - 20, GameSettings.SCREEN_HEIGHT // 2 - 140))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.KEYDOWN:
                main(screen=screen)
#mostrar_menu_principal(screen=screen)
menu(death_count = 0, screen=screen)
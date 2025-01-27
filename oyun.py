import pygame
import time
import random
import pyautogui
# Pygame'i başlat
pygame.init()
# Ekran boyutları
x,y = pyautogui.size()
WIDTH, HEIGHT = x,y
BLOCK_SIZE = 20
# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Oyun ekranını oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")
# Saat
clock = pygame.time.Clock()
# Yılan ve oyun ayarları
snake_speed = 15
def snake(block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, block_size, block_size])
def game_loop():
    game_over = False
    game_close = False
    # Başlangıç pozisyonları
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    # Rastgele yem konumu
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            font_style = pygame.font.SysFont("comicsansms", 35)
            message = font_style.render("kaybettin c tekrar oyna-q çık", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = BLOCK_SIZE
        # Yılan ekranın dışına çıkarsa
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        # Yemi çiz
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        # Yılanın hareketi
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # Yılan kendine çarparsa
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        snake(BLOCK_SIZE, snake_list)
        # Yem yeme kontrolü
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    quit()
if __name__ == "__main__":
    game_loop()
import pygame
import time
import random
# Pygame'i başlat
pygame.init()
# Ekran boyutları
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
# Renkler
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Oyun ekranını oluştur
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Yılan Oyunu")
# Saat
clock = pygame.time.Clock()
# Yılan ve oyun ayarları
snake_speed = 15
def snake(block_size, snake_list):
    for x, y in snake_list:
        pygame.draw.rect(screen, GREEN, [x, y, block_size, block_size])
def game_loop():
    game_over = False
    game_close = False
    # Başlangıç pozisyonları
    x1 = WIDTH // 2
    y1 = HEIGHT // 2
    x1_change = 0
    y1_change = 0
    snake_list = []
    length_of_snake = 1
    # Rastgele yem konumu
    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
    while not game_over:
        while game_close:
            screen.fill(BLACK)
            font_style = pygame.font.SysFont("comicsansms", 35)
            message = font_style.render("kaybettin c tekrar oyna-q çık", True, RED)
            screen.blit(message, [WIDTH / 6, HEIGHT / 3])
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -BLOCK_SIZE
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = BLOCK_SIZE
        # Yılan ekranın dışına çıkarsa
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(BLACK)
        # Yemi çiz
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        # Yılanın hareketi
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        # Yılan kendine çarparsa
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True
        snake(BLOCK_SIZE, snake_list)
        # Yem yeme kontrolü
        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 20.0) * 20.0
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 20.0) * 20.0
            length_of_snake += 1
        pygame.display.update()
        clock.tick(snake_speed)
    pygame.quit()
    quit()
if __name__ == "__main__":
    game_loop()
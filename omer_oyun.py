import pygame
import random

# Pygame'i başlat
pygame.init()

# Ekran boyutu
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basit Minecraft Tarzı Oyun")

# Renkler
WHITE = (255, 255, 255)
GREEN = (34, 177, 76)
BROWN = (139, 69, 19)
BLUE = (50, 153, 213)

# Blok boyutu
BLOCK_SIZE = 40

# Ekranda yer alacak bloklar (2D liste)
blocks = []

# Yılanın vücut kısmı
player_x = WIDTH // 2
player_y = HEIGHT - 60
player_width = 40
player_height = 40
player_color = (255, 0, 0)

# Ekranda yer alacak blokları oluşturma fonksiyonu
def create_blocks():
    for y in range(HEIGHT // BLOCK_SIZE - 1, HEIGHT // BLOCK_SIZE - 10, -1):  # Zemin için bloklar
        for x in range(0, WIDTH // BLOCK_SIZE):
            blocks.append(pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

# Blokları çizme fonksiyonu
def draw_blocks():
    for block in blocks:
        pygame.draw.rect(screen, BROWN, block)

# Ana oyun döngüsü
def gameLoop():
    running = True
    clock = pygame.time.Clock()
    player_speed = 5
    player_x, player_y = 100, 100  # Initialize player position
    create_blocks()  # Zemin bloklarını oluştur

    while running:
        screen.fill(WHITE)  # Ekranı temizle
        draw_blocks()  # Blokları çiz

        # Oyuncu hareketi
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= player_speed
        if keys[pygame.K_RIGHT]:
            player_x += player_speed
        if keys[pygame.K_DOWN]:
            player_y += player_speed
        if keys[pygame.K_UP]:
            player_y -= player_speed

        # Update the display
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    gameLoop()
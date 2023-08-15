import pygame
import sys
from pygame.locals import *

pygame.init()

# Configuración del display
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LABERINTO")

colorCuadros = (241, 155, 163)
colorFondo = (251, 213, 221)

# Nacimiento de Hello Kitty
HelloKitty = pygame.image.load("HelloKitty.png")
HelloKitty = pygame.transform.scale(HelloKitty, (70, 70))
HelloKittyRect = HelloKitty.get_rect()
HelloKittyRect.center = (300, 30)
move_speed = 2

# Fresa
Fresa = pygame.image.load("fresa.png")
Fresa = pygame.transform.scale(Fresa, (60, 60))
FresaRect = Fresa.get_rect()
FresaRect.center = (290, 560)

# Definir los rectángulos de las paredes del laberinto
paredes = [
    pygame.Rect(10, 10, 15, 575),
    pygame.Rect(10, 10, 235, 15),
    pygame.Rect(335, 10, 250, 15),
    pygame.Rect(575, 10, 15, 575),
    pygame.Rect(10, 575, 235, 15),
    pygame.Rect(335, 575, 250, 15),
    pygame.Rect(10, 100, 100, 15),
    pygame.Rect(448, 10, 15, 200),
    pygame.Rect(235, 440, 15, 150),
    pygame.Rect(120, 325, 460, 15),
    pygame.Rect(120, 250, 15, 180),
    pygame.Rect(225, 100, 15, 230),
    pygame.Rect(225, 100, 130, 15),
    pygame.Rect(345, 100, 15, 115)
]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        new_rect = HelloKittyRect.move(0, -move_speed)
        if all(not new_rect.colliderect(pared) for pared in paredes):
            HelloKittyRect = new_rect
    if keys[pygame.K_s]:
        new_rect = HelloKittyRect.move(0, move_speed)
        if all(not new_rect.colliderect(pared) for pared in paredes):
            HelloKittyRect = new_rect
    if keys[pygame.K_a]:
        new_rect = HelloKittyRect.move(-move_speed, 0)
        if all(not new_rect.colliderect(pared) for pared in paredes):
            HelloKittyRect = new_rect
    if keys[pygame.K_d]:
        new_rect = HelloKittyRect.move(move_speed, 0)
        if all(not new_rect.colliderect(pared) for pared in paredes):
            HelloKittyRect = new_rect

    # Verificar colision con la fresa
    if HelloKittyRect.colliderect(FresaRect):
        pygame.quit()
        sys.exit()

    DISPLAYSURF.fill(colorFondo)

    # Dibujar las paredes del laberinto
    for pared in paredes:
        pygame.draw.rect(DISPLAYSURF, colorCuadros, pared)

    DISPLAYSURF.blit(HelloKitty, HelloKittyRect)
    DISPLAYSURF.blit(Fresa, FresaRect)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

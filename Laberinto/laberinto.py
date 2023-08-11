import pygame
from pathlib import Path
import sys
from pygame.locals import *

pygame.init()

# configuracion del display
DISPLAYSURF = pygame.display.set_mode((600, 600))
pygame.display.set_caption("LABERINTO")

colorCuadros = (241, 155, 163)
colorFondo = (251, 213, 221)

# Nacimiento de Hello Kitty
HelloKitty = pygame.image.load("Laberinto/HelloKitty.png")
HelloKitty = pygame.transform.scale(HelloKitty, (70, 70))
HelloKittyRect = HelloKitty.get_rect()
HelloKittyRect.center = (300, 30)
move_speed = 2

# Fresa
Fresa = pygame.image.load("Laberinto/fresa.png")
Fresa = pygame.transform.scale(Fresa, (60, 60))
FresaRect = Fresa.get_rect()
FresaRect.center = (290, 560)
# Teclas y movimiento
while True: 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        HelloKittyRect.y -= move_speed
    if keys[pygame.K_s]:
        HelloKittyRect.y += move_speed
    if keys[pygame.K_a]:
        HelloKittyRect.x -= move_speed
    if keys[pygame.K_d]:
        HelloKittyRect.x += move_speed

    # Verificar colision con la fresa
    if HelloKittyRect.colliderect(FresaRect):
        pygame.quit()
        sys.exit()

    DISPLAYSURF.fill(colorFondo)

    # Dibujar las paredes del laberinto
    cuadro01 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (10, 10, 15, 575))
    cuadro02 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (10, 10, 235, 15))
    cuadro03 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (335, 10, 250, 15))
    cuadro04 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (575, 10, 15, 575))
    cuadro05 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (10, 575, 235, 15))
    cuadro06 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (335, 575, 250, 15))
    cuadro07 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (10, 100, 100, 15))
    cuadro08 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (448, 10, 15, 200))
    cuadro09 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (235, 440, 15, 150))
    cuadro10 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (235, 425, 225, 15))
    cuadro11 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (120, 325, 460, 15))
    cuadro12 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (120, 250, 15, 180))
    cuadro13 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (225, 100, 15, 230))
    cuadro14 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (225, 100, 130, 15))
    cuadro15 = pygame.draw.rect(DISPLAYSURF, colorCuadros, (345, 100, 15, 115))

    DISPLAYSURF.blit(HelloKitty, HelloKittyRect)
    DISPLAYSURF.blit(Fresa, FresaRect)
    pygame.display.flip()
    
    pygame.time.Clock().tick(60)

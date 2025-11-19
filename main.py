import pygame
from map import HeatMap
from gui_fire import render_heatmap

pygame.init()

# Fenstergröße
HEIGHT = 40
WIDTH = 40
PIXEL = 8  # jedes HeatMap-Feld wird ein 8×8-Block

screen = pygame.display.set_mode((WIDTH * PIXEL, HEIGHT * PIXEL))
pygame.display.set_caption("FireAnneal")

# HeatMap erzeugen
fire = HeatMap(HEIGHT, WIDTH)
fire.fill_random()

T = 1.0

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Annealing Schritt
    fire, _ = HeatMap.annealing_step(fire, T)
    T = HeatMap.cool(T, 0.999)

    # Rendering
    render_heatmap(screen, fire, PIXEL)

    pygame.display.flip()
    clock.tick(2000)   # 60 FPS

pygame.quit()
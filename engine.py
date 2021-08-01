"""Visualization of pathfinding"""
import pygame
import numpy as np
from maze_gen import MazeGen


pygame.init()
display = pygame.display.set_mode((640, 480), flags=pygame.SCALED)
#  fake_display = display.copy()


arr = MazeGen(70, 60).generate()

surf = pygame.surfarray.make_surface(arr)

running: bool = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        #  if event.type == pygame.VIDEORESIZE:
        #      pygame.display._resize_event(event)

    #  fake_display.blit(surf, (0, 0))
    #  display.blit(surf, (0, 0))
    display.blit(pygame.transform.scale(surf, (640, 480)), (0, 0))
    pygame.display.flip()

pygame.quit()

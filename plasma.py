"""Perlin noize generation"""
import pygame
import math
import numpy as np


def init_world():
    pygame.init()
    display = pygame.display.set_mode((800, 600), flags=pygame.SCALED)
    display.fill((0, 0, 0))
    return display


def generate_perlin_noise_2d(shape, res):
    def f(t):
        return 6 * t ** 5 - 15 * t ** 4 + 10 * t ** 3

    delta = (res[0] / shape[0], res[1] / shape[1])
    d = (shape[0] // res[0], shape[1] // res[1])
    grid = (
        np.mgrid[0 : res[0] : delta[0], 0 : res[1] : delta[1]].transpose(
            1, 2, 0
        )
        % 1
    )
    # Gradients
    angles = 2 * np.pi * np.random.rand(res[0] + 1, res[1] + 1)
    gradients = np.dstack((np.cos(angles), np.sin(angles)))
    g00 = gradients[0:-1, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g10 = gradients[1:, 0:-1].repeat(d[0], 0).repeat(d[1], 1)
    g01 = gradients[0:-1, 1:].repeat(d[0], 0).repeat(d[1], 1)
    g11 = gradients[1:, 1:].repeat(d[0], 0).repeat(d[1], 1)
    # Ramps
    n00 = np.sum(grid * g00, 2)
    n10 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1])) * g10, 2)
    n01 = np.sum(np.dstack((grid[:, :, 0], grid[:, :, 1] - 1)) * g01, 2)
    n11 = np.sum(np.dstack((grid[:, :, 0] - 1, grid[:, :, 1] - 1)) * g11, 2)
    # Interpolation
    t = f(grid)
    n0 = n00 * (1 - t[:, :, 0]) + t[:, :, 0] * n10
    n1 = n01 * (1 - t[:, :, 0]) + t[:, :, 0] * n11
    return np.sqrt(2) * ((1 - t[:, :, 1]) * n0 + t[:, :, 1] * n1)


def generate_surface():
    """Generate perlin's noize and
    fit matrix range from [-1...1] to [0...255]
    """
    surf = (
        ((generate_perlin_noise_2d((800, 800), (10, 10)) + 1) / 2) * 255
    ).astype("uint8")
    return surf


def calculate_sin_table():
    sin_table = []
    for x in range(360):
        value = math.sin(math.radians(x))
        value = ((value + 1) / 2.0) * 255
        sin_table.append(int(value))
    return sin_table


def change_pallete(surface, value, sin_table):
    """Create and set surface pallete

    param surface: surface from pygame
    param value: periodical value in range of 0...359
    """
    palette = []
    for x in range(256):
        palette_item = (
            sin_table[value],
            x,
            x,
            255,
        )
        palette.append(palette_item)
        print(palette_item)
    surface.set_palette(palette)


def world_loop(display):
    """Main loop"""
    running: bool = True
    color_value = 0
    sin_table = calculate_sin_table()
    clock = pygame.time.Clock()

    surface = pygame.surfarray.make_surface(generate_surface())

    while running:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                surface = pygame.surfarray.make_surface(generate_surface())

        change_pallete(surface, color_value, sin_table)
        display.blit(surface, (0, 0))
        pygame.display.flip()

        if color_value >= 359:
            color_value = 0
        else:
            color_value += 1

        #  pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    display = init_world()
    world_loop(display)

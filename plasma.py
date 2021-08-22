"""Perlin noize generation"""
import pygame
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


def grayscale(surface: pygame.Surface):
    arr = pygame.surfarray.pixels3d(surface)
    mean_arr = np.dot(arr[:, :, :], [0.216, 0.587, 0.144])
    mean_arr3d = mean_arr[..., np.newaxis]
    new_arr = np.repeat(mean_arr3d[:, :, :], 3, axis=2)
    return pygame.surfarray.make_surface(new_arr)


def generate_surface():
    surf = (
        ((generate_perlin_noise_2d((800, 800), (10, 10)) + 1) / 2) * 255
    ).astype("uint8")
    return surf


def greyscale_pallete(surface):
    palette = []
    for x in range(256):
        palette.append([x, x, x, 255])
    surface.set_palette(palette)


def world_loop(display):
    """Main loop"""
    running: bool = True
    clock = pygame.time.Clock()

    surface = pygame.surfarray.make_surface(generate_surface())
    greyscale_pallete(surface)

    while running:
        surface = None
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
                surface = pygame.surfarray.make_surface(generate_surface())
                greyscale_pallete(surface)

                #  print(generate_surface())
                #  print(surface.get_palette())
                #  greyscale_pallete(surface)

        if surface:
            display.blit(surface, (0, 0))
            pygame.display.flip()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    display = init_world()
    world_loop(display)

import pygame

def temp_to_color(value: int) -> tuple[int, int, int]:
    # einfacher Feuer-Farbverlauf: gelb → orange → rot
    return (value, value // 2, 0)

def render_heatmap(screen, heatmap, pixel_size: int = 5):
    for y in range(heatmap.height):
        for x in range(heatmap.width):
            color = temp_to_color(heatmap.my_map[y][x])
            pygame.draw.rect(
                screen,
                color,
                (x * pixel_size, y * pixel_size, pixel_size, pixel_size)
            )
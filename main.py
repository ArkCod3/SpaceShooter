import math

import pygame

# pygame setup
pygame.init()
SCREEN_RESOLUTION: pygame.Vector2 = (1280, 720)
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()
running = True
dt = 0  #in seconds

player_pos: pygame.Vector2 = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(0, 0, 0))

    player_mouse_vector: pygame.Vector2 = pygame.mouse.get_pos() - player_pos
    player_mouse_mag: float = math.sqrt(player_mouse_vector.x**2 + player_mouse_vector.y**2)
    player_mouse_dir: pygame.Vector2 = player_mouse_vector / player_mouse_mag

    rotation: float = math.atan2(player_mouse_vector.y, player_mouse_vector.x)

    PLAYER_RADIUS: float = 50.0
    PLAYER_NOSE_RADIUS: float = PLAYER_RADIUS / 5.0
    PLAYER_COLOR: pygame.Color = pygame.Color(255, 255, 255)
    PLAYER_NOSE_COLOR: pygame.Color = pygame.Color(255, 0, 255)

    pygame.draw.circle(screen, PLAYER_COLOR, player_pos, PLAYER_RADIUS)
    pygame.draw.circle(screen, PLAYER_NOSE_COLOR, player_pos + (player_mouse_dir * PLAYER_RADIUS), PLAYER_NOSE_RADIUS)

    SPEED: int = 400 # pixels per second

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= SPEED * dt
    
    if keys[pygame.K_s]:
        player_pos.y += SPEED * dt
    
    if keys[pygame.K_a]:
        player_pos.x -= SPEED * dt
    
    if keys[pygame.K_d]:
        player_pos.x += SPEED * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    FRAME_RATE: float = 60.0
    dt = clock.tick(FRAME_RATE) / 1000

pygame.quit()
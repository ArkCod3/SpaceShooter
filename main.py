import pygame

import math

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
# rotation = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(pygame.Color(0, 0, 125, 100))


    # print(player_pos + (10, 10), player_pos + (20, 20))

    SIDE_LENGTH: float = 20
    SIDE_COUNT: int = 3
    
    rads_per_vertice: float = math.tau / SIDE_COUNT

    rads: float = rads_per_vertice * 0
    point1 = (math.cos(rads) * SIDE_LENGTH, math.sin(rads) * SIDE_LENGTH)

    rads = rads_per_vertice * 1
    point2 = (math.cos(rads) * SIDE_LENGTH, math.sin(rads) * SIDE_LENGTH)

    rads = rads_per_vertice * 2
    point3 = (math.cos(rads) * SIDE_LENGTH, math.sin(rads) * SIDE_LENGTH)

    # mag = math.sqrt((point1[0] ** 2) + (point1[1] ** 2))

    player_to_mouse_vec = pygame.mouse.get_pos() - player_pos
    # player_mouse_mag = math.sqrt(player_to_mouse_vec[0] ** 2 + player_to_mouse_vec[1] ** 2)
    player_to_mouse_dir = (player_to_mouse_vec[0], player_to_mouse_vec[1])

    # ANGULAR_SPEED = math.tau # Rotations per second
    # rotation += ANGULAR_SPEED * dt

    rotation = math.atan2(player_to_mouse_dir[1], player_to_mouse_dir[0])

    angle1 = math.atan2(point1[1], point1[0])
    rotated1 = (math.cos(angle1 + rotation) * SIDE_LENGTH, math.sin(angle1 + rotation) * SIDE_LENGTH)

    angle2 = math.atan2(point2[1], point2[0])
    rotated2 = (math.cos(angle2 + rotation) * SIDE_LENGTH, math.sin(angle2 + rotation) * SIDE_LENGTH)

    angle3 = math.atan2(point3[1], point3[0])
    rotated3 = (math.cos(angle3 + rotation) * SIDE_LENGTH, math.sin(angle3 + rotation) * SIDE_LENGTH)

    # pygame.draw.polygon(screen, "red", (player_pos + point1, player_pos + point2, player_pos + point3))
    pygame.draw.polygon(screen, "red", (player_pos + rotated1, player_pos + rotated2, player_pos + rotated3))

    pygame.draw.circle(screen, "black", player_pos + rotated1, 5)

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

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
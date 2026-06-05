import pygame
pygame.init()

# -----------------------------
# Window
# -----------------------------
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 600

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tron Light Cycle")

# -----------------------------
# Cycle settings
# -----------------------------
CYCLE_SIZE = 20

cycle_x = WINDOW_WIDTH // 2
cycle_y = WINDOW_HEIGHT // 2

cycle_dx = 0
cycle_dy = 0

move_speed = CYCLE_SIZE

# -----------------------------
# Game data
# -----------------------------
trail_coords = []
score = 0
has_moved = False

# -----------------------------
# FPS
# -----------------------------
clock = pygame.time.Clock()
FPS = 15

font = pygame.font.SysFont("Arial", 25)

# -----------------------------
# Sound (load once)
# -----------------------------
collision_sound = pygame.mixer.Sound("pick_up_sound.wav")

# -----------------------------
# Game loop
# -----------------------------
running = True

while running:

    # -------------------------
    # Events
    # -------------------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            left_pressed = event.key == pygame.K_LEFT
            right_pressed = event.key == pygame.K_RIGHT
            up_pressed = event.key == pygame.K_UP
            down_pressed = event.key == pygame.K_DOWN

            cannot_move_horizontal = cycle_dx != 0
            cannot_move_vertical = cycle_dy != 0

            if left_pressed and not cannot_move_horizontal:
                cycle_dx = -move_speed
                cycle_dy = 0
                has_moved = True

            elif right_pressed and not cannot_move_horizontal:
                cycle_dx = move_speed
                cycle_dy = 0
                has_moved = True

            elif up_pressed and not cannot_move_vertical:
                cycle_dx = 0
                cycle_dy = -move_speed
                has_moved = True

            elif down_pressed and not cannot_move_vertical:
                cycle_dx = 0
                cycle_dy = move_speed
                has_moved = True

    # -------------------------
    # Move cycle
    # -------------------------
    cycle_x += cycle_dx
    cycle_y += cycle_dy

    # -------------------------
    # Create cycle rectangle
    # -------------------------
    cycle_rect = (cycle_x, cycle_y, CYCLE_SIZE, CYCLE_SIZE)

    # -------------------------
    # Wall checks (simple steps)
    # -------------------------
    left_wall_hit = cycle_x < 0
    right_wall_hit = cycle_x >= WINDOW_WIDTH
    top_wall_hit = cycle_y < 0
    bottom_wall_hit = cycle_y >= WINDOW_HEIGHT

    hit_wall = (
        left_wall_hit or
        right_wall_hit or
        top_wall_hit or
        bottom_wall_hit
    )

    if hit_wall:
        collision_sound.play()
        pygame.time.delay(1000)
        running = False

    # -------------------------
    # Trail collision
    # -------------------------
    hit_trail = cycle_rect in trail_coords

    if has_moved and hit_trail:
        collision_sound.play()
        pygame.time.delay(1000)
        running = False

    # -------------------------
    # Add trail
    # -------------------------
    trail_coords.insert(0, cycle_rect)

    # -------------------------
    # Score
    # -------------------------
    if has_moved:
        score += 1

    # -------------------------
    # Draw
    # -------------------------
    display.fill((255, 255, 255))

    for block in trail_coords:
        pygame.draw.rect(display, (0, 150, 255), block)

    pygame.draw.rect(display, (0, 0, 100), cycle_rect)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    display.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

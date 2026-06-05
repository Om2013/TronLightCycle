import pygame
pygame.init()

# ---------------- WINDOW ----------------
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 600

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tron Light Cycle")

# ---------------- CYCLE ----------------
CYCLE_SIZE = 20

cycle_x = WINDOW_WIDTH // 2
cycle_y = WINDOW_HEIGHT // 2

cycle_dx = 0
cycle_dy = 0

# ---------------- GAME DATA ----------------
trail_coords = []
score = 0
has_moved = False

# ---------------- SETUP ----------------
clock = pygame.time.Clock()
FPS = 15

font = pygame.font.SysFont("Arial", 25)

collision_sound = pygame.mixer.Sound("pick_up_sound.wav")

# ---------------- GAME LOOP ----------------
running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and cycle_dx == 0:
                cycle_dx = -CYCLE_SIZE
                cycle_dy = 0
                has_moved = True

            elif event.key == pygame.K_RIGHT and cycle_dx == 0:
                cycle_dx = CYCLE_SIZE
                cycle_dy = 0
                has_moved = True

            elif event.key == pygame.K_UP and cycle_dy == 0:
                cycle_dx = 0
                cycle_dy = -CYCLE_SIZE
                has_moved = True

            elif event.key == pygame.K_DOWN and cycle_dy == 0:
                cycle_dx = 0
                cycle_dy = CYCLE_SIZE
                has_moved = True

    # move cycle
    cycle_x += cycle_dx
    cycle_y += cycle_dy

    cycle_rect = (cycle_x, cycle_y, CYCLE_SIZE, CYCLE_SIZE)

    # wall collision
    if cycle_x < 0 or cycle_x >= WINDOW_WIDTH or cycle_y < 0 or cycle_y >= WINDOW_HEIGHT:
        collision_sound.play()
        pygame.time.delay(1000)
        running = False

    # trail collision
    if has_moved and cycle_rect in trail_coords:
        collision_sound.play()
        pygame.time.delay(1000)
        running = False

    trail_coords.insert(0, cycle_rect)

    if has_moved:
        score += 1

    # draw
    display.fill((255, 255, 255))

    for block in trail_coords:
        pygame.draw.rect(display, (0, 150, 255), block)

    pygame.draw.rect(display, (0, 0, 100), cycle_rect)

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    display.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

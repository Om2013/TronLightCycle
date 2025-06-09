import pygame
pygame.init()

# Game window settings 
WINDOW_WIDTH = 650
WINDOW_HEIGHT = 600

CYCLE_SIZE = 20 # How big each segment will be in pixels

cycle_x = WINDOW_WIDTH // 2 # Start at the middle of the screen for x axis 
cycle_y = WINDOW_HEIGHT // 2 # Start at the middle of the screen for y axis

# Snake dx and dy 
cycle_dx = 0 
cycle_dy = 0 

# Set the 
trail_coords = [] # Empty list
score = 0 # Set the list to 0 to start
has_moved = False 

FPS = 15 # Set the frames per second to 15
clock = pygame.time.Clock() # Count how many fps have gone by
display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # Set the window height and width
pygame.display.set_caption("Tron Light Cycle") # Set the window caption
font = pygame.font.SysFont("Arial", 25) # Give the font settings

# Gameloop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # If player quits the screen (clicks on the x)
            running = False # Stop the game 

        # Movement key handling
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT and cycle_dx == 0: # Left
                cycle_dx = -CYCLE_SIZE
                cycle_dy = 0
                has_moved = True
            elif event.key == pygame.K_RIGHT and cycle_dx == 0: # Right
                cycle_dx = CYCLE_SIZE
                cycle_dy = 0
                has_moved = True
            elif event.key == pygame.K_UP and cycle_dy == 0: # Up
                cycle_dx = 0
                cycle_dy = -CYCLE_SIZE
                has_moved = True
            elif event.key == pygame.K_DOWN and cycle_dy == 0: # Down
                cycle_dx = 0
                cycle_dy = CYCLE_SIZE
                has_moved = True
     
    # Move cycle horizontally
    cycle_x += cycle_dx 

    # Move cycle vertically
    cycle_y += cycle_dy

    # Set cycle initial position and size 
    head_coord = (cycle_x, cycle_y, CYCLE_SIZE, CYCLE_SIZE)

    # --- Collision with walls ---
    if cycle_x < 0 or cycle_x >= WINDOW_WIDTH or cycle_y < 0 or cycle_y >= WINDOW_HEIGHT:
        collision_sound = pygame.mixer.Sound(r"C:\Users\omrad\OneDrive\Desktop\Tron Light Cycle - HW\pick_up_sound.wav")
        collision_sound.play() # Play the sound givem
        pygame.time.delay(1000) 
        running = False # Stop the game

    if has_moved and head_coord in trail_coords:
        collision_sound = pygame.mixer.Sound(r"C:\Users\omrad\OneDrive\Desktop\Tron Light Cycle - HW\pick_up_sound.wav")
        collision_sound.play() # Play the sound givem
        pygame.time.delay(1000)
        running = False # Stop the game
     
    
    trail_coords.insert(0, head_coord)
    if has_moved:
     score += 1

    # --- Draw everything ---
    display.fill((255, 255, 255))  # White background

    # Draw the trail
    for block in trail_coords:
        pygame.draw.rect(display, (0, 150, 255), block)  # Trail color

    pygame.draw.rect(display, (0, 0, 100), head_coord)  # Head color
     
    
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    display.blit(score_text, (10, 10))

    # Update the screen and count the fps seconds 
    pygame.display.flip()
    clock.tick(FPS)

# Quit pygame 
pygame.quit()

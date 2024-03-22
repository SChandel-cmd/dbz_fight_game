import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of your window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# Create the window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Cropped Image Square")

# Load your image
image = pygame.image.load("assets/sprites/goku_processed/goku_big_7.png")
image_width, image_height = image.get_size()

# Determine the size of the square
square_size = min(image_width, image_height) //2

# Create a new surface for the square
square_surface = pygame.Surface((square_size, square_size))

# Calculate the offset for centering the image within the square
offset_x = (square_size - image_width) // 2
offset_y = (square_size - image_height) // 2

# Blit the image onto the square surface
square_surface.blit(image, (offset_x, offset_y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Blit the square surface onto the screen
    screen.blit(square_surface, (50, 50))  # Adjust position as needed

    # Update the display
    pygame.display.flip()

pygame.quit()
sys.exit()

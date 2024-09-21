import pygame
from pygame.examples.cursors import image

pygame.init()

# Screen dimensions and display characteristics
sc_width, sc_height = 800, 400

main_screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Pancho´s Game") # screen tittle

# Load an image to be used as the game icon
main_icon = pygame.image.load("graphics/fs.ico")
pygame.display.set_icon(main_icon)

# Create an instance of clock so we can define the fpm our game is going to run (max speed)
game_clock = pygame.time.Clock() # Need to be call inside the while loop

# JUST TEST THINGS HERE
# surface_t = pygame.Surface((100, 300))
# surface_t.fill("darkorange4")

# load the sky and ground image
sky_img = pygame.image.load("graphics/Sky.png")
ground_img = pygame.image.load("graphics/ground.png")

# Run the screen by using while
while True:
    # Is constantly scanning user actions by getting any possible event (keys, mouse clicks and so on)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:   # Closes the windows and stop the code
            pygame.quit()
            exit()

    # TEST SECTION DISPLAY
    # main_screen.blit(surface_t, (5, 5))

    # bg images
    main_screen.blit(sky_img, (0, 0))
    main_screen.blit(ground_img, (0, 300))

    # Updates the screen at any while iteration
    pygame.display.update()
    game_clock.tick(60)
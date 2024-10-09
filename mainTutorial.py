import pygame
from pygame import MOUSEMOTION
from pygame.examples.cursors import image
from math import sqrt

pygame.init()

# Screen dimensions and display characteristics
sc_width, sc_height = 800, 400

# Extra variables
game_activity = True
counter = 0

# Variables related to character movements
cha_gravity = 0

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
sky_img = pygame.image.load("graphics/sky.png").convert_alpha()
ground_img = pygame.image.load("graphics/ground.png").convert_alpha()

# load character
cha_sur = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
cha_rec = cha_sur.get_rect(midbottom=(100, 300))

# load snail 1
snail1_surface = pygame.image.load("graphics/Snail/snail1.png").convert_alpha()
snail1_rec = snail1_surface.get_rect(bottomleft=(900, 300)) # Initial position

# Create and load font so we can write info on the screen
tutorial_font = pygame.font.Font("font/Pixeltype.ttf", 50)
score_surf = tutorial_font.render("score: ", True, "red")
score_rec = score_surf.get_rect(midbottom=(400, 40))


# Run the screen by using while
while True:
    # Is constantly scanning user actions by getting any possible event (keys, mouse clicks and so on)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:   # Closes the windows and stop the code
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Mouse pressed")
            if cha_rec.collidepoint(event.pos):
                print("do something")
        if event.type == pygame.MOUSEBUTTONUP:
            print("Mouse released")

        if event.type == pygame.MOUSEMOTION:
            # print(event.pos)
            pass

        # Character movements
        # One way to do it

        if event.type == pygame.KEYDOWN:
            # Character movements (UP)
            if cha_rec.bottom == 300 and event.key == pygame.K_SPACE:
                print("up")
                cha_gravity -= 20


    # ------------------------------------------------------------------------------------------------------------

    # TEST SECTION
    # Here I do tests and exercises from the course

    # ------------------------------------------------------------------------------------------------------------

    # main_screen.blit(surface_t, (5, 5))
    a = pygame.mouse.get_pos()

    if snail1_rec.collidepoint(a):
        print("Cawadunga")
        pygame.mouse.set_pos(0, 0)

    # exercise (draw a line from tot left to bottom right)
    # pygame.draw.line(main_screen, "blue", (0, 0), (800, 400), 10)

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    if game_activity:
        # bg images and text
        main_screen.blit(sky_img, (0, 0))
        main_screen.blit(ground_img, (0, 300))
        main_screen.blit(score_surf, score_rec)

        # show main character

        # up movement conditions
        cha_gravity += 1
        cha_rec.bottom += cha_gravity

        if cha_rec.bottom >= 300:
            cha_rec.bottom = 300
            cha_gravity = 0

        main_screen.blit(cha_sur, cha_rec)

        # show snails
        snail1_rec.x -= 4


        if snail1_rec.right < 0:
            snail1_rec.x = 880

        main_screen.blit(snail1_surface, snail1_rec)

        if cha_rec.colliderect(snail1_rec):
            print("au")
            snail1_rec.right = 900
            counter += 1
            print(counter)
            if counter == 5:
                game_activity = not game_activity


        # Character movement instructions method 2, I´ll use it to sides movements

        all_keys = pygame.key.get_pressed()
        if (all_keys[pygame.K_RIGHT] or all_keys[pygame.K_d]) and (cha_rec.right < 800):
            cha_rec.right += 10

        if (all_keys[pygame.K_LEFT] or all_keys[pygame.K_a]) and (cha_rec.left > 0):
            cha_rec.right -= 10

    # Updates the screen at any while iteration
    pygame.display.update()
    game_clock.tick(60)
from random import randrange

import pygame
from sys import exit


pygame.init()   # always required tu run pygame

# Extra variables
lives = 10

# Display main surface, tittle and icon
screen_width = 800
screen_height = 400
game_screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("SK")
game_icon = pygame.image.load("graphics/fs.ico")
pygame.display.set_icon(game_icon)


# We need to use this to ensure our game runs to a maximum of fps, we´ll use 60 fps
game_clock = pygame.time.Clock()


# Background images initial position
back_img_pos = [0, -200]
back_img_2_pos  = [1000, -200]

# Load background images to use, we use convert_alpha to standardize the images and make life easier for pygame
back_img = pygame.image.load("graphics/cordillera.jpg").convert_alpha()
back_img_2 = pygame.image.load("graphics/cordillera2.jpg").convert_alpha()
ground_image = pygame.image.load("graphics/ground.png").convert_alpha()

# Load main character, change its size and remove bg colour
main_character = pygame.image.load("graphics/Player/character.png").convert_alpha()
main_character_scl = pygame.transform.scale(main_character, (80, 80))
main_character_scl.set_colorkey((255, 255, 255))

# Creates a rectangle around our character so it is easier to locate
main_ch_rec = main_character_scl.get_rect(bottomleft=(0, 300))

# Load enemies (images)
moth_one = pygame.image.load("graphics/snail/moth1.png").convert_alpha()
moth_one_scl = pygame.transform.scale(moth_one, (60, 60))
moth_one_rec = moth_one_scl.get_rect(bottomleft=(800, 200))


# Here we draw and update everything appear on the screen
while True:

    # Check all the possible events happening and take actions depending on the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # First quits the pygame module and next it exits the whole code
            pygame.quit()
            print("Game Successfully closed")
            exit()

        if event.type == pygame.KEYDOWN:
            # Character movements
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                print("left")
                main_ch_rec.left -= 10

            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                print("right")
                main_ch_rec.left += 10

            if event.key == pygame.K_UP or event.key == pygame.K_w:
                print("up")
                main_ch_rec.bottom -= 10

            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                print("down")
                if main_ch_rec.bottom >= 300:
                    main_ch_rec.bottom = 300
                else:
                    main_ch_rec.bottom += 10



    # Generate background movement
    back_img_pos[0] -= .5
    back_img_2_pos[0] -= .5

    game_screen.blit(back_img, (back_img_pos[0], back_img_pos[1]))
    game_screen.blit(back_img_2, (back_img_2_pos[0], back_img_2_pos[1]))
    game_screen.blit(ground_image, (0, 300))

    # set limits in the background images movement
    if back_img_pos[0] + 1000 < 0:
        back_img_pos[0] = 1000

    if back_img_2_pos[0] + 1000 < 0:
        back_img_2_pos[0] = 1000

    # Gives movement to the enemy
    moth_one_rec.left -= 2
    moth_one_rec.bottom += randrange(-1, 2) # just give some oscillation to the enemy

    game_screen.blit(moth_one_scl, moth_one_rec)

    # set limits to the enemy movement and resend the enemy to appear again
    if moth_one_rec.right < 0:
        moth_one_rec.left = randrange(800, 1000)
        moth_one_rec.bottom = randrange(60, 250)


    # Main character
    if main_ch_rec.left < 800:
        main_ch_rec.left += 0
        game_screen.blit(main_character_scl, main_ch_rec)

    else:
        main_ch_rec.right = 0

    if main_ch_rec.colliderect(moth_one_rec):
        lives -= 1
        print("Lives: ")
        print(lives)

    # Updates our screen surface
    pygame.display.update()

    # Limits our game to 60 fps
    game_clock.tick(60)


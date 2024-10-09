from random import randrange
from turtle import TurtleScreen

import pygame
from sys import exit

pygame.init()   # always required tu run pygame

# Extra variables
lives = 5
keep = True
main_ch_gravity = 0
lives_surf = None

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

# Create text to display info
lives_font = pygame.font.Font("font/Atop.ttf", 40)
game_over_font = pygame.font.Font("font/Atop.ttf", 80)
game_over_font_2 = pygame.font.Font("font/Atop.ttf", 40)


# Load main character, change its size and remove bg colour
main_ch = pygame.image.load("graphics/Player/character.png").convert_alpha()
main_ch_scl = pygame.transform.scale(main_ch, (80, 80))
main_ch_scl.set_colorkey((255, 255, 255))

main_ch_walk = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
main_ch__walk_rec = main_ch_walk.get_rect(bottomleft=(0, 300))

# Creates a rectangle around our character so it is easier to locate
main_ch_rec = main_ch_scl.get_rect(bottomleft=(0, 300))

# Load enemies (images)
moth_one = pygame.image.load("graphics/Snail/moth1.png").convert_alpha()
moth_one_scl = pygame.transform.scale(moth_one, (60, 60))
moth_one_rec = moth_one_scl.get_rect(bottomleft=(800, 200))

# Here we draw and update everything appear on the screen

while True:
    # Check all the possible events happening and take actions depending on the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # First quits the pygame module and next it exits the whole code
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN and keep == False:
            if event.key == pygame.K_1:
                keep = True
                lives = 5
                main_ch_rec.left = 0
                game_screen.blit(main_ch_scl, main_ch_rec)

            elif event.key == pygame.K_2:
                pygame.quit()
                exit()


        # The character just can jump if it is touching the ground
        if event.type == pygame.KEYDOWN and main_ch_rec.bottom == 300:

            # Character movement (UP)
            if event.key == pygame.K_SPACE:
                main_ch_gravity -= 20


    # Generate background movement
    if main_ch_rec.right == screen_width:
        back_img_pos[0] -= 5
        back_img_2_pos[0] -= 5

    if keep:
        game_screen.blit(back_img, (back_img_pos[0], back_img_pos[1]))
        game_screen.blit(back_img_2, (back_img_2_pos[0], back_img_2_pos[1]))
        game_screen.blit(ground_image, (0, 300))

        # Testing circle
        pygame.draw.circle(game_screen, "red", (10, 10), 5)


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


        # Main character position and some instructions
        main_ch_gravity += 1
        main_ch_rec.bottom += main_ch_gravity

        if main_ch_rec.bottom >= 300:
            main_ch_rec.bottom = 300
            main_ch_gravity = 0

        # This way we can create a smooth movement from side to side in the character
        # also limited the character to go no further than the screen´s width
        pressed_key = pygame.key.get_pressed()
        if (pressed_key[pygame.K_RIGHT] or pressed_key[pygame.K_d]) and (main_ch_rec.right < 800):
            main_ch_rec.right += 5

        if (pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]) and (main_ch_rec.left > 0):
            main_ch_rec.right -= 5

        game_screen.blit(main_ch_scl, main_ch_rec)

        # Check for collision between enemies and main character
        if main_ch_rec.colliderect(moth_one_rec):
            lives -= 1
            moth_one_rec.left = randrange(800, 1000)
            moth_one_rec.bottom = randrange(60, 250)

        # Shows lives text on the screen (at the end so no image cover it)
        lives_surf = lives_font.render(f"lives: {lives}", False, "white")
        lives_rect = lives_surf.get_rect(bottomleft=(20, 50))
        game_screen.blit(lives_surf, lives_rect)

        if lives <= 0:
            keep = False

    else:
        game_screen.fill("White")
        game_over_surf = game_over_font.render("Game Over", False, "darkred")
        game_over_rect = lives_surf.get_rect(bottomleft=(200, 100))
        game_screen.blit(game_over_surf, game_over_rect)

        retry_surf = game_over_font_2.render("retry:", False, "darkred")
        retry_rect = retry_surf.get_rect(bottomleft=(200, 200))
        game_screen.blit(retry_surf, retry_rect)

        retry_yes_surf = game_over_font_2.render("1 - Yes", False, "darkred")
        retry_yes_rect = retry_yes_surf.get_rect(bottomleft=(200, 250))
        game_screen.blit(retry_yes_surf, retry_yes_rect)

        retry_no_surf = game_over_font_2.render("2 - No", False, "darkred")
        retry_no_rect = retry_no_surf.get_rect(bottomleft=(200, 300))
        game_screen.blit(retry_no_surf, retry_no_rect)


    # Updates our screen surface
    pygame.display.update()

    # Limits our game to 60 fps
    game_clock.tick(60)


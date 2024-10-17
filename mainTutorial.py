from random import randint
import pygame
# from pygame import MOUSEMOTION
# from pygame.examples.cursors import image

def game_score():
    current_time = pygame.time.get_ticks() - start_time # Count since we start init
    current_time_sec = int(current_time/1000)
    game_score_surf = tutorial_font.render(f"SCORE: {current_time_sec} ", False, "red")
    game_score_surf_rect = game_score_surf.get_rect(midbottom=(100, 50))
    main_screen.blit(game_score_surf, game_score_surf_rect)

def game_lives(lives_to_show, where):
    game_lives_surf = tutorial_font.render(f"LIVES: {lives_to_show} ", False, "red")
    game_lives_rect = game_lives_surf.get_rect(midbottom=(700, 50))
    where.blit(game_lives_surf, game_lives_rect)

def insects_mov(insect_rectangles, cha_rectangle, game_live:int):
    if insect_rectangles:
        for insect_rec in insect_rectangles:
            insect_rec.x -= 4

            # Check for collisions so we discount lives
            if cha_rectangle.colliderect(insect_rec):
                game_live -= 1
                insect_rec.left = -100
                print(game_live)

            if insect_rec.bottom == 300:
                main_screen.blit(snail1_surface, insect_rec)
            elif insect_rec.bottom < 300:
                main_screen.blit(fly_surface, insect_rec)
        # Deletes the rectangle after it is located at position -100
        insect_rectangles = [obstacle for obstacle in insect_rectangles if obstacle.x > -100]

        return insect_rectangles, game_live

    else:
        return [], game_live


pygame.init()

# Screen dimensions and display characteristics
sc_width, sc_height = 800, 400

# Extra variables
game_activity = True
cha_lives = 5
start_time = 0

insect_option = None
insects_rec_list = []


# Variables related to character movements
cha_gravity = 0

main_screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Pancho´s Game") # screen tittle

# Load an image to be used as the game icon
main_icon = pygame.image.load("graphics/fs.ico")
pygame.display.set_icon(main_icon)

# Create an instance of clock so we can define the fpm our game is going to run (max speed)
game_clock = pygame.time.Clock() # Need to be call inside the while loop

# load the sky and ground image
sky_img = pygame.image.load("graphics/sky.png").convert_alpha()
ground_img = pygame.image.load("graphics/ground.png").convert_alpha()

# load character
cha_sur = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
cha_rec = cha_sur.get_rect(midbottom=(100, 300))

# insects images
snail1_surface = pygame.image.load("graphics/Snail/snail1.png").convert_alpha()
fly_surface = pygame.image.load("graphics/Fly/Fly1.png").convert_alpha()

# Create and load font so we can write info on the screen
tutorial_font = pygame.font.Font("font/Pixeltype.ttf", 50)

# Events
insects_event = pygame.USEREVENT + 1
pygame.time.set_timer(insects_event, randint(1000, 1400))

# Run the screen by using while
while True:
    # Is constantly scanning user actions by getting any possible event (keys, mouse clicks and so on)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:   # Closes the windows and stop the code
            pygame.quit()
            exit()

        # Just works while the game is working
        if game_activity:
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(insects_rec_list)
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
                    cha_gravity -= 20

            # User event to control how often insects appear on screen
            if event.type == insects_event and game_activity == True:
                # depending on which option is assigned to the variable, which insect is appended to the list
                # hence put into the rectangle and shows on screen

                insect_option = randint(0, 1)
                if insect_option:
                    insects_rec_list.append(snail1_surface.get_rect(bottomleft=(randint(850, 1000), 300)))
                else:
                    insects_rec_list.append(fly_surface.get_rect(bottomleft=(randint(850, 1000),
                                                                             randint(100, 250))))

        # Whenever game activity goes to False check instructions to reset or quit game
        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_1:
                keep = True
                cha_lives = 5
                cha_rec.left = 0
                main_screen.blit(cha_sur, cha_rec)
                game_activity = True
                start_time = pygame.time.get_ticks()

            elif event.key == pygame.K_2:
                pygame.quit()
                exit()

    # ------------------------------------------------------------------------------------------------------------

    # TEST SECTION
    # Here I do tests and exercises from the course

    # ------------------------------------------------------------------------------------------------------------

    # exercise (draw a line from top left to bottom right)
    # pygame.draw.line(main_screen, "blue", (0, 0), (800, 400), 10)

    # ------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------------------------------------------------------------------

    if game_activity:
        # bg images and text
        main_screen.blit(sky_img, (0, 0))
        main_screen.blit(ground_img, (0, 300))


        # show main character

        # up movement conditions
        cha_gravity += 1
        cha_rec.bottom += cha_gravity

        if cha_rec.bottom >= 300:
            cha_rec.bottom = 300
            cha_gravity = 0

        main_screen.blit(cha_sur, cha_rec)

        # Insects inserted to the screen
        insects_rec_list, cha_lives = insects_mov(insects_rec_list, cha_rec, cha_lives)

        # Character movement instructions method 2, I´ll use it to sides movements
        all_keys = pygame.key.get_pressed()
        if (all_keys[pygame.K_RIGHT] or all_keys[pygame.K_d]) and (cha_rec.right < 800):
            cha_rec.right += 10

        if (all_keys[pygame.K_LEFT] or all_keys[pygame.K_a]) and (cha_rec.left > 0):
            cha_rec.right -= 10

        game_score()
        game_lives(cha_lives, main_screen)

        if cha_lives == 0:
            game_activity = False
            insects_rec_list.clear()

    else:
        main_screen.fill("black")
        game_over_surf = tutorial_font.render("Game Over", False, "red")
        game_over_rect = game_over_surf.get_rect(bottomleft=(200, 100))
        main_screen.blit(game_over_surf, game_over_rect)

        play_again_surf = tutorial_font.render("Try again:", False, "white")
        play_again_rect = play_again_surf.get_rect(bottomleft=(200, 150))
        main_screen.blit(play_again_surf, play_again_rect)

        yes_surf = tutorial_font.render("1) Yes", False, "white")
        yes_rec = yes_surf.get_rect(bottomleft=(200, 200))
        main_screen.blit(yes_surf, yes_rec)

        no_surf = tutorial_font.render("2) No", False, "white")
        no_rec = no_surf.get_rect(bottomleft=(350, 200))
        main_screen.blit(no_surf, no_rec)


    # Updates the screen at any while iteration
    pygame.display.update()
    game_clock.tick(60)
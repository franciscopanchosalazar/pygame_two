from random import randrange, randint
import pygame
from sys import exit

# Functions

# this function allows me to show multiple enemies

# enemies_rect_list = enemies_movement(enemies_rect_list, va=enemy_condition)
def lives_img_movement(lives_image):
    game_screen.blit(lives_img, lives_image)

def enemies_movement(enemies_list, mov_speed=6, game_lives=5):
    if enemies_list:
        for enemies_rect in enemies_list:
            enemies_rect.x -= mov_speed

            # Check for collision between enemies and main character
            if main_ch_rec.colliderect(enemies_rect):
                game_lives -= 1
                enemies_rect.left = randrange(800, 1000)

            if 40 < enemies_rect.y < 150:
                game_screen.blit(moth_one_scl, enemies_rect)
            elif 150 < enemies_rect.y < 300:
                game_screen.blit(moth_two_scl, enemies_rect)
            else:
                pass

        enemies_list = [enemy for enemy in enemies_list if enemies_rect.x > -100]

        return enemies_list, game_lives

    else:
        return [], game_lives

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


# Lives image
lives_img = pygame.image.load("graphics/raid.png").convert_alpha()
lives_img = pygame.transform.rotozoom(lives_img, -15, 0.15)


# Load enemies (images)
moth_one = pygame.image.load("graphics/Snail/moth1.png").convert_alpha()
moth_one_scl = pygame.transform.scale(moth_one, (60, 60))
# moth_one_rec = moth_one_scl.get_rect(bottomleft=(800, 200)) # used to the first idea

moth_two = pygame.image.load("graphics/Snail/moth2.png").convert_alpha()
moth_two_scl = pygame.transform.scale(moth_two, (60, 60))
# moth_two_rec = moth_two_scl.get_rect(bottomleft=(800, 200))


# Enemies actions and variables
enemies_pos_x = 0
enemies_pos_y = 0
enemies_rect_list = []


# Here we draw and update everything appear on the screen

# Create an event which will be repeated in intervals of time
enemies_event_one = pygame.USEREVENT + 1
pygame.time.set_timer(enemies_event_one, randint(1000, 2000))   # Triggers the event within a range of time


# Event for the lives can appearance:
lives_event = pygame.USEREVENT + 2
pygame.time.set_timer(lives_event, randint(7000, 9000))

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

        # This is the event I created
        if event.type == enemies_event_one and keep == True:
            enemies_pos_x = randint(850, 1000)
            enemies_pos_y = randint(60, 300)
            op = randint(0, 1)
            print(op)
            if op:   # If it is one(True)
                enemies_rect_list.append(moth_one_scl.get_rect(bottomleft=(enemies_pos_x, randint(40, 150))))
                #enemy_condition = 1
            else:
                enemies_rect_list.append(moth_two_scl.get_rect(bottomleft=(enemies_pos_x, randint(150, 300))))
                #enemy_condition = 2

        if event.type == lives_event and keep == True:
            if lives <= 3:
                lives_can_px, lives_can_py = randint(850, 1000), randint(60, 300)
                lives_img_rec = lives_img.get_rect(bottom=300)
                print("Can should appear now")
                lives_img_movement(lives_img_rec)

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

        # Raid display
        # game_screen.blit(lives_img, lives_img_rec)

        # set limits in the background images movement
        if back_img_pos[0] + 1000 < 0:
            back_img_pos[0] = 1000

        if back_img_2_pos[0] + 1000 < 0:
            back_img_2_pos[0] = 1000

        # Gives movement to the enemy
        enemies_rect_list, lives = enemies_movement(enemies_rect_list, game_lives=lives)

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
            main_ch_rec.right += 10

        if (pressed_key[pygame.K_LEFT] or pressed_key[pygame.K_a]) and (main_ch_rec.left > 0):
            main_ch_rec.right -= 10

        game_screen.blit(main_ch_scl, main_ch_rec)


        # Shows lives text on the screen (at the end so no image cover it)
        lives_surf = lives_font.render(f"lives: {lives}", False, "white")
        lives_rect = lives_surf.get_rect(bottomleft=(20, 50))
        game_screen.blit(lives_surf, lives_rect)

        if lives <= 0:
            keep = False

    else:
        # Create surfaces for game over fonts
        game_over_surf = game_over_font.render("Game Over", False, "darkred")
        game_over_rect = game_over_surf.get_rect(bottomleft=(200, 100))
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

        enemies_rect_list.clear()

    # Updates our screen surface
    pygame.display.update()

    # Limits our game to 60 fps
    game_clock.tick(60)


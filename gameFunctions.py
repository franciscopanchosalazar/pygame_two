import pygame
from random import randrange

game_screen = pygame.display.set_mode((600, 400))  # Display a surface
pygame.display.set_caption("SK")
game_clock = pygame.time.Clock()


# Function utilized to insert, adjust size and put a character in some position on screen
def characters_insert(screen, ch_path, ch_width, ch_height, pos_x, pos_y):
    ch_img = pygame.image.load(ch_path).convert_alpha()
    pygame.transform.scale(ch_img, (ch_width, ch_height))
    ch_pos = [pos_x, pos_y]

    ready_ch = screen.blit(ch_img, (ch_pos[0], ch_pos[1]))

    return ready_ch


def ch_mov(ch_to_move, mv_by):
    pass



while True:
    game_screen.fill("dodgerblue")

    # Check all the possible events happening and take actions depending on the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # First quits the pygame module and next it exits the whole code
            pygame.quit()
            print("Game Successfully closed")
            exit()

    ch_one = characters_insert(game_screen,"graphics/snail/snail1.png",
                                   120, 120, 110, 300)


    pygame.display.update()

    # Limits our game to 60 fps
    game_clock.tick(20)

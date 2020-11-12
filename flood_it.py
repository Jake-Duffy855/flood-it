# Simple pygame program
# 934 478 40 40
# Import and initialize the pygame library
import pygame
import autopy
import cv2
import board
import time

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([560, 600])
game = board.Board()
possible_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (127, 0, 255)]
# Run until the user asks to quit
prev_color = (255, 0, 0)
running = True
while running:
    # time.sleep(.3)
    # max_changed = 0
    # max_point = (0, 0)
    # for color in possible_colors:
    #     test = game.__copy__()
    #     point = game.get_pos_of_color(color)
    #     if point is not None:
    #         prev_color = color
    #         test.click(point)
    #         changed = test.click(game.get_pos_of_color(prev_color))
    #         if changed > max_changed:
    #             max_changed = changed
    #             max_point = point
    #
    #
    # print(max_point)
    # game.click(max_point)

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            ev = pygame.event.get()

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            pos = tuple(int(posi/40) for posi in pos)
            game.click(pos)

    # Fill the background with white
    screen.fill((255, 255, 255))

    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    text_surface = font.render(str(game.moves), True, (0, 0, 0))
    screen.blit(text_surface, (270, 565))

    # Draw a solid blue circle in the center
    for i in range(game.size):
        for j in range(game.size):
            # color = cv2.get_color
            # color = autopy.color.hex_to_rgb(autopy.screen.get_color(934 + 40 * i, 478 + 40 * j))
            pygame.draw.rect(screen, game.squares[i][j].color, (40 * j, 40 * i, 40, 40))

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()

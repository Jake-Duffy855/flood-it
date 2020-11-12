# Simple pygame program
# 934 478 40 40
# Import and initialize the pygame library
import pygame
import autopy
import cv2
import board
import time


def get_colors(moves):
    result = []
    for color in moves:
        if color == (255, 0, 0):
            result.append("r")
        elif color == (255, 128, 0):
            result.append("o")
        elif color == (255, 255, 0):
            result.append("y")
        elif color == (0, 255, 0):
            result.append("g")
        elif color == (0, 0, 255):
            result.append("b")
        elif color == (127, 0, 255):
            result.append("p")
    return result

def get_best_move(game, moves_ahead=1):
    max_changed = 0
    max_point = (0, 0)
    moves_ahead -= 1
    for color in possible_colors:
        if color != game.squares[0][0].color:
            test = game.__copy__()
            point = test.get_pos_of_color(color)
            if point is not None:
                test.click(point)
                colors = test.get_colors_left()
                colors.remove(test.squares[0][0].color)
                if len(colors) > 0:
                    if moves_ahead == 0:
                        changed = test.click(test.get_pos_of_color(colors[0]))
                    else:
                        changed = get_best_move(test, moves_ahead)[0]

                    if changed > max_changed:
                        max_changed = changed
                        max_point = point
                else:
                    return (0, (0, 0))

    return max_changed, max_point


pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([560, 600])
game = board.Board()
possible_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (127, 0, 255)]
# Run until the user asks to quit
running = True
min_moves = 40
moves_ahead = 3
total_moves = 0
games = 0
moves = []

while running:
    # time.sleep(0.01)
    move = get_best_move(game, moves_ahead)[1]
    if move != (0, 0):
        game.click(move)
        moves.append(game.squares[move[0]][move[1]].color)
    else:
        total_moves += game.moves + moves_ahead
        games += 1
        if game.moves + moves_ahead <= min_moves:
            min_moves = game.moves + moves_ahead
        game = board.Board()
        print(total_moves/games, min_moves)
        print(get_colors(moves))
        moves = []


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



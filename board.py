import square as s
import random


class Board:
    possible_colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (127, 0, 255)]

    def __init__(self, size=14, colors=6):
        self.solved = False
        self.moves = 0
        self.size = size
        self.colors = colors
        self.squares = [[random_square(x, y) for y in range(size)] for x in range(size)]

    def click(self, pos):
        color = self.squares[pos[1]][pos[0]].color
        changed = 0
        if (color != self.squares[0][0].color):
            self.solved = False
            self.change_to_color(0, 0, color)
            self.moves += 1
            for i in range(self.size):
                for j in range(self.size):
                    if self.squares[i][j].changed:
                        changed += 1
                        self.squares[i][j].changed = False
        return changed

    def change_to_color(self, x, y, color):
        if x + 1 < self.size and not self.squares[y][x + 1].changed:
            if self.squares[y][x + 1].color == self.squares[y][x].color:
                self.squares[y][x + 1].changed = True
                self.change_to_color(x + 1, y, color)
            else:
                self.solved = False
        if x - 1 >= 0 and not self.squares[y][x - 1].changed:
            if self.squares[y][x - 1].color == self.squares[y][x].color:
                self.squares[y][x - 1].changed = True
                self.change_to_color(x - 1, y, color)
            else:
                self.solved = False
        if y + 1 < self.size and not self.squares[y + 1][x].changed:
            if self.squares[y + 1][x].color == self.squares[y][x].color:
                self.squares[y + 1][x].changed = True
                self.change_to_color(x, y + 1, color)
            else:
                self.solved = False
        if y - 1 >= 0 and not self.squares[y - 1][x].changed:
            if self.squares[y - 1][x].color == self.squares[y][x].color:
                self.squares[y - 1][x].changed = True
                self.change_to_color(x, y - 1, color)
            else:
                self.solved = False

        self.squares[y][x].color = color

    def __str__(self):
        result = ""
        for i in range(self.size):
            for j in range(self.size):
                result += str(self.squares[j][i].x) + " "
            result += "\n"
        return result

    def __copy__(self):
        new = Board(self.size, self.colors)
        for i in range(self.size):
            for j in range(self.size):
                square = self.squares[i][j]
                new.squares[i][j] = s.Square(square.x, square.y, square.color)

        return new

    def get_pos_of_color(self, color):
        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].color == color:
                    return (j, i)

    def get_colors_left(self):
        colors_left = []
        for i in range(self.size):
            for j in range(self.size):
                if self.squares[i][j].color not in colors_left:
                    colors_left.append(self.squares[i][j].color)

        return colors_left


def random_square(x, y):
    return s.Square(x, y, random.choice(Board.possible_colors))

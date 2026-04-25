import matplotlib.pyplot as plt
from random import random, randrange

RED = (255, 0, 0)
BLUE = (0, 255, 0)
WHITE = (255, 255, 255)

W, H = 32, 32


def make_grid(w, h, func):
    return [[func() for _ in range(W)] for _ in range(H)]

def get_random_color():
    i = randrange(3)
    return [RED, BLUE, WHITE][i]

def get_coords(grid, target_x, target_y, step=1):
    w = len(grid[0])
    h = len(grid)
    lst = []

    for x in range(target_x-step, target_x+step+1):
        for y in range(target_y-step, target_y+step+1):
            if (target_x, target_y) != (x, y) and \
                y >= 0 and y < h and x >=0 and y < w:
                   lst.append((x, y))

    return lst

grid = make_grid(W, H, get_random_color)

for x, y, in get_coords(grid, 5, 5):
    print(x, y)

plt.imshow()
plt.

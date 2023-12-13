from utils.utils import Advent
import numpy as np
from itertools import product
from tqdm import tqdm


advent = Advent(17)

neighbors = [
    (0, 0, 1),
    (0, 0, -1),
    (0, 1, 0),
    (0, 1, 1),
    (0, 1, -1),
    (0, -1, 0),
    (0, -1, 1),
    (0, -1, -1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 0, -1),
    (1, 1, 0),
    (1, 1, 1),
    (1, 1, -1),
    (1, -1, 0),
    (1, -1, 1),
    (1, -1, -1),
    (-1, 0, 0),
    (-1, 0, 1),
    (-1, 0, -1),
    (-1, 1, 0),
    (-1, 1, 1),
    (-1, 1, -1),
    (-1, -1, 0),
    (-1, -1, 1),
    (-1, -1, -1),
]


def main():
    lines = advent.get_input_lines()
    space = np.array([[[c for c in l] for l in lines]], dtype=str)
    for c in tqdm(range(6)):
        space = expand(space)
        to_active, to_inactive = cycle(space)
        for node in to_active:
            space[node] = "#"
        for node in to_inactive:
            space[node] = "."

    # advent.submit(1, len(np.where(space == "#")[0]))


def cycle(space):
    sz, sx, sy = space.shape
    to_active = []
    to_inactive = []
    for z in range(sz):
        for x in range(sx):
            for y in range(sy):
                cube = space[z, x, y]
                an = list(neighbors3d(space, (z, x, y))).count("#")
                if cube == "#" and an not in (2, 3):
                    to_inactive.append((z, x, y))
                elif cube == "." and an == 3:
                    to_active.append((z, x, y))

    return to_active, to_inactive


def expand(space):
    sz, sx, sy = space.shape
    new = np.full((sz + 2, sx + 2, sy + 2), ".", dtype=str)
    new[1:-1, 1:-1, 1:-1] = space
    return new


def neighbors3d(space, node):
    sz, sx, sy = space.shape
    z, x, y = node
    for dz, dx, dy in neighbors:
        if 0 <= z + dz < sz and 0 <= x + dx < sx and 0 <= y + dy < sy:
            yield space[z + dz, x + dx, y + dy]


if __name__ == "__main__":
    main()

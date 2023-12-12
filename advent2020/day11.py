from utils.utils import Advent
from utils.algos import neighbors8

advent = Advent(11)


def main():
    lines = advent.get_input_lines()
    grid = [[c for c in l] for l in lines]
    to_fill, to_empty = to_change(grid)
    while to_fill or to_empty:
        apply_changes(grid, to_fill, to_empty)
        to_fill, to_empty = to_change(grid)

    count = 0
    for row in grid:
        for seat in row:
            if seat == "#":
                count += 1
    advent.submit(1, count)


def apply_changes(grid, to_fill, to_empty):
    for x, y in to_fill:
        grid[x][y] = "#"
    for x, y in to_empty:
        grid[x][y] = "L"


def to_change(grid):
    to_fill = []
    to_empty = []
    for x, row in enumerate(grid):
        for y, seat in enumerate(row):
            if seat == "L":
                if can_fill(grid, (x, y)):
                    to_fill.append((x, y))
            elif seat == "#":
                if must_empty(grid, (x, y)):
                    to_empty.append((x, y))
    return to_fill, to_empty


def must_empty(grid, seat):
    fill_count = 0
    for i, j in neighbors8(grid, seat):
        if grid[i][j] == "#":
            fill_count += 1
            if fill_count >= 4:
                return True
    return False


def can_fill(grid, seat):
    for i, j in neighbors8(grid, seat):
        if grid[i][j] == "#":
            return False
    return True


if __name__ == "__main__":
    main()

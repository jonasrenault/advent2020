from tqdm import tqdm
from utils.utils import Advent
from collections.abc import Iterator

advent = Advent(24)


def main():
    lines = advent.get_input_lines()
    advent.submit(1, len(get_flipped(lines, (0, 0))))


def get_flipped(lines: list[str], start: tuple[int, int]) -> set[tuple[int, int]]:
    blacks = set()
    for instructions in lines:
        tile = move_to(start, instructions)
        if tile in blacks:
            blacks.remove(tile)
        else:
            blacks.add(tile)
    return blacks


def move_to(start: tuple[int, int], instructions: str) -> tuple[int, int]:
    curr = start
    for move in moves(instructions):
        curr = move_one(curr, move)
    return curr


def moves(line) -> Iterator[str]:
    i = 0
    while i < len(line):
        if line[i] == "s" or line[i] == "n":
            yield line[i : i + 2]
            i += 2
        else:
            yield line[i : i + 1]
            i += 1


def move_one(tile: tuple[int, int], dir: str) -> tuple[int, int]:
    x, y = tile
    match dir:
        case "e":
            return (x + 2, y)
        case "ne":
            return (x + 1, y + 1)
        case "nw":
            return (x - 1, y + 1)
        case "w":
            return (x - 2, y)
        case "sw":
            return (x - 1, y - 1)
        case "se":
            return (x + 1, y - 1)


if __name__ == "__main__":
    main()

from utils.utils import Advent
import numpy as np
import numpy.typing as npt
from itertools import combinations
from tqdm import tqdm
from math import prod

advent = Advent(20)


def main():
    lines = advent.get_input_lines()
    tiles = get_tiles(lines)

    pairs_match = {}
    for p1, p2 in tqdm(combinations(tiles.keys(), 2)):
        ep1 = get_edges(tiles[p1]) | get_edges(np.flip(tiles[p1]))
        ep2 = get_edges(tiles[p2]) | get_edges(np.flip(tiles[p2]))
        if ep1 & ep2:
            pairs_match[p1] = pairs_match.get(p1, 0) + 1
            pairs_match[p2] = pairs_match.get(p2, 0) + 1

    # advent.submit(1, prod([k for k, v in pairs_match.items() if v == 2]))


def get_edges(tile: npt.NDArray[np.str_]) -> set[str]:
    edges = (
        tile[0, :],
        tile[-1, :],
        tile[:, 0],
        tile[:, -1],
    )
    res = set(np.array2string(e) for e in edges)
    return res


def get_tiles(lines: list[str]) -> dict[int, npt.NDArray[np.str_]]:
    id = None
    arr = []
    tiles = {}
    for l in lines:
        if l.startswith("Tile"):
            id = int(l[5:-1])
        elif l:
            arr.append([c for c in l])
        else:
            tiles[id] = np.array(arr, dtype=str)
            arr = []
    tiles[id] = np.array(arr, dtype=str)
    return tiles


if __name__ == "__main__":
    main()

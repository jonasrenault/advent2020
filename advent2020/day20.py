from utils.utils import Advent
import numpy as np
import numpy.typing as npt
from itertools import combinations
from collections import defaultdict
from tqdm import tqdm
from math import prod, sqrt
from utils.algos import neighbors

advent = Advent(20)


def main():
    lines = advent.get_input_lines()
    tiles = read_tiles(lines)

    matching_tiles = get_matching_tiles(tiles)
    # corners have only 2 edges
    # advent.submit(1, prod([k for k, v in matching_tiles.items() if len(v) == 2]))

    # # find each piece's place in the puzzle
    # pieces = fit_pieces(pairs_match)
    # print(pieces)

    # # flip / rotate pieces to build the puzzle
    # print(build_puzzle(tiles, pieces))


def build_puzzle(tiles, pieces):
    # place the first corner piece
    corner = tiles[pieces[0, 0]]
    # get the edges for the piece to its right
    # pr_edges = set(get_edges(tiles[pieces[0, 1]])) | set(
    #     get_edges(np.flip(tiles[pieces[0, 1]]))
    # )
    pr_edges = set(get_edges(tiles[pieces[0, 1]]))
    # # do I need to flip it ?
    # if not set(get_edges(corner)) & pr_edges:
    #     corner = np.flip(corner)

    while not (
        np.array2string(corner[:, -1]) in pr_edges
        or np.array2string(np.flip(corner[:, -1])) in pr_edges
    ):
        corner = np.rot90(corner)

    puzzle = []
    row = [
        corner,
    ]
    side = int(sqrt(len(tiles)))
    flipud = False
    for r in range(side):
        if r != 0:
            row = []
        for c in range(side):
            if r == 0 and c == 0:
                continue
            if c == 0:  # match to top
                row.append(
                    match_piece(
                        tiles[pieces[r, c]], puzzle[r - 1][c], True, flipud and r < 2
                    )
                )
            else:  # match to left
                row.append(
                    match_piece(tiles[pieces[r, c]], row[-1], False, flipud and r < 2)
                )

        if r == 0:  # should i flip top row ?
            flipud = np.array2string(corner[0, :]) in set(
                get_edges(tiles[pieces[1, 0]])
            ) | set(get_edges(np.flip(tiles[pieces[1, 0]])))
            if flipud:
                row = [np.flipud(p) for p in row]
        puzzle.append(row)
    return puzzle


def match_piece(piece, other_piece, is_top, flipud):
    # flip piece if it does not match other_piece edges
    # if not set(get_edges(piece)) & set(get_edges(other_piece)):
    #     piece = np.flip(piece)
    if flipud:
        piece = np.flipud(piece)

    # rotate piece until top or left edge matches other_piece
    if is_top:
        while not get_edge(piece, "T") == get_edge(other_piece, "B"):
            piece = np.rot90(piece)
    else:
        while not get_edge(piece, "L") == get_edge(other_piece, "R"):
            piece = np.rot90(piece)

    return piece


def fit_pieces(pairs_match):
    """
    Given list of matching pieces, place them next to each other

    Args:
        pairs_match (_type_): _description_

    Returns:
        _type_: _description_
    """
    side = int(sqrt(len(pairs_match)))
    puzzle = np.zeros((side, side), dtype=int)
    for x in range(side):
        for y in range(side):
            find_piece(pairs_match, puzzle, x, y)

    return puzzle


def find_piece(pairs_match, puzzle, x, y):
    side = int(sqrt(len(pairs_match))) - 1
    pair_length = 4
    if x in (0, side) and y in (0, side):  # corners
        pair_length = 2
    elif x in (0, side) or y in (0, side):  # sides
        pair_length = 3

    nbs = set([puzzle[n] for n in neighbors(puzzle, (x, y)) if puzzle[n] != 0])

    pieces = set(
        [
            k
            for k, v in pairs_match.items()
            if len(v) == pair_length and k not in puzzle and len(nbs.difference(v)) == 0
        ]
    )
    puzzle[x, y] = pieces.pop()


def get_matching_tiles(tiles: dict[int, npt.NDArray[np.str_]]) -> dict[int, list[int]]:
    # find which tiles have matching edges
    matching_tiles = defaultdict(list)
    for p1, p2 in tqdm(combinations(tiles.keys(), 2)):
        ep1 = set(get_edges(tiles[p1])) | set(get_edges(np.flip(tiles[p1])))
        ep2 = set(get_edges(tiles[p2])) | set(get_edges(np.flip(tiles[p2])))
        if ep1 & ep2:
            matching_tiles[p1].append(p2)
            matching_tiles[p2].append(p1)

    return matching_tiles


def get_edges(tile: npt.NDArray[np.str_]) -> list[str]:
    edges = (
        tile[0, :],  # top edge
        tile[:, 0],  # left edge
        tile[-1, :],  # bottom edge
        tile[:, -1],  # right edge
    )
    return [np.array2string(e) for e in edges]


def get_edge(tile: npt.NDArray[np.str_], edge: str) -> str:
    if edge == "T":
        return np.array2string(tile[0, :])
    if edge == "L":
        return np.array2string(tile[:, 0])
    if edge == "R":
        return np.array2string(tile[:, -1])
    return np.array2string(tile[-1, :])


def read_tiles(lines: list[str]) -> dict[int, npt.NDArray[np.str_]]:
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

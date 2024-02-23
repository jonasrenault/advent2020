from utils.utils import Advent
from collections import deque

advent = Advent(22)


def main():
    lines = advent.get_input_lines()
    decks = get_decks(lines)

    while len(decks[0]) > 0 and len(decks[1]) > 0:
        play_round(decks)

    if len(decks[0]) > 0:
        deck = decks[0]
    else:
        deck = decks[1]
    advent.submit(1, sum([x * (len(deck) - i) for i, x in enumerate(deck)]))


def play_round(decks: tuple[deque[int], deque[int]]):
    """
    Play a round

    Args:
        decks (tuple[deque[int], deque[int]]): decks
    """
    l = decks[0].popleft()
    r = decks[1].popleft()
    if l > r:
        decks[0].append(l)
        decks[0].append(r)
    else:
        decks[1].append(r)
        decks[1].append(l)


def get_decks(lines: list[str]) -> tuple[deque[int], deque[int]]:
    """
    Read decks

    Args:
        lines (list[str]): input lines

    Returns:
        tuple[deque[int], deque[int]]: decks
    """
    decks = []
    deck = []
    for line in lines[1:]:
        if not line:
            continue
        if line.startswith("Player"):
            decks.append(deque(deck))
            deck = []
        else:
            deck.append(int(line))
    decks.append(deque(deck))
    return tuple(decks)


if __name__ == "__main__":
    main()

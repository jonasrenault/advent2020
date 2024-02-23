from utils.utils import Advent
from collections import deque
from collections.abc import Iterable

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
    # advent.submit(1, sum([x * (len(deck) - i) for i, x in enumerate(deck)]))

    decks = get_decks(lines)
    play_recursive_game(decks, 1)
    print(decks)


def play_recursive_game(
    decks: tuple[deque[int], deque[int]], game_id: int
) -> tuple[tuple[Iterable[int], Iterable[int]], int]:
    history = set()
    print(f"Playing Game {game_id}")
    game_counts = 0
    while len(decks[0]) > 0 and len(decks[1]) > 0:
        game = ",".join(map(str, decks[0])) + "|" + ",".join(map(str, decks[1]))
        if game in history:
            return ([], [1]), game_counts
        history.add(game)
        game_counts += play_recursive_round(decks, game_id + game_counts)

    print(f"Finished Game {game_id}")
    return decks, game_counts


def play_recursive_round(decks: tuple[deque[int], deque[int]], game_id: int) -> int:
    l = decks[0].popleft()
    r = decks[1].popleft()

    if len(decks[0]) >= l and len(decks[1]) >= r:
        (dl, _), c = play_recursive_game(
            (deque(decks[0]), deque(decks[1])), game_id + 1
        )
        if len(dl) == 0:  # Player1 won
            decks[1].append(r)
            decks[1].append(l)
        else:
            decks[0].append(l)
            decks[0].append(r)
        return 1 + c
    else:  # regular round
        if l > r:
            decks[0].append(l)
            decks[0].append(r)
        else:
            decks[1].append(r)
            decks[1].append(l)
        return 0


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

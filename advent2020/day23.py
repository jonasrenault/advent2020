from utils.utils import Advent
from tqdm import tqdm

advent = Advent(23)


def main():
    lines = advent.get_input_lines()
    cups = [int(c) for c in lines[0]]
    curr = cups[0]
    for _ in tqdm(range(100)):
        cups, curr = move(cups, curr)

    advent.submit(
        1, "".join(map(str, cups[cups.index(1) + 1 :] + cups[: cups.index(1)]))
    )


def move(cups: list[int], current):
    # pick up cups
    curr_idx = cups.index(current)
    pick_up_idx = [(curr_idx + i) % len(cups) for i in range(1, 4)]
    pick_up = [cups[i] for i in pick_up_idx]

    # remove picked_up cups
    for v in pick_up:
        cups.remove(v)

    # pick dest cup
    dest = current - 1
    while dest not in cups:
        dest -= 1
        if dest < min(cups):
            dest = max(cups)

    dest_idx = cups.index(dest)
    cups = cups[: dest_idx + 1] + pick_up + cups[dest_idx + 1 :]
    new_curr = cups[(cups.index(current) + 1) % len(cups)]
    return cups, new_curr


if __name__ == "__main__":
    main()

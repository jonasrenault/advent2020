from utils.utils import Advent

advent = Advent(12)


def main():
    lines = advent.get_input_lines()
    pos = run(lines)
    advent.submit(1, abs(pos[0]) + abs(pos[1]))


DIRS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0),
    90: (1, 0),
    180: (0, -1),
    270: (-1, 0),
    0: (0, 1),
}


def run(instructions: list[str]):
    heading = 90
    pos = (0, 0)
    for i in instructions:
        d = i[0]
        v = int(i[1:])
        if d == "R":
            heading = (heading + v) % 360
        elif d == "L":
            heading = (heading - v) % 360
        elif d == "F":
            offset = DIRS[heading]
            pos = pos[0] + v * offset[0], pos[1] + v * offset[1]
        else:
            offset = DIRS[d]
            pos = pos[0] + v * offset[0], pos[1] + v * offset[1]
    return pos


if __name__ == "__main__":
    main()

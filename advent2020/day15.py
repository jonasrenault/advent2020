from utils.utils import Advent

advent = Advent(15)


def main():
    lines = advent.get_input_lines()
    history = [int(x) for x in lines[0].split(",")]
    history = run(history, 2020)
    # advent.submit(1, history[-1])
    history = [int(x) for x in lines[0].split(",")]
    history = run(history, 30000000)
    history[-1]


def run(history, size):
    while len(history) < size:
        last = history[-1]
        c = history.count(last)
        if c == 1:
            history.append(0)
        else:
            history.append(len(history) - last_index(history[:-1], last) - 1)
    return history


def last_index(l, v):
    i = l[::-1].index(v)
    return len(l) - 1 - i


if __name__ == "__main__":
    main()

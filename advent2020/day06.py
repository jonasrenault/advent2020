from utils.utils import Advent

advent = Advent(6)


def main():
    lines = advent.get_input_lines()
    qs = group_questions(lines)
    c = [len(q) for q in qs]
    advent.submit(1, sum(c))

    qs2 = group_all_questions(lines)
    c2 = [len(q) for q in qs2]
    advent.submit(2, sum(c2))


def group_all_questions(lines: list[str]) -> list[set[str]]:
    qs = []
    q = None
    for line in lines:
        if not line:
            qs.append(q)
            q = None
        else:
            if q is None:
                q = set(line)
            else:
                q = q.intersection(set(line))
    qs.append(q)
    return qs


def group_questions(lines: list[str]) -> list[set[str]]:
    qs = []
    q = set()
    for line in lines:
        if not line:
            qs.append(q)
            q = set()
        else:
            q.update(line)
    qs.append(q)
    return qs


if __name__ == "__main__":
    main()

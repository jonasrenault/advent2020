from utils.utils import Advent

advent = Advent(16)


def main():
    lines = advent.get_input_lines()
    rules, ticket, tickets = parse(lines)
    er = [is_invalid(rules, t) for t in tickets]
    advent.submit(1, sum(er))

    tickets = [ticket] + [t for t in tickets if not is_invalid(rules, t)]
    cols = {}
    possible = set(range(len(ticket)))
    while len(cols) != len(rules):
        start_s = len(possible)
        for k, r in rules.items():
            p = find_possible(possible, r, tickets)
            if len(p) == 1:
                possible = possible - p
                cols[k] = p.pop()
        end_s = len(possible)
        if start_s == end_s:
            break

    val = 1
    for k, c in cols.items():
        if k.startswith("departure"):
            print(f"{k}: {ticket[c]}")
            val *= ticket[c]
    advent.submit(2, val)


def find_possible(
    possible: set[int],
    rule: tuple[tuple[int, int], tuple[int, int]],
    tickets: list[list[int]],
) -> set[int]:
    a, b = rule
    p = set(possible)
    for i in range(len(tickets[0])):
        if i in p:
            for t in tickets:
                v = t[i]
                if not (a[0] <= v <= a[1] or b[0] <= v <= b[1]):
                    p.remove(i)
                    break
    return p


def is_invalid(
    rules: dict[str, tuple[tuple[int, int], tuple[int, int]]], ticket: list[int]
) -> int:
    for val in ticket:
        for a, b in rules.values():
            if a[0] <= val <= a[1] or b[0] <= val <= b[1]:
                break
        else:
            return val
    return 0


def parse(
    lines: list[str],
) -> tuple[
    dict[str, tuple[tuple[int, int], tuple[int, int]]], list[int], list[list[int]]
]:
    rules = {}
    ticket = None
    tickets = []
    for l in lines:
        if l and not l[0].isdigit() and "ticket" not in l:
            rule = l[: l.index(":")]
            r0, r1 = l[l.index(":") + 1 :].split("or")
            r0 = tuple(int(x.strip()) for x in r0.split("-"))
            r1 = tuple(int(x.strip()) for x in r1.split("-"))
            rules[rule] = (r0, r1)
        elif l and l[0].isdigit() and ticket is None:
            ticket = [int(x) for x in l.split(",")]
        elif l and l[0].isdigit():
            tickets.append([int(x) for x in l.split(",")])
    return rules, ticket, tickets


if __name__ == "__main__":
    main()

from utils.utils import Advent

advent = Advent(16)


def main():
    lines = advent.get_input_lines()
    rules, ticket, tickets = parse(lines)
    er = [is_invalid(rules, t) for t in tickets]
    advent.submit(1, sum(er))


def is_invalid(rules, ticket) -> int:
    for val in ticket:
        for a, b in rules.values():
            if a[0] <= val <= a[1] or b[0] <= val <= b[1]:
                break
        else:
            return val
    return 0


def parse(lines):
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

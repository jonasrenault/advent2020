from utils.utils import Advent

advent = Advent(19)


def main():
    lines = advent.get_input_lines()
    rules, messages = parse(lines)

    c = 0
    for m in messages:
        if len(m) == matched(rules, "0", m):
            c += 1
    advent.submit(1, c)


def matched(rules, rule: str, message: str):
    ors = rules[rule]
    if len(ors) == 1:
        ands = ors[0]
        if not ands[0].isdigit():
            # end case, check first char matches a or b
            if message[0] == ands[0]:
                return 1
            return -1
        else:
            return match_ands(rules, ands, message)
    else:
        for ands in ors:
            c = match_ands(rules, ands, message)
            if c > 0:
                return c
        return -1


def match_ands(rules, ands: list[str], message: str):
    c = 0
    for r in ands:
        m = matched(rules, r, message[c:])
        if m < 0:
            return -1
        c += m
    return c


def parse(lines):
    rules = {}
    messages = []
    for line in lines:
        if not line:
            continue
        if line[0].isdigit():
            key = line[: line.index(":")]
            rule = line[line.index(":") + 1 :].replace('"', "")
            alts = rule.split("|")
            alts = [[x.strip() for x in r.strip().split(" ")] for r in alts]
            rules[key] = alts
        else:
            messages.append(line)

    return rules, messages


if __name__ == "__main__":
    main()

from utils.utils import Advent

advent = Advent(4)

KEYS = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def main():
    lines = advent.get_input_lines()
    passports = get_passports(lines)
    c = [p for p in passports if all([k in p for k in KEYS])]
    advent.submit(1, len(c))

    c = 0
    for p in passports:
        try:
            is_valid(p)
            c += 1
        except Exception:
            continue
    advent.submit(2, c)


def is_valid(p: dict[str, str]) -> bool:
    assert 1920 <= int(p["byr"]) <= 2002
    assert 2010 <= int(p["iyr"]) <= 2020
    assert 2020 <= int(p["eyr"]) <= 2030
    if "cm" in p["hgt"]:
        assert 150 <= int(p["hgt"][:-2]) <= 193
    elif "in" in p["hgt"]:
        assert 59 <= int(p["hgt"][:-2]) <= 76
    else:
        raise ValueError("invalid hgt")
    assert p["hcl"][0] == "#" and len(p["hcl"]) == 7
    assert p["hcl"].lower() == p["hcl"] and p["hcl"][1:].isalnum()
    assert p["ecl"] in ("amb blu brn gry grn hzl oth".split(" "))
    assert len(p["pid"]) == 9 and all([c.isdigit() for c in p["pid"]])
    return True


def get_passports(lines: list[str]) -> list[dict[str, str]]:
    passports = []
    passport = {}
    for line in lines:
        if not line:
            passports.append(passport)
            passport = {}
        else:
            kvs = [e.split(":") for e in line.split(" ")]
            for k, v in kvs:
                passport[k] = v
    passports.append(passport)
    return passports


if __name__ == "__main__":
    main()

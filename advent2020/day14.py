from utils.utils import Advent

advent = Advent(14)


def main():
    lines = advent.get_input_lines()
    memory = run(lines)
    advent.submit(1, sum(memory.values()))


def run(lines: list[str]) -> dict[str, int]:
    mask = None
    memory = {}
    for line in lines:
        if line.startswith("mask"):
            mask = line[7:]
        else:
            mem = line[line.index("[") + 1 : line.index("]")]
            val = int(line[line.index("=") + 2 :])
            binv = str(bin(val))[2:]
            val = int(apply_mask(mask, binv), 2)
            memory[mem] = val
    return memory


def apply_mask(mask: str, binv: str) -> str:
    val = ""
    for i in range(1, len(mask) + 1):
        if mask[-i] != "X":
            val += mask[-i]
        elif i > len(binv):
            val += "0"
        else:
            val += binv[-i]
    return val[::-1]


if __name__ == "__main__":
    main()

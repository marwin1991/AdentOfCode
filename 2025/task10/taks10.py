FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def parse_line(line):
    diag_part, rest = line.split("]", 1)
    diag = diag_part.strip()[1:]
    target = [1 if c == "#" else 0 for c in diag]
    buttons = []

    i = 0
    while True:
        start = rest.find("(", i)
        if start == -1:
            break
        end = rest.find(")", start)
        group = rest[start+1:end]
        if group.strip():
            buttons.append([int(x) for x in group.split(",")])
        i = end + 1

    return target, buttons

def solve_machine(target, buttons):
    n = len(target)
    m = len(buttons)
    best = None

    # brute-force minimal Hamming-weight solution over GF(2)
    # 2^m buttons; m is small in AoC input
    for mask in range(1 << m):
        presses = bin(mask).count("1")

        if best is not None and presses >= best:
            continue
        state = [0] * n

        for b in range(m):
            if (mask >> b) & 1:
                for idx in buttons[b]:
                    state[idx] ^= 1
        if state == target:
            best = presses

    return best

def main():
    lines = [l.strip() for l in read_file() if l.strip()]
    total = 0

    for line in lines:
        target, buttons = parse_line(line)
        total += solve_machine(target, buttons)
    print(total)

if __name__ == '__main__':
    main()

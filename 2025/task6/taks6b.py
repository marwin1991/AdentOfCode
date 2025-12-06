FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def split_n(s, n):
    return [s[i:i + n] for i in range(0, len(s), n)]


def main():
    lines = read_file()
    numbers = []

    for line in lines:
        row = line.split()
        numbers.append(row)

    print(numbers)

    numeric_rows = []
    operator_row = None

    for row in numbers:
        if all(x.isdigit() for x in row):
            numeric_rows.append(list(map(int, row)))
        else:
            operator_row = row

    max_len = max(len(line) for line in lines)
    padded = [line.ljust(max_len) for line in lines[:-1]]

    columns = [''.join(row[col] for row in padded) for col in range(max_len)]

    problems = []
    current = []

    for col in columns:
        if col.strip() == "":
            if current:
                problems.append(current)
                current = []
        else:
            current.append(col)

    if current:
        problems.append(current)

    results = []

    for col, op in zip(problems, operator_row):
        if op == "+":
            col_sum = 0
            for n in col:
                col_sum += int(n)
            results.append(col_sum)
        elif op == "*":
            prod = 1
            for n in col:
                prod *= int(n)
            results.append(prod)
        else:
            raise ValueError(f"Unknown operator: {op}")

    print(problems)

    total = 0
    for r in results:
        total += r

    print("total:", total)


if __name__ == '__main__':
    main()

FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


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

    columns = list(zip(*numeric_rows))

    results = []
    for col, op in zip(columns, operator_row):
        if op == "+":
            results.append(sum(col))
        elif op == "*":
            prod = 1
            for n in col:
                prod *= n
            results.append(prod)
        else:
            raise ValueError(f"Unknown operator: {op}")

    total = 0

    for r in results:
        total += r

    print("total:", total)

if __name__ == '__main__':
    main()

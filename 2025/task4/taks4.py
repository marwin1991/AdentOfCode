FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def can_take(elements: list):
    counter = 0
    for e in elements:
        if e == "@" or e == "x":
            counter += 1

    return counter < 4


def main():
    rows = read_file()

    table_2d = []  # columns [row][col]
    row_counter = 0
    for row in rows:
        row_table = list(row.strip())
        row_table.insert(0, ".")
        row_table.append(".")
        table_2d.append(row_table)
        row_counter += 1

    col_counter = len(rows[1]) + 2
    last_row = ["." for _ in range(col_counter)]

    table_2d.insert(0, last_row)
    table_2d.insert(row_counter + 1, last_row)

    prev_x_counter = -1
    x_counter = 0

    while prev_x_counter != x_counter:
        prev_x_counter = x_counter

        for row_idx in range(len(table_2d)):
            for col_idx in range(len(table_2d[row_idx])):
                if table_2d[row_idx][col_idx] == "@" and can_take([
                    table_2d[row_idx - 1][col_idx - 1], table_2d[row_idx - 1][col_idx], table_2d[row_idx - 1][col_idx + 1],
                    table_2d[row_idx][col_idx - 1], table_2d[row_idx][col_idx + 1],
                        table_2d[row_idx + 1][col_idx - 1], table_2d[row_idx + 1][col_idx], table_2d[row_idx + 1][col_idx + 1]]):
                    table_2d[row_idx][col_idx] = "x"
                    x_counter += 1

        for row_idx in range(len(table_2d)):
            for col_idx in range(len(table_2d[row_idx])):
                if table_2d[row_idx][col_idx] == "x":
                    table_2d[row_idx][col_idx] = "."


    for row_idx in range(len(table_2d)):
        for col_idx in range(len(table_2d[row_idx])):
            print(table_2d[row_idx][col_idx], end="")
        print()

    print(f"x counter: {x_counter}")


if __name__ == '__main__':
    main()

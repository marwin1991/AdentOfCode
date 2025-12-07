FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def tachion_move(table_2d, row, col):
    if row == len(table_2d) - 1:
        return

    if table_2d[row+1][col] == ".":
        table_2d[row+1][col] = "|"
        tachion_move(table_2d, row + 1, col)

    if table_2d[row+1][col] == "^":
        tachion_move.counter += 1

        table_2d[row+1][col-1] = "|"
        tachion_move(table_2d, row + 1, col-1)

        table_2d[row+1][col+1] = "|"
        tachion_move(table_2d, row + 1, col+1)

tachion_move.counter = 0


def main():
    lines = read_file()

    table_2d = []  # table_2d [row][col]

    for row in lines:
        row_table = list(row.strip())
        table_2d.append(row_table)

    s_col = table_2d[0].index("S")

    tachion_move(table_2d, 0, s_col)

    for row in table_2d:
        print("".join(row))

    print(tachion_move.counter)



if __name__ == '__main__':
    main()

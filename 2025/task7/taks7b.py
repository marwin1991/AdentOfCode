FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def tachion_move(table_2d, row, col):
    if row == len(table_2d) - 1:
        return

    if table_2d[row + 1][col] == ".":
        table_2d[row + 1][col] = "|"
        tachion_move(table_2d, row + 1, col)

    if table_2d[row + 1][col] == "^":
        tachion_move.counter += 1

        table_2d[row + 1][col - 1] = "|"
        tachion_move(table_2d, row + 1, col - 1)

        table_2d[row + 1][col + 1] = "|"
        tachion_move(table_2d, row + 1, col + 1)


tachion_move.counter = 0

global col_max
global row_max
global table_2d


def ok(table_2d, row, col):
    return 0 <= row < row_max and 0 <= col < col_max and table_2d[row][col] == "|"


from functools import lru_cache


@lru_cache(None) # to jakiś pojebany game changer z 1h do 2sekund????
def dfs(row, col):
    global table_2d

    if row == row_max - 1:
        print("found 1 path, dfs rec counter = ", dfs.rec_counter, "")
        return 1

    total = 0

    if table_2d[row + 1][col] == "^":
        for d_col in (-1, 1):
            new_row, new_col = row + 1, col + d_col
            if ok(table_2d, new_row, new_col):
                dfs.rec_counter += 1
                print(f"total: {total}  - dfs rec counter: {dfs.rec_counter}")
                total += dfs(new_row, new_col)

    if table_2d[row + 1][col] == "|":
        for d_col in [0]:
            new_row, new_col = row + 1, col + d_col
            if ok(table_2d, new_row, new_col):
                dfs.rec_counter += 1
                print(f"total: {total}  - dfs rec counter: {dfs.rec_counter}")
                total += dfs(new_row, new_col)

    print(f"return total: {total}  - dfs rec counter: {dfs.rec_counter}")
    return total


dfs.rec_counter = 0


def main():
    lines = read_file()

    global table_2d
    table_2d = []  # table_2d [row][col]

    for row in lines:
        row_table = list(row.strip())
        table_2d.append(row_table)

    global col_max
    global row_max
    col_max = len(table_2d[0])
    row_max = len(table_2d)

    s_col = table_2d[0].index("S")

    tachion_move(table_2d, 0, s_col)

    for row in table_2d:
        print("".join(row))

    print(tachion_move.counter)
    print(dfs(0, s_col))


if __name__ == '__main__':
    main()

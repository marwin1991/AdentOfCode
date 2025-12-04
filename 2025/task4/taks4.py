FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def can_take(elements: list):
    counter = 0
    for e in elements:
        if e == "@":
            counter += 1

    return counter < 4


def main():
    rows = read_file()

    table_2d = [] # columns [row][col]
    for row in rows:
        row_table = list(row.strip())
        table_2d.append(row_table)

    x_counter = 0

    for row_idx in range(len(table_2d)):
        for col_idx in range(len(table_2d[row_idx])):

            if row_idx == 0 and col_idx == 0:
                if table_2d[row_idx][col_idx] == "@":
                    table_2d[row_idx][col_idx] = "x"
                    x_counter += 1

            if row_idx == 0 and col_idx == len(table_2d[row_idx]) - 1:
                if table_2d[row_idx][col_idx] == "@":
                    table_2d[row_idx][col_idx] = "x"
                    x_counter += 1

            if row_idx == 0:
                if table_2d[row_idx][col_idx] == "@" and can_take([table_2d[row_idx][col_idx-1], table_2d[row_idx][col_idx+1], table_2d[row_idx-1][col_idx-1], table_2d[row_idx-1][col_idx], table_2d[row_idx-1][col_idx+1]]):
                    table_2d[row_idx][col_idx] = "x"
                    x_counter += 1


    for row_idx in range(len(table_2d)):
        for col_idx in range(len(table_2d[row_idx])):
            print(table_2d[row_idx][col_idx], end="")
        print()




if __name__ == '__main__':
    main()


FILE_PATH = "input-test.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def rectangle_area(p1, p2):
    x, y = p1
    x1, y1 = p2
    return (abs(x1 - x) + 1) * (abs(y1 - y) + 1)

def min_max(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), max(xs), min(ys), max(ys)

def make_table(points):
    min_x, max_x, min_y, max_y = min_max(points)
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1

    grid = []
    point_set = set(points)
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            row += "#" if (x, y) in point_set else "."
        grid.append(list(row))
    return grid

def main():
    lines = read_file()
    coords_base = []

    for row in lines:
        xy = row.strip().split(",")
        coords_base.append((int(xy[0]), int(xy[1])))

    grid = make_table(coords_base)
    for row in grid:
        print(row)

    print("Largest value:", 1)



if __name__ == '__main__':
    main()

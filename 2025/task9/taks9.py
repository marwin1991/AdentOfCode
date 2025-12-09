FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def rectangle_area(p1, p2):
    x, y = p1
    x1, y1 = p2
    return (abs(x1 - x) + 1) * (abs(y1 - y) + 1)


def main():
    lines = read_file()
    coords_base = []

    for row in lines:
        xy = row.strip().split(",")
        coords_base.append((int(xy[0]), int(xy[1])))

    coords = []
    ares = []

    for i in range(len(coords_base)):
        for j in range(len(coords_base)):
            if i != j:
                ares.append(rectangle_area(coords_base[i], coords_base[j]))


    largest = max(ares)

    print("Largest value:", largest)



if __name__ == '__main__':
    main()

from collections import deque

FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def rectangle_area(p1, p2, grid):
    x, y = p1
    x1, y1 = p2
    xmin, xmax = min(x, x1), max(x, x1)
    ymin, ymax = min(y, y1), max(y, y1)
    h = len(grid)
    w = len(grid[0])
    for yy in range(ymin, ymax + 1):
        for xx in range(xmin, xmax + 1):
            gy = h - 1 - yy
            gx = xx
            if gy < 0 or gy >= h or gx < 0 or gx >= w:
                return 0
            if grid[gy][gx] != True:
                return 0
    return (abs(x1 - x) + 1) * (abs(y1 - y) + 1)


def min_max(points):
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    return min(xs), max(xs), min(ys), max(ys)


def connect_points(points):
    segments = set(points)
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % n]
        if x1 == x2:
            step = 1 if y2 > y1 else -1
            for y in range(y1, y2 + step, step):
                segments.add((x1, y))
        elif y1 == y2:
            step = 1 if x2 > x1 else -1
            for x in range(x1, x2 + step, step):
                segments.add((x, y1))
    return segments

import numpy as np

def make_table(points):
    segments = connect_points(points)
    min_x, max_x, min_y, max_y = min_max(list(segments))

    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1

    ###

    # for y in range(max_y, min_y - 1, -1):
    #     row = ""
    #     for x in range(min_x, max_x + 1):
    #         if (x, y) in points:
    #             row += "#"
    #         elif (x, y) in segments:
    #             row += "X"
    #         else:
    #             row += "."
    #     grid.append(list(row))
    #     print(f"gen new grid line {max_y-y}/{max_y}")
    ###

    grid = np.full((max_y - min_y + 1, max_x - min_x + 1), False, dtype=bool)
    for x, y in points:
        grid[max_y - y, x - min_x] = True
    for x, y in segments:
        if grid[max_y - y, x - min_x] == False:
            grid[max_y - y, x - min_x] = True
        print(f"gen new grid line {max_y-y}/{max_y}")

    print("FINISHED GENERATING GRID")
    h = len(grid)
    w = len(grid[0])
    q = deque()

    visited = np.full((h, w), False, dtype=bool)

    i = 0
    for i in range(w):
        q.append((0, i))
        q.append((h - 1, i))
    for i in range(h):
        q.append((i, 0))
        q.append((i, w - 1))
    while q:
        y, x = q.popleft()
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        if visited[y][x]:
            continue
        if grid[y][x] == True:
            continue
        visited[y][x] = True
        q.append((y + 1, x))
        q.append((y - 1, x))
        q.append((y, x + 1))
        q.append((y, x - 1))

        i+=1
        if i % 100000 == 0:
            print(f"flooded iteration {i}/{w*h}")

    print("FINISHED GENERATING FLOOD")
    for y in range(h):
        for x in range(w):
            if grid[y][x] == False and not visited[y][x]:
                grid[y][x] = True
        print(f"gen new grid line flooded {y}/{h}")

    print("FINISHED MARKING FLOOD")
    return grid


def main():
    lines = read_file()
    coords_base = []

    for row in lines:
        xy = row.strip().split(",")
        coords_base.append((int(xy[0]), int(xy[1])))

    grid = make_table(coords_base)

    ares = []

    max_iters = len(coords_base) * len(coords_base)
    for i in range(len(coords_base)):
        for j in range(len(coords_base)):
            if i != j:
                print(f"testing rect {(i+1)*(j+1)}/{max_iters}")
                ares.append(rectangle_area(coords_base[i], coords_base[j], grid))

    largest = max(ares)

    print("Largest value:", largest)


if __name__ == '__main__':
    main()

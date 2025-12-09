from operator import itemgetter

FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def rectangle_area_base(p1, p2):
    x, y = p1
    x1, y1 = p2
    return (abs(x1 - x) + 1) * (abs(y1 - y) + 1), p1, p2


def rectangle_area(p1, p2, grid):
    x, y = p1
    x1, y1 = p2
    xmin, xmax = min(x, x1), max(x, x1)
    ymin, ymax = min(y, y1), max(y, y1)
    h = len(grid)
    w = len(grid[0])
    for yy in range(ymin, ymax + 1):
        if yy == ymin or yy == ymax:
            for xx in range(xmin, xmax + 1):
                gy = h - 1 - yy
                gx = xx
                if gy < 0 or gy >= h or gx < 0 or gx >= w:
                    return 0
                if grid[gy][gx] == True:
                    return 0
        else:
            for xx in (xmin, xmax):
                gy = h - 1 - yy
                gx = xx
                if gy < 0 or gy >= h or gx < 0 or gx >= w:
                    return 0
                if grid[gy][gx] == True:
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
from collections import deque

def flood4(grid):
    h, w = grid.shape
    visited = np.zeros((h, w), dtype=bool)
    q = deque()

    for x in range(w):
        if not grid[0, x]:
            visited[0, x] = True
            q.append((0, x))
        if not grid[h-1, x]:
            visited[h-1, x] = True
            q.append((h-1, x))

    for y in range(1, h-1):
        if not grid[y, 0]:
            visited[y, 0] = True
            q.append((y, 0))
        if not grid[y, w-1]:
            visited[y, w-1] = True
            q.append((y, w-1))

    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

    iteration_count = 0
    while q:
        iteration_count += 1
        y, x = q.popleft()

        for dy, dx in directions:
            ny, nx = y + dy, x + dx

            if 0 <= ny < h and 0 <= nx < w and not visited[ny, nx] and not grid[ny, nx]:
                visited[ny, nx] = True  # Mark BEFORE enqueuing
                q.append((ny, nx))

        if iteration_count % 1000000 == 0:
            print(f"flooded iteration {iteration_count}/{w*h} -- {len(q)}")

    return visited

def make_table(points):
    segments = connect_points(points)
    min_x, max_x, min_y, max_y = min_max(list(segments))

    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1

    grid = np.full((max_y - min_y + 1, max_x - min_x + 1), False, dtype=bool)
    for x, y in points:
        grid[max_y - y, x - min_x] = True
    for x, y in segments:
        if grid[max_y - y, x - min_x] == False:
            grid[max_y - y, x - min_x] = True
        print(f"gen new grid line {max_y-y}/{max_y}")

    print("FINISHED GENERATING GRID")
    visited = flood4(grid)
    print("FINISHED GENERATING FLOOD")
    return visited


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
                ares.append(rectangle_area_base(coords_base[i], coords_base[j]))

    largest_list = sorted(ares, key=itemgetter(0), reverse=True)

    r = None
    for r in largest_list:
        if rectangle_area(r[1], r[2], grid) != 0:
            print(r)
            break

    print("Largest value:", r)


if __name__ == '__main__':
    main()

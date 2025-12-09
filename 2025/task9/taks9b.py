from collections import deque

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

def make_table(points):
    segments = connect_points(points)
    min_x, max_x, min_y, max_y = min_max(list(segments))
    min_x -= 1
    min_y -= 1
    max_x += 1
    max_y += 1
    grid = []
    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in points:
                row += "#"
            elif (x, y) in segments:
                row += "X"
            else:
                row += "."
        grid.append(list(row))
    h = len(grid)
    w = len(grid[0])
    q = deque()
    visited = [[False]*w for _ in range(h)]
    for i in range(w):
        q.append((0, i))
        q.append((h-1, i))
    for i in range(h):
        q.append((i, 0))
        q.append((i, w-1))
    while q:
        y, x = q.popleft()
        if x < 0 or x >= w or y < 0 or y >= h:
            continue
        if visited[y][x]:
            continue
        if grid[y][x] in ("#", "X"):
            continue
        visited[y][x] = True
        q.append((y+1, x))
        q.append((y-1, x))
        q.append((y, x+1))
        q.append((y, x-1))
    for y in range(h):
        for x in range(w):
            if grid[y][x] == "." and not visited[y][x]:
                grid[y][x] = "X"
    return grid

def main():
    lines = read_file()
    coords_base = []

    for row in lines:
        xy = row.strip().split(",")
        coords_base.append((int(xy[0]), int(xy[1])))

    grid = make_table(coords_base)
    for row in reversed(grid):
        print(row)

    print("Largest value:", 1)



if __name__ == '__main__':
    main()

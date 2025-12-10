from operator import itemgetter

FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def rectangle_area(p1, p2):
    x, y = p1
    x1, y1 = p2
    return (abs(x1 - x) + 1) * (abs(y1 - y) + 1), p1, p2

def rectangle_edges(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if x1 == x2 or y1 == y2:
        return []

    v1 = (x1, y1)
    v2 = (x1, y2)
    v3 = (x2, y2)
    v4 = (x2, y1)
    return [(v1, v2), (v2, v3), (v3, v4), (v4, v1)]

def points_to_segments(points):
    return [ (points[i], points[(i+1) % len(points)]) for i in range(len(points)) ]

def is_point_inside_polygon(point, polygon_lines):
    x, y = point

    def orient(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

    def on_segment(p, q, r):
        return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and \
            min(p[1], r[1]) <= q[1] <= max(p[1], r[1])

    for (x1, y1), (x2, y2) in polygon_lines:
        if orient((x1, y1), (x2, y2), (x, y)) == 0 and on_segment((x1, y1), (x, y), (x2, y2)):
            return True

    count = 0
    for (x1, y1), (x2, y2) in polygon_lines:
        if (y1 > y) != (y2 > y):
            xinters = (y - y1) * (x2 - x1) / (y2 - y1) + x1
            if x < xinters:
                count += 1

    return count % 2 == 1

def segments_intersect_inside(a, b, c, d):
    def orient(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])

    o1 = orient(a, b, c)
    o2 = orient(a, b, d)
    o3 = orient(c, d, a)
    o4 = orient(c, d, b)

    if o1 * o2 < 0 and o3 * o4 < 0:
        return True

    return False

def rectangle_inside(figure_lines, r_edges):

    vertices = [edge[0] for edge in r_edges]
    for v in vertices:
        if not is_point_inside_polygon(v, figure_lines):
            return False

    for e1 in r_edges:
        for e2 in figure_lines:
            if segments_intersect_inside(e1[0], e1[1], e2[0], e2[1]):
                return False

    return True

def main():
    lines = read_file()
    coords_base = []

    for row in lines:
        xy = row.strip().split(",")
        coords_base.append((int(xy[0]), int(xy[1])))


    ares = []

    for i in range(len(coords_base)):
        for j in range(len(coords_base)):
            if i != j:
                ares.append(rectangle_area(coords_base[i], coords_base[j]))

    figure_lines = points_to_segments(coords_base)

    largest_list = sorted(ares, key=itemgetter(0), reverse=True)

    largest_inside = None

    max_i = len(largest_list)
    i=0
    for r in largest_list:
        i+=1
        print(f"{i} / {max_i}:")
        r_edges = rectangle_edges(r[1], r[2])
        if r_edges == []:
            continue
        if rectangle_inside(figure_lines, r_edges):
            largest_inside = r
            break

    print("Largest value:", largest_inside)


if __name__ == '__main__':
    main()

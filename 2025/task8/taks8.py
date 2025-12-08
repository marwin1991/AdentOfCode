import math
from operator import itemgetter

FILE_PATH = "input.txt"

MAX = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def distance(c1, c2):
    return math.sqrt((c2[0] - c1[0]) ** 2 + (c2[1] - c1[1]) ** 2 + (c2[2] - c1[2]) ** 2)

def is_connected(c1, c2):
    for p in c1[4]:
        if p in c2[4]:
            return True

    return False


def closest_point(coords, i):
    c_name = "c_" + str(i)
    p_name = "p_" + str(i)
    closest_point1_idx = None
    closest_point2_idx = None
    closest_dist = MAX

    for c1_idx in range(len(coords)):
        for c2_idx in range(len(coords)):
            if c1_idx != c2_idx:
                if ((coords[c1_idx][3] is None or coords[c2_idx][3] is None)
                        or (coords[c1_idx][3] != coords[c2_idx][3])
                        or (coords[c1_idx][3] == coords[c2_idx][3] and not is_connected(coords[c1_idx], coords[c2_idx]))):
                    dist = distance(coords[c1_idx], coords[c2_idx])
                    if dist <= closest_dist:
                        closest_dist = dist
                        closest_point1_idx = c1_idx
                        closest_point2_idx = c2_idx

    if closest_dist != MAX:

        coords[closest_point1_idx][4].append(p_name)
        coords[closest_point2_idx][4].append(p_name)

        if coords[closest_point1_idx][3] is not None and coords[closest_point2_idx][3] is not None and coords[closest_point1_idx][3] == coords[closest_point2_idx][3]:
            print(f"same circut already {coords[closest_point1_idx][3]} - closest points: {coords[closest_point1_idx]} {coords[closest_point2_idx]}")
            return coords[closest_point1_idx], coords[closest_point2_idx], closest_point

        if coords[closest_point1_idx][3] is None and coords[closest_point2_idx][3] is None:
            coords[closest_point1_idx][3] = c_name
            coords[closest_point2_idx][3] = c_name
        elif coords[closest_point1_idx][3] is not None and coords[closest_point2_idx][3] is None:
            coords[closest_point2_idx][3] = coords[closest_point1_idx][3]
        elif coords[closest_point1_idx][3] is None and coords[closest_point2_idx][3] is not None:
            coords[closest_point1_idx][3] = coords[closest_point2_idx][3]
        else:
            change_from = coords[closest_point1_idx][3]
            change_to = coords[closest_point2_idx][3]
            print(f"--------------- changing {change_from} to {change_to}")
            for c in coords:
                if c[3] == change_from:
                    print(f"change made from {c[3]} to {change_to}")
                    c[3] = change_to

        print(f"closest points: {coords[closest_point1_idx]} {coords[closest_point2_idx]}")
        return coords[closest_point1_idx], coords[closest_point2_idx], closest_point

    return None, None, None

I = 1000

def main():
    lines = read_file()

    coords = []

    for row in lines:
        xyz = row.strip().split(",")
        #                                                    final circut, connections
        coords.append([int(xyz[0]), int(xyz[1]), int(xyz[2]), None , []])

    for i in range(I):
        closest_point(coords, i)

    circuts = []
    for i in range(I):
        circuts.append(["c_" + str(i), 0])


    for i in range(I):
        for c in coords:
            if c[3] == "c_" + str(i):
                circuts[i][1] += 1


    circuts = sorted(circuts, key=itemgetter(1), reverse=True)

    for c in coords:
        print(c)


    for c in circuts:
        print(c)

    print("Result: " + str(circuts[0][1] * circuts[1][1] * circuts[2][1]))

    print(distance([0,0,0], [0,0,1]))


if __name__ == '__main__':
    main()

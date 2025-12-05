from operator import itemgetter

FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def main():
    lines = read_file()
    ranges = []
    numbers = []

    is_numbers = False

    for line in lines:
        if line.strip() == "":
            is_numbers = True
            continue

        if is_numbers:
            numbers.append(int(line.strip()))
        else:
            range_numbers = line.strip().split("-")
            ranges.append((int(range_numbers[0]), int(range_numbers[1])))

    # ranges = [(3,5), (10,14), (16,20), (12,18), (3, 3)]

    ranges = sorted(ranges, key=itemgetter(0))

    is_change = True
    final_new_ranges = []
    original_ranges = ranges.copy()

    while is_change:
        is_change = False
        new_ranges = []

        range_idx = 0
        while range_idx < len(ranges):
            if range_idx != len(ranges) - 1 and ranges[range_idx][1] >= ranges[range_idx + 1][0]:
                if ranges[range_idx + 1][1] >= ranges[range_idx][1]:
                    new_ranges.append((ranges[range_idx][0], ranges[range_idx + 1][1]))
                    range_idx += 2
                    is_change = True
                else:
                    print(f"Next range {ranges[range_idx + 1]} is included in current range end {ranges[range_idx]}")
                    new_ranges.append(ranges[range_idx])
                    range_idx += 2
                    is_change = True
            else:
                new_ranges.append(ranges[range_idx])
                range_idx += 1

        final_new_ranges = new_ranges.copy()
        ranges = new_ranges.copy()

    print(len(original_ranges))
    print(len(final_new_ranges))

    sum_all = 0

    for r in final_new_ranges:
        sum_all += r[1] - r[0] + 1

    print(f"sum all: {sum_all}") # 296656343488847



if __name__ == '__main__':
    main()

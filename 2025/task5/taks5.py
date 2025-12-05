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
            ranges.append((range_numbers[0], range_numbers[1]))

    fresh_counter = 0

    for number in numbers:
        for r in ranges:
            if int(r[0]) <= number <= int(r[1]):
                fresh_counter += 1
                break


    print(f"fresh counter: {fresh_counter}")


if __name__ == '__main__':
    main()

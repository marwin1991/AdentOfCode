FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readline()

def split(string, n):
    out = []
    for i in range(0, len(string), n):
        out.append(string[i:i+n])
    return out

def is_sequence(str_number, prefix):
    if len(str_number) == 1:
        return False

    if len(prefix) > len(str_number):
        return False


    chunks = split(str_number, len(prefix))

    for c in chunks:
        if c != prefix:
            return False

    return True

def is_invalid(number):
    str_number = str(number)
    length = len(str_number)

    for i in range(1, max(length//2,1) + 1):
        if is_sequence(str_number, str_number[:i]):
            return True

    return False


def main():
    line = read_file()
    ranges = line.split(",")
    invalid_count = 0
    invalid_sum = 0
    for r in ranges:
        print("-------------------")
        print(r)

        numbers = r.split("-")
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        for i in range(n1, n2+1):
            if is_invalid(i):
                invalid_count += 1
                invalid_sum += i
                print(f"{i} is invalid")

    print(f"invalid count: {invalid_count}")
    print(f"invalid sum: {invalid_sum}")

if __name__ == '__main__':
    main()


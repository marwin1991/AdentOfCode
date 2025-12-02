FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readline()

def is_invalid(number):
    str_number = str(number)
    firstpart, secondpart = str_number[:len(str_number)//2], str_number[len(str_number)//2:]
    return firstpart == secondpart

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
            if len(str(i)) % 2 == 0:
                if is_invalid(i):
                    invalid_count += 1
                    invalid_sum += i
                    print(f"{i} is invalid")

    print(f"invalid count: {invalid_count}")
    print(f"invalid sum: {invalid_sum}")

if __name__ == '__main__':
    main()


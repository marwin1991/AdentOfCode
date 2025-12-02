FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readline()

def main():
    line = read_file()
    ranges = line.split(",")
    for r in ranges:
        print("-------------------")
        print(r)

        numbers = r.split("-")
        n1 = int(numbers[0])
        n2 = int(numbers[1])

        for i in range(n1, n2+1):
            print(i)


if __name__ == '__main__':
    main()


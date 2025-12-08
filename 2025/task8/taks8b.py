FILE_PATH = "input.txt"


def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def main():
    lines = read_file()




if __name__ == '__main__':
    main()

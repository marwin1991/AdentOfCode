
FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def main():
    instructions = read_file()
    print(len(instructions))
    state = 50
    time_pointing_zero = 0
    for instruction in instructions:
        if instruction.startswith('L'):
           state -= int(instruction[1:])
        else:
            state += int(instruction[1:])

        if state > 99:
            state -= 100
        if state < 0:
            state += 100

        print(f"{instruction} --> {state}")

        if state == 0:
            time_pointing_zero+=1

    print("=========================")
    print(time_pointing_zero)



if __name__ == '__main__':
    main()
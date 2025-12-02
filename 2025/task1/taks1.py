
FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()


def main():
    instructions = read_file()

    state = 50
    times_pointing_zero = 0
    times_passes_zero = 0
    for instruction in instructions:
        print(f"-------------------{instruction}beginning state: {state}")
        start_state = state
        if instruction.startswith('L'):
            state -= int(instruction[1:].strip())
        else:
            state += int(instruction[1:].strip())

        while state > 100:
            state -= 100
            times_passes_zero += 1
            print(f"-----pass zero")

        if state == 100:
            state -= 100

        while state <= -100:
            state += 100
            times_passes_zero += 1
            print(f"-----pass zero")

        while state < 0:
            state += 100
            if start_state != 0:
                times_passes_zero += 1
                print(f"-----pass zero")

        print(f"{instruction} --> {state}")

        if state == 0:
            times_pointing_zero+=1

    print("=========================")
    print(f"{times_pointing_zero} + {times_passes_zero} = {times_pointing_zero + times_passes_zero}")



if __name__ == '__main__':
    main()
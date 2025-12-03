FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def largest_digit(bank: list, start_index, stop_index):
    max_digit = 0
    max_digit_index = 0

    for battery1_index in range(start_index, len(bank) - stop_index):
        val = int(bank[battery1_index])
        if val > max_digit:
            max_digit = val
            max_digit_index = battery1_index

    if max_digit == 0:
        raise Exception("no max digit found")

    return max_digit, max_digit_index



def largest_joltage(bank: list, digits_number: int = 12):
    number = ""
    start_index = 0
    stop_index = digits_number - 1

    for i in range(digits_number):
        max_digit, max_digit_index = largest_digit(bank, start_index, stop_index)
        number += str(max_digit)
        start_index = max_digit_index + 1
        stop_index -= 1

    return number



def main():
    banks = read_file()

    sum_of_batteries = 0

    for bank in banks:
        print(bank)
        bank = list(bank.strip())
        largest = largest_joltage(bank)
        sum_of_batteries += int(largest)

    print(f"sum of batteries: {sum_of_batteries }") # part 1 = 17330

if __name__ == '__main__':
    main()


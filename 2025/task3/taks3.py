FILE_PATH = "input.txt"

def read_file():
    with open(FILE_PATH) as f:
        return f.readlines()

def largest_joltage(bank: list):
    biggest = 0
    for battery1_index in range(len(bank)):
        for battery2_index in range(battery1_index+1, len(bank)):
            print(f"{bank[battery1_index]} + {bank[battery2_index]}")
            value = int(bank[battery1_index] + bank[battery2_index])
            if value > biggest:
                biggest = value

    return biggest



def main():
    banks = read_file()

    sum_of_batteries = 0

    for bank in banks:
        bank = list(bank.strip())
        largest = largest_joltage(bank)
        sum_of_batteries += largest

    print(f"sum of batteries: {sum_of_batteries }")

if __name__ == '__main__':
    main()


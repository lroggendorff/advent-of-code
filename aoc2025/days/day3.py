import pathlib


def answer(data):
    banks = [b.strip() for b in data.split("\n")]
    high_joltage = []
    for bank in banks:
        first_digit = 0
        second_digit = 0
        found_first = 0

        for i, d in enumerate(bank[:-1]):
            if int(d) > first_digit:
                found_first = i
                first_digit = int(d)
        for d in bank[found_first + 1:]:
            if int(d) > second_digit:
                second_digit = int(d)
        high_joltage.append(int(f"{first_digit}{second_digit}"))

    return sum(high_joltage)

def answer_part_two(data):
    banks = [b.strip() for b in data.split("\n")]
    high_joltage = 0
    for bank in banks:
        integers = [int(b) for b in bank]
        # count down from the necessary amount of batteries (12)
        for i in range(11, -1, -1):
            battery_location = 0
            if i == 0:  # we only need on more battery
                largest_battery = max(integers)
            else:
                # the max of integers remaining in the bank
                largest_battery = max(integers[:-i])
            # find where that battery value is
            battery_location = integers.index(largest_battery)
            # and update the bank to drop any intervening values
            integers = integers[battery_location + 1:]
            # multiply by 10 to the power of the current location to pad with zeros
            # and add to the total
            high_joltage += largest_battery * (10 ** i)

    return high_joltage


if __name__ == "__main__":
    data = open(pathlib.Path(__file__).parent.parent / "inputs/day3.txt").read()
    print(answer(data.strip()))
    print(answer_part_two(data.strip()))

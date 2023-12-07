NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def match(string: str) -> int | None:
    for number in NUMBERS.keys():
        if number in string[: len(number)]:
            return NUMBERS[number]
    return None


def get_num(line: str) -> int:
    nums: list[int] = []
    for index, char in enumerate(line):
        if char.isdigit():
            nums.append(int(char))
            continue
        found = match(line[index:])
        if found is None:
            continue
        nums.append(int(found))

    first = nums[0]
    last = nums[-1]
    return first * 10 + last


def main() -> None:
    output = 0
    with open("inputs/day1.txt", "r", encoding="utf-8") as file:
        for line in file.read().split("\n"):
            if not line:
                continue
            num = get_num(line)
            output += num
    print(output)


if __name__ == "__main__":
    main()

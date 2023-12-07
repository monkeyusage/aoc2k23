from dataclasses import dataclass


@dataclass
class Symbol:
    xcoord: int
    ycoord: int


@dataclass
class Number:
    xcoords: tuple[int, ...]
    ycoord: int
    value: int


def main() -> None:
    with open("inputs/day3.txt", "r") as file:
        content = file.read()

    # first read the symbols
    numbers: list[Number] = []
    symbols: list[Symbol] = []
    max_x = content.find("\n")
    max_y = (len(content) // max_x) - 1
    breakpoint()
    for ycoord, line in enumerate(content.splitlines()):
        for xcoord, char in enumerate(line):
            if char in "*#+$":
                symbols.append(Symbol(xcoord, ycoord))
                continue
            if not char.isdigit():
                continue


if __name__ == "__main__":
    main()

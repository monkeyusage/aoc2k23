import re
from functools import reduce


def game_possible(line: str) -> bool:
    max_cubes_for_color = {'red': 12, 'green': 13, 'blue': 14}
    game_stats = line.split(':')[-1]
    sub_games: list[str] = game_stats.split(';')
    for sub_game in sub_games:
        colors: list[str] = sub_game.split(',')
        for color in colors:
            ncubes, cube_color = color.strip().split()
            max_ncubes = max_cubes_for_color[cube_color]
            if int(ncubes) > max_ncubes:
                return False
    return True


def game_power(line: str) -> int:
    rgb_min = {'red': 0, 'green': 0, 'blue': 0}
    game_stats = line.split(':')[-1]
    sub_games: list[str] = game_stats.split(';')
    for sub_game in sub_games:
        cubes: list[str] = sub_game.split(',')
        for cube in cubes:
            ncubes, cube_color = cube.strip().split()
            if int(ncubes) > rgb_min[cube_color]:
                rgb_min[cube_color] = int(ncubes)
   
    return reduce(lambda a, b: a * b, rgb_min.values())


def main() -> None:
    total = 0
    gameid_pattern = re.compile(r'\d+')
    with open('inputs/day2.txt', 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()

    for line in lines:
        match = gameid_pattern.search(line)
        assert match is not None
        # game_id = int(match.group())
        power = game_power(line)
        total += power
    
    print(total)

if __name__ == '__main__':
    main()

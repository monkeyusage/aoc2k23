@register_passable
struct RGB:
    var red: Int
    var green: Int
    var blue: Int

    fn __init__() -> Self:
        return Self{red: 1, green: 1, blue: 1}

    fn multiply(inout self) -> Int:
        return self.red * self.green * self.blue


fn strip_left(borrowed string: String) -> String:
    var out = String('')
    for index in range(len(string)):
        let char = string[index]
        if (out == '') and (char == ' '):
            continue
        out += char
    return out

fn game_power(owned line: String) raises -> Int:
    if len(line) == 0:
        return 0
    var rgb_min = RGB()
    let game_stats = line.split(":")[1]
    let sub_games: DynamicVector[String] = game_stats.split(";")
    for index in range(sub_games.size):
        let sub_game: String = sub_games[index]
        let cubes: DynamicVector[String] = sub_game.split(",")
        for sub_index in range(cubes.size):
            let cube: String = cubes[sub_index]
            let cube_info = strip_left(cube).split(' ')
            let ncubes = atol(str(cube_info[0]))
            let cube_color = cube_info[1]
            if cube_color == "blue" and ncubes > rgb_min.blue:
                rgb_min.blue = ncubes
                continue
            if cube_color == "red" and ncubes > rgb_min.red:
                rgb_min.red = ncubes
                continue
            if cube_color == "green" and ncubes > rgb_min.green:
                rgb_min.green = ncubes

    return rgb_min.multiply()


fn main() raises:
    var total : Int = 0
    var lines = DynamicVector[String]()
    with open("inputs/day2.txt", "r") as file:
        let content = file.read()
        lines = content.split("\n")

    for index in range(lines.size):
        let line = lines[index]
        let power = game_power(line^)
        total += power

    print(total)

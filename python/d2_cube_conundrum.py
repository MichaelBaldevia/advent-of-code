game_dict = {}

def  get_game_id_sum(game_record):
    game_winning_cubes = {'red':12, 'green': 13, 'blue': 14}
    sum_of_ids = 0
    sum_of_powers = 0
    for game_id in game_record:
        if game_record[game_id]['red'] <=  game_winning_cubes["red"] and game_record[game_id]['green'] <= game_winning_cubes["green"] and game_record[game_id]['blue'] <= game_winning_cubes["blue"]:
            sum_of_ids += int(game_id)
        sum_of_powers += ((game_record[game_id]['red'] * game_record[game_id]['green']) * game_record[game_id]['blue'])
    return sum_of_ids, sum_of_powers

def curate_games(line):
    game_desc = line.replace(" ", "")
    game_desc = game_desc.replace("\n", "")
    game_desc = game_desc.replace("Game","")
    game_desc = game_desc.split(":")
    return game_desc

with open('./puzzle_inputs/d2_input.txt', 'r') as file:
    for game in file:
        cubes = {}
        game_desc = curate_games(game)
        cube_set = game_desc[1].split(";")
        for cube in cube_set:
            cube_record = cube.split(",")
            for color in cube_record:
                number = ""
                word = ""
                for char in color:
                    if char.isdigit():
                        number += char
                    else:
                        word += char
                number = int(number)
                if word not in cubes:
                    cubes[word] = number
                else:
                    if cubes[word] < number:
                        cubes[word] = number
        game_dict[game_desc[0]] = cubes
    sum_of_ids,sum_of_powers = get_game_id_sum(game_dict)
    print(sum_of_ids)
    print(sum_of_powers)
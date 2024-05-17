digits = []

with open('./puzzle_inputs/d1_input.txt', 'r') as file:
    for line in file:
        first_num = 0
        second_num = 0
        for character in line:
            if character.isdigit() and first_num == 0:
                first_num = character
            if character.isdigit():
                second_num = character
        digits.append(str(first_num) + str(second_num))

sum = sum(int(number) for number in digits)
print(sum)
import util


def main():
    calories = []
    calories_tmp = 0
    
    with open(util.input_file) as f:
        while (line := f.readline()):
            line = line.rstrip()
            if line:
                calories_tmp += int(line)
            else:
                calories.append(calories_tmp)
                calories_tmp = 0

    calories.sort(reverse=True)
    top_3_calories = sum(calories[0:3])

    print(f'The elf with most calories is carrying {calories[0]} calories.')
    print(f'The 3 elves with most calories are carrying {top_3_calories} calories in total.')


if __name__ == '__main__':
    main()

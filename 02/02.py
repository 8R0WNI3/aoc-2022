import util


def get_indicated_shape(char_1: str, char_2: str) -> str:
    if is_loose := char_2 == 'X':
        if is_rock := char_1 == 'A':
            return 'Z'
        elif is_paper := char_1 == 'B':
            return 'X'
        elif is_scissors := char_1 == 'C':
            return 'Y'
    if is_draw := char_2 == 'Y':
        if is_rock := char_1 == 'A':
            return 'X'
        elif is_paper := char_1 == 'B':
            return 'Y'
        elif is_scissors := char_1 == 'C':
            return 'Z'
    if is_win := char_2 == 'Z':
        if is_rock := char_1 == 'A':
            return 'Y'
        elif is_paper := char_1 == 'B':
            return 'Z'
        elif is_scissors := char_1 == 'C':
            return 'X'


def get_points_for_outcome(char_1: str, char_2: str) -> int:
    if is_rock := char_1 == 'A':
        if is_rock := char_2 == 'X':
            return 3
        elif is_paper := char_2 == 'Y':
            return 6
        elif is_scissors := char_2 == 'Z':
            return 0
    elif is_paper := char_1 == 'B':
        if is_rock := char_2 == 'X':
            return 0
        elif is_paper := char_2 == 'Y':
            return 3
        elif is_scissors := char_2 == 'Z':
            return 6
    elif is_scissors := char_1 == 'C':
        if is_rock := char_2 == 'X':
            return 6
        elif is_paper := char_2 == 'Y':
            return 0
        elif is_scissors := char_2 == 'Z':
            return 3



def get_points_for_shape(char: str) -> int:
    if is_rock := char == 'A' or char == 'X':
        return 1
    if is_paper := char == 'B' or char == 'Y':
        return 2
    if is_scissors := char == 'C' or char == 'Z':
        return 3


def main():
    top_secret_strategy_guide_points = ultra_top_secret_strategy_guide_points = 0
    
    with open(util.input_file) as f:
        while (line := f.readline().rstrip()):
            char_1, char_2 = line.split(' ')

            top_secret_strategy_guide_points += get_points_for_shape(char_2)
            top_secret_strategy_guide_points += get_points_for_outcome(char_1, char_2)

            indicated_shape = get_indicated_shape(char_1, char_2)
            ultra_top_secret_strategy_guide_points += get_points_for_shape(indicated_shape)
            ultra_top_secret_strategy_guide_points += get_points_for_outcome(char_1, indicated_shape)

    print(f'The total score for the top secret strategy guide would be {top_secret_strategy_guide_points}.')
    print(f'The total score for the ultra top secret strategy guide would be {ultra_top_secret_strategy_guide_points}.')


if __name__ == '__main__':
    main()

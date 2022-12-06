import util


def get_badge_char(items: list[str]) -> str:
    for char in items[0]:
        if char in items[1] and char in items[2]:
            return char


def get_char_priority(char: str) -> int:
    if char.isupper():
        return ord(char) - 38
    return ord(char) - 96


def get_erroneous_char(items: str) -> str:
    first, second = items[:len(items)//2], items[len(items)//2:]

    for char in first:
        if char in second:
            return char


def main():
    sum_erroneous = sum_badges = 0
    group_items = []
    
    with open(util.input_file) as f:
        while (line := f.readline().rstrip()):
            erroneous_char = get_erroneous_char(line)
            sum_erroneous += get_char_priority(erroneous_char)

            group_items.append(line)
            if len(group_items) == 3:
                badge_char = get_badge_char(group_items)
                sum_badges += get_char_priority(badge_char)
                group_items = []

    print(f'The sum of the erroneous priorities of the item types is {sum_erroneous}.')
    print(f'The sum of the badge priorities of the item types is {sum_badges}.')


if __name__ == '__main__':
    main()

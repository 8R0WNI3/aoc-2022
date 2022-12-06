import util


def a_overlaps_b(a: list[int], b: list[int]) -> bool:
    return (a[0] <= b[0] and b[0] <= a[1]) or (b[0] <= a[0] and a[0] <= b[1])


def a_contains_b(a: list[int], b: list[int]) -> bool:
    return a[0] <= b[0] and a[1] >= b[1]


def main():
    sum_contains = sum_overlaps = 0
    
    with open(util.input_file) as f:
        while (line := f.readline().rstrip()):
            first, second = line.split(',')
            first = first.split('-')
            first = [int(first[0]), int(first[1])]
            second = second.split('-')
            second = [int(second[0]), int(second[1])]
            if a_contains_b(first, second) or a_contains_b(second, first):
                sum_contains += 1
            if a_overlaps_b(first, second):
                sum_overlaps += 1


    print(f'In {sum_contains} assigned pairs one range fully contains the other.')
    print(f'In {sum_overlaps} assigned pairs one range overlaps the other.')


if __name__ == '__main__':
    main()

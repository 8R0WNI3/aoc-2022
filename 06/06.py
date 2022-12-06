import util


def check_if_marker(marker: str, length: int) -> bool:
    for idx_1 in range(length-1):
        for idx_2 in range(0, length):
            if (idx_1 != idx_2 and marker[idx_1] == marker[idx_2]):
                return False
    return True


def get_marker_if_exists(line: str, length: int) -> tuple[str, int]:
    for idx in range(length-1, len(line)):
        marker = line[idx-(length-1):idx+1]
        if check_if_marker(marker, length):
            return (marker, idx+1)


def main():
    package_marker = message_marker = None
    package_idx = message_idx = 0
    with open(util.input_file) as f:
        while (line := f.readline().rstrip()):
            package_marker, package_idx = get_marker_if_exists(line, 4)
            message_marker, message_idx = get_marker_if_exists(line, 14)

    print(f'{package_idx} characters need to be processed before the first package marker {package_marker}.')
    print(f'{message_idx} characters need to be processed before the first message marker {message_marker}.')


if __name__ == '__main__':
    main()

import util


class Tree():
    def __init__(self, name: str, size: int, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        self.files = []


def get_size(dir: Tree) -> int:
    size = 0
    for child in dir.children:
        size += get_size(child)

    return dir.size + size


def get_closest_dir_to_size(root: Tree, size: int) -> Tree | None:
    dir = None
    for child in root.children:
        new_dir = get_closest_dir_to_size(child, size)
        if new_dir and (not dir or new_dir.size < dir.size):
            dir = new_dir

    if not dir and get_size(root) >= size:
        dir = root
    return dir


def traverse_and_get_sum(dir: Tree) -> int:
    sum = 0
    for child in dir.children:
        sum += traverse_and_get_sum(child)

    if (size := get_size(dir)) <= 100000:
        sum += size

    return sum


def main():
    root = None
    parent = None
    with open(util.input_file) as f:
        while (line := f.readline().strip()):
            if line == '$ ls':
                pass
            elif line == '$ cd ..':
                parent = parent.parent
            elif line.startswith('$ cd'):
                cur_dir_name = line.split('cd ')[1]
                cur_dir = Tree(cur_dir_name, 0, parent)
                if parent:
                    parent.children.append(cur_dir)
                parent = cur_dir
                if cur_dir_name == '/':
                    root = cur_dir
            elif line.startswith('dir'):
                pass
            else:
                size, file = line.split(' ')
                if file not in parent.files:
                    parent.size += int(size)
                    parent.files.append(file)

    print(f'The sum of the total sizes of the directories with at most a size of 100000 is {traverse_and_get_sum(root)}.')

    missing_disc_space = get_size(root) - 40000000
    print('Total disc space: 70.000.000')
    print('Required disc space: 30.000.000')
    print(f'Filled disc space: {get_size(root)}')
    print(f'Missing disc space: {missing_disc_space}')
    print(f'Total size of closest directory is {get_size(get_closest_dir_to_size(root, missing_disc_space))}.')


if __name__ == '__main__':
    main()

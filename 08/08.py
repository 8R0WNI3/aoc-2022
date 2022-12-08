import util


def main():
    grid = []
    with open(util.input_file) as f:
        while (line := f.readline().strip()):
            cur_row = []
            for char in line:
                cur_row.append(int(char))
            grid.append(cur_row)

    sum = 0
    scenic_score = 0
    for idx_1 in range(len(grid)):
        for idx_2 in range(len(grid[idx_1])):
            # Check if tree is on the edge
            if idx_1 == 0 or idx_2 == 0 or idx_1 == len(grid) - 1 or idx_2 == len(grid[idx_1]) - 1:
                sum += 1
            else:
                is_visible = False
                # Check if tree is visible from the left
                for idx_tmp in range(idx_2):
                    if not grid[idx_1][idx_tmp] < grid[idx_1][idx_2]:
                        break
                    elif idx_tmp == idx_2 - 1:
                        is_visible = True
                        break
                # Check if tree is visible from the right
                if not is_visible:
                    for idx_tmp in range(len(grid[idx_1]) - 1, idx_2, -1):
                        if not grid[idx_1][idx_tmp] < grid[idx_1][idx_2]:
                            break
                        elif idx_tmp == idx_2 + 1:
                            is_visible = True
                            break
                # Check if tree is visible from the top
                if not is_visible:
                    for idx_tmp in range(idx_1):
                        if not grid[idx_tmp][idx_2] < grid[idx_1][idx_2]:
                            break
                        elif idx_tmp == idx_1 - 1:
                            is_visible = True
                            break
                # Check if tree is visible from the bottom
                if not is_visible:
                    for idx_tmp in range(len(grid) - 1, idx_1, -1):
                        if not grid[idx_tmp][idx_2] < grid[idx_1][idx_2]:
                            break
                        elif idx_tmp == idx_1 + 1:
                            is_visible = True
                            break
                if is_visible:
                    sum += 1

            # Calculate scenic score
            distance_left = distance_right = distance_top = distance_bottom = 0
            idx_tmp = idx_2 - 1
            while idx_tmp >= 0:
                distance_left += 1
                if grid[idx_1][idx_tmp] >= grid[idx_1][idx_2]:
                    break
                idx_tmp -= 1
            idx_tmp = idx_2 + 1
            while idx_tmp < len(grid[idx_1]):
                distance_right += 1
                if grid[idx_1][idx_tmp] >= grid[idx_1][idx_2]:
                    break
                idx_tmp += 1
            idx_tmp = idx_1 - 1
            while idx_tmp >= 0:
                distance_top += 1
                if grid[idx_tmp][idx_2] >= grid[idx_1][idx_2]:
                    break
                idx_tmp -= 1
            idx_tmp = idx_1 + 1
            while idx_tmp < len(grid):
                distance_bottom += 1
                if grid[idx_tmp][idx_2] >= grid[idx_1][idx_2]:
                    break
                idx_tmp += 1
            new_scenic_score = distance_left * distance_right * distance_top * distance_bottom
            scenic_score = max(new_scenic_score, scenic_score)

    print(f'{sum} trees are visible from outside the grid.')
    print(f'The highest scenic score possible for any tree is {scenic_score}.')


if __name__ == '__main__':
    main()

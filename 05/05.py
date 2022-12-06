import util


def rearrange_multiple(line: str, stacks: list[list[str]]) -> list[list[str]]:
    procedure_step = line.split(' ')
    crate_count = int(procedure_step[1])
    from_stack = int(procedure_step[3])
    to_stack = int(procedure_step[5])
    crates = stacks[from_stack-1][0:crate_count]
    stacks[from_stack-1] = stacks[from_stack-1][crate_count:]
    stacks[to_stack-1] = crates + stacks[to_stack-1]
    return stacks


def rearrange_single(line: str, stacks: list[list[str]]) -> list[list[str]]:
    procedure_step = line.split(' ')
    crate_count = int(procedure_step[1])
    from_stack = int(procedure_step[3])
    to_stack = int(procedure_step[5])
    for _ in range(crate_count):
        crate = stacks[from_stack-1].pop(0)
        stacks[to_stack-1].insert(0, crate)
    return stacks


def main():
    single_stacks = [[] for _ in range(9)]
    multiple_stacks = [[] for _ in range(9)]
    
    with open(util.input_file) as f:
        while (line := f.readline()):
            line = line.strip()
            # Build stacks with top elem on first index
            if line.startswith('['):
                for idx in range(9):
                    if crate := line[idx*4+1:idx*4+2].strip():
                        single_stacks[idx].append(crate)
                        multiple_stacks[idx].append(crate)
            elif line.startswith('move'):
                single_stacks = rearrange_single(line, single_stacks)
                multiple_stacks = rearrange_multiple(line, multiple_stacks)

    print(f'After the single rearrangement procedure, the following crates end up on the top of each stack: {"".join([stack[0] or "" for stack in single_stacks if len(stack) > 0])}')
    print(f'After the multiple rearrangement procedure, the following crates end up on the top of each stack: {"".join([stack[0] or "" for stack in multiple_stacks if len(stack) > 0])}')


if __name__ == '__main__':
    main()

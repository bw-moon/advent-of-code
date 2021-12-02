def get_deeper_count(lines):
    deeper_count = 0
    previous_depth = None
    for line in lines:
        depth = int(line)
        if previous_depth is not None and depth > previous_depth:
            deeper_count += 1
        previous_depth = depth

    return deeper_count


def get_slided_lines(lines, window_size, aggregator):
    window = []
    result = []
    for line in lines:
        depth = int(line)

        if len(window) >= window_size:
            window.pop(0)
        window.append(depth)

        if len(window) < window_size:
            continue

        result.append(aggregator(window))
    return result


if __name__ == '__main__':
    with open('day1-input.txt') as f:
        data = f.readlines()
        print('Part1')
        print(get_deeper_count(data))
        print('Part2')
        print(get_deeper_count(get_slided_lines(data, 3, sum)))

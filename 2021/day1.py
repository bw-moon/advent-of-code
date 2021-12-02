def get_deeper_count():
    deeper_count = 0
    previous_depth = None
    with open('day1-input.txt') as f:
        while True:
            line = f.readline()
            if not line:
                break
            depth = int(line)
            if previous_depth is not None and depth > previous_depth:
                deeper_count += 1
                print(f"{depth} '(increased)'")
            else:
                print(f"{depth} '(decreased or same)'")
            previous_depth = depth

    return deeper_count


if __name__ == '__main__':
    print(get_deeper_count())

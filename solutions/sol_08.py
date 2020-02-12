import fileinput


def solution() -> None:
    lines = 0
    for _ in fileinput.input():
        lines += 1
    print(f"Number of lines in this input is: {lines}")


def main():
    solution()


if __name__ == '__main__':
    main()
import sys


def solution() -> None:
    try:
        with open("/etc/passwd", "r") as file:
            lines = file.readlines()
        bash_lines = [(line_number, line.strip()) for line_number, line
                      in enumerate(lines, 1) if "/bin/bash" in line]
    except (IOError, FileNotFoundError) as exception:
        sys.exit(f"ERROR: {exception}")
    else:
        for bash_line in bash_lines:
            print(bash_line)


def main():
    solution()


if __name__ == '__main__':
    main()
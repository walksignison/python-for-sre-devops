import sys


def solution() -> None:
    print(f"Python version installed: {sys.version}")
    print(f"OS version installed: {sys.platform}")
    print(f"Number of modules in search path: {len(sys.path)}")
    print(f"Number of modules loaded: {len(sys.modules)}")
    print("Arguments: ")
    for arg in sys.argv:
        print(arg)


def main():
    solution()


if __name__ == '__main__':
    main()
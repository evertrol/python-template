import argparse

from . import func1


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", help="Input value for the calculation")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    y = func1(x)
    print(y)


if __name__ == "__main__":
    main()

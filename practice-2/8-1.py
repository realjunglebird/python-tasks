import os
import argparse

def print_content():
    for file in os.listdir():
        print(file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-r')

    args = parser.parse_args()

    if args.R:
        pass
        print("r passed")
    else:
        print_content()

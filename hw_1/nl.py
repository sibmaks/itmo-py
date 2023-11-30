#! /usr/bin/env python

import sys


def nl(file_path=None):
    if file_path:
        with open(file_path, 'r') as file:
            line = file.readline()
            i = 1
            while line:
                print(f"{i}\t{line.strip()}")
                line = file.readline()
                i += 1
    else:
        line = sys.stdin.readline()
        i = 1
        while line:
            print(f"{i}\t{line.strip()}")
            line = sys.stdin.readline()
            i += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        nl(sys.argv[1])
    else:
        nl()

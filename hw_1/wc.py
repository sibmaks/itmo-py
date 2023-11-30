#! /usr/bin/env python

import sys


def wc(files=None):
    if not files:
        data = sys.stdin.read()
        lines = data.splitlines()
        words = data.split()
        total_lines = len(lines)
        total_words = len(words)
        total_bytes = len(data.encode())
        print(f"{total_lines}\t{total_words}\t{total_bytes}")
    else:
        total_lines = 0
        total_words = 0
        total_bytes = 0
        for file in files:
            with open(file, 'r') as f:
                data = f.read()
                lines = data.splitlines()
                words = data.split()
                file_lines = len(lines)
                file_words = len(words)
                file_bytes = len(data.encode())
                total_lines += file_lines
                total_words += file_words
                total_bytes += file_bytes
                print(f"{file_lines}\t{file_words}\t{file_bytes}\t{file}")

        if len(files) > 1:
            print(f"{total_lines}\t{total_words}\t{total_bytes}\ttotal")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        wc()

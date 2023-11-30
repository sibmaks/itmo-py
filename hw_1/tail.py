import sys


def tail(files=None):
    if not files:
        lines = sys.stdin.readlines()
        start_index = max(0, len(lines) - 17)
        for line in lines[start_index:]:
            print(line, end='')
    else:
        count = len(files)
        for file in files:
            if count > 1:
                print(f"==> {file} <==")
            with open(file, 'r') as f:
                lines = f.readlines()
                start_index = max(0, len(lines) - 10)
                for line in lines[start_index:]:
                    print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail(sys.argv[1:])
    else:
        tail()

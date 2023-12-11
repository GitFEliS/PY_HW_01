import sys


def tail(filenames: str):
    not_first = False
    for filename in filenames:
        try:
            f = open(filename, 'r')
        except:
            print(f"tail: cannot open '{filename}' for readin: No such file or directory")  # nopep8
            return
        if not_first:
            print()
        not_first = True
        if (len(filenames) > 1):
            print(F"==> {filename} <==")
        lines = f.readlines()[-10:]
        f.close()
        for line in lines:
            print(line, end='')


def tail_stdin():
    lines = sys.stdin.readlines()[-17:]
    for line in lines:
        print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        tail(sys.argv[1:])
    else:
        tail_stdin()

import sys


def nl(filename: str):
    try:
        f = open(filename, 'r')
    except:
        print(f"nl: {filename}: No such file or directory")
        return
    counter = 1
    body = True
    for line in f:
        if line == "\\:\\:\\:\n" or line == "\\:\n":
            body = False
            print()
            continue
        elif line == "\\:\\:\n":
            body = True
            print()
            counter = 1
            continue
        if body:
            print(f"{counter:6d}\t{line}", end='')
        else:
            print(f"       {line}", end='')
        counter += 1
    f.close()


def nl_stdin():
    counter = 1
    body = True
    for line in sys.stdin:
        if line == "\\:\\:\\:\n" or line == "\\:\n":
            body = False
            print()
            continue
        elif line == "\\:\\:\n":
            body = True
            print()
            continue
        if body:
            print(f"{counter:6d}\t{line}", end='')
        else:
            print(f"       {line}", end='')
        counter += 1


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for file in sys.argv[1:]:
            nl(file)
    else:
        nl_stdin()

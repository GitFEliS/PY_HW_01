import sys
import math


def wc(filenames: str):
    total_lines = 0
    total_bytes = 0
    total_words = 0
    answers = []  # для правильного форматирования надо знать весь ответ
    for filename in filenames:
        try:
            f = open(filename, 'r')
            lines = f.read().split('\n')
            words = [x for y in lines for x in y.split()]
            f.close()
        except:
            answers.append((filename, ))
            continue
            # print(f"wc: {filename}: No such file or directory")
        bytes = 0
        for line in lines:
            bytes += len(line.encode())
        if bytes > 0:
            digits = int(math.log10(bytes))+1  # для такого же форматирования
        else:
            digits = 1

        # print(lines)
        ends_with_nl = lines[-1] == ''
        bytes += len(lines) - ends_with_nl
        answers.append((len(lines) - ends_with_nl, len(words), bytes, filename))  # nopep8
        # print(f'{len(lines):{digits}} {len(words):{digits}} {bytes} {filename}')  # nopep8

        total_lines += len(lines) - ends_with_nl
        total_bytes += bytes
        total_words += len(words)

    if total_bytes > 0:
        digits = int(math.log10(total_bytes))+1  # для такого же форматирования
    else:
        digits = 1

    for ans in answers:
        if len(ans) < 4:
            print(f"wc: {ans[0]}: No such file or directory")
        else:
            print(f'{ans[0]:{digits}} {ans[1]:{digits}} {ans[2]:{digits}} {ans[3]}')  # nopep8

    if (len(filenames) > 1):
        print(f'{total_lines:{digits}} {total_words:{digits}} {total_bytes} total')  # nopep8


def tail_stdin():
    lines = sys.stdin.readlines()[-10:]
    for line in lines:
        print(line, end='')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        wc(sys.argv[1:])
    else:
        tail_stdin()

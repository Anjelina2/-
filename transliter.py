def letters(symbol):
    d = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'g', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    return symbol in d


def numbers(symbol):
    d = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    return symbol in d


def sign(symbol):
    d = ('+', '-')
    return symbol in d


def main(line):
    line = line.lower()
    spisok = []

    for i in range(len(line)):
        if letters(line[i]):
            spisok.append([line[i], 'letter'])
        elif numbers(line[i]):
            spisok.append([line[i], 'digit'])
        elif line[i] == ' ':
            spisok.append([line[i], 'space'])
        elif sign(line[i]):
            spisok.append([line[i], 'sign'])
        elif line[i] == '[':
            spisok.append([line[i], 'square_bracket_start'])
        elif line[i] == ']':
            spisok.append([line[i], 'square_bracket_end'])
        elif line[i] == ';':
            spisok.append([line[i], 'semicolon'])
        elif line[i] == ':':
            spisok.append([line[i], 'colon'])
        elif line[i] == '.':
            spisok.append([line[i], 'dot'])
        elif line[i] == ',':
            spisok.append([line[i], 'comma'])
        else:
            return 'error'

    return spisok


'''
line='if a(3 +  d5) then repeat b(True) until e51(False);'
print(main(if))'''
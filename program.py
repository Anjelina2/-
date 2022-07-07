import transliter
import lexical
import syntax

f = open('input.txt', 'r')
line = f.readline()
f.close()

f = open('output.txt', 'w')

line = transliter.main(line)
if line == 'ошибка':
    f.write('REJECT')
else:
    line = lexical.main(line)
    if line == 'ошибка':
        f.write('REJECT')
    else:
        line = syntax.main(line)
        if line:
            f.write('ACCEPT')
        else:
            f.write('REJECT')

f.close()
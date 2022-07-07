def key_words(word):
    d = ('and', 'end', 'nil', 'set', 'array', 'file', 'not', 'then', 'begin', 'for', 'of', 'to', 'case', 'function',
         'or', 'type', 'const', 'goto', 'packed', 'until', 'div', 'if', 'procedure', 'var', 'do', 'in', 'program',
         'while', 'downto', 'label', 'record', 'with', 'else', 'mod', 'repeat')
    return word in d


def math_sign(word):
    d = ('div', 'mod')
    return word in d


def bool_const(word):
    d = ('true', 'false')
    return word in d


def main(ident):
    if math_sign(ident):
        type = 'мат_знак'
    elif key_words(ident):
        type = 'клслово_' + ident
    elif bool_const(ident):
        type = 'лог_конст'
    else:
        type = 'идентификатор'
    return type

'''
line='if'
print(main(if))'''
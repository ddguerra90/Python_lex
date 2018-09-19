#https://www.dabeaz.com/ply/PLYTalk.pdf
import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS', 'JUMPLINE' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_JUMPLINE = r'\n'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

entrada = open("expresiones.in","r")
exp = entrada.readlines()

for i in range(0, len(exp)):    
    pp = exp[i]
    str1 = str(pp)
    print ("------####-------")
    print (str1)
    print ("P")
    lex.input(str1)
    while True:
        tok = lex.token()
        if not tok: break
        print (str(tok.value) + " - " + str(tok.type))

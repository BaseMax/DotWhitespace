# Max Base
# DotWhitespace Interpreter
# https://github.com/BaseMax/DotWhitespace
# Date: 2020-07-17, 2020-07-23
import sys
import string

debug=False
chars=' '+string.ascii_lowercase+string.ascii_uppercase+'0123456789!@#$%^&*()_-=+?<>[]{}'
ops='+-*/^%'
variable={}
'''
T      +
TT     -
TTT    *
TTTT   /
TTTTT  **
TTTTTT %
.
'''
'''
.S.SS.SSS T .SS.S        ; ABC = 'BA'
.S.SS.SSS T T SS . S     ; ABC = 10

..S T .S.SS.SSS         ; PRINT ABC
..S   .SS.S             ; PRINT 'BA'
..ST  SS.S              ; PRINT 10
..ST  SS.S              ; PRINT 10
..ST  SS.S T SSS.S      ; PRINT 10 + 20
...
'''

def calculate_number(values):
    result=0
    i=0
    # for value in values:
    while i<len(values):
        if values[i][1]==None:
            break
        else:
            values[i][0]=float(values[i][0])
            values[i+1][0]=float(values[i+1][0])
            if result==0:
                result=values[i][0]
            if values[i][1]=='+':
                result=result + values[i+1][0]
            elif values[i][1]=='-':
                result=result - values[i+1][0]
            elif values[i][1]=='*':
                result=result * values[i+1][0]
            elif values[i][1]=='/':
                result=result / values[i+1][0]
            elif values[i][1]=='^':
                result=result ** values[i+1][0]
            elif values[i][1]=='%':
                result=result % values[i+1][0]
        i+=1
    if i==0 and values[0][1]==None:
        result=float(values[0][0])
    if result==int(result):
        return int(result)
    return result

def parse_number(command):
    global debug
    ## print('parsing number...')
    length=len(command)
    j=0
    value=''
    values=[]
    # for i in range(length):
    i=0
    while i<length:
        if command[i]=='.':
            value+=str(j-1)
            j=0
        elif command[i]=='\t' or command[i]=='T':
            op=0
            if command[i-1]!='.':
                value+=str(j-1)
            for j in range(i+1, length):
                if command[j]=='\t' or command[j]=='T':
                    op+=1
                    i+=1
                else:
                    break
            values.append([value, ops[op]])
            value=''
            j=0
        else:
            j+=1
        i+=1
    if j!=0:
        value+=str(j-1)
        j=0
    if value!='':
        values.append([value, None])
    if debug:
        print(values)
    return values

def parse_string(command):
    length=len(command)
    j=0
    value=''
    for i in range(length):
        if command[i]=='.':
            value+=chars[j]
            j=0
        elif command[i]=='\t' or command[j]=='T':
            return (value, i)
        else:
            j+=1
    return (value, i)

def parse_value(command):
    # print(command)
    if command[0]=='\t' or command[0]=='T':
        return('VAR', parse_string(command[1:])[0][1:])
    elif command[0]=='.':
        return('STR', parse_string(command[1:])[0])
    else:
        return('NUM', calculate_number(parse_number(command)))

def parse_command(command):
    global debug, variable
    if command.lower() == '# debug' or command.lower() == '#debug':
        debug=True
    elif command.startswith('#'):
        return
    elif command.startswith('... ') or command.startswith('...S'):
        if debug:
            print('READ') # TODO
    elif command.startswith('.. ') or command.startswith('..S'):
        command=command[3:]
        if debug:
            print('PRINT', parse_value(command))
        value=parse_value(command)
        if value[0] == 'VAR':
            try:
                print(variable[value[1]][1])
            except IndexError:
                print('not found')
        else:
            print(value[1])
    elif command.startswith('. ') or command.startswith('.S'):
        ident=parse_string(command[2:])
        value=parse_value(command[ident[1]+3:])
        if debug:
            print('DEFINE', ident[0][1:], value)
        variable[ident[0][1:]]=value

def parse(input):
    commands=input.split('\n')
    commands=list(filter(None, commands))
    for command in commands:
        parse_command(command)

def read(fileName):
    return open(fileName).read()

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == '-debug':
            debug=True
            parse( read( sys.argv[2] ) )
        elif sys.argv[2] == '-debug':
            debug=True
            parse( read( sys.argv[1] ) )
        else:
            print("Error: bad arguments!")
    if len(sys.argv) == 2:
        parse( read( sys.argv[1] ) )

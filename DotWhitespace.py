# Max Base
# DotWhitespace Interpreter
# https://github.com/BaseMax/DotWhitespace
import string
chars=string.ascii_lowercase+string.ascii_uppercase+'0123456789!@#$%^&*()_-=+?<>[]{}'
ops='+-*/^%'
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
input=''
input+='. . .  .   .\t. .  .   .\n'
input+='. . .  .   .\t\t. .  .   .\n'
input+='. . .  .   .\t  .   .    . .\n'
input+='.. \t. .  .   .\n'
input+='.. . .  .   .\n'
input+='..   . .\n'
input+='..   . . .\t   . .\n'
input+='..   . . \t   . \n'

commands=input.split('\n')
commands=list(filter(None, commands))
variable={}
## print(input)
## print(commands)
def calculate_number(values):
    result=0
    i=0
    for value in values:
        if value[1]==None:
            break
        else:
            values[i][0]=float(values[i][0])
            values[i+1][0]=float(values[i+1][0])
            if value[1]=='+':
                result+=values[i][0] + values[i+1][0]
            elif value[1]=='-':
                result+=values[i][0] - values[i+1][0]
            elif value[1]=='*':
                result+=values[i][0] * values[i+1][0]
            elif value[1]=='/':
                result+=values[i][0] / values[i+1][0]
            elif value[1]=='^':
                result+=values[i][0] ** values[i+1][0]
            elif value[1]=='%':
                result+=values[i][0] % values[i+1][0]
            i+=1
    if i==0 and values[0][1]==None:
        result=float(values[0][0])
    if result==int(result):
        return int(result)
    return result

def parse_number(command):
    ## print('parsing number...')
    length=len(command)
    j=0
    value=''
    values=[]
    for i in range(length):
        if command[i]=='.':
            ## print('\tINT', j-1)
            value+=str(j-1)
            j=0
        elif command[i]=='\t':
            op=0
            if command[i-1]!='.':
                value+=str(j-1)
            for j in range(i+1, length):
                if command[j]=='\t':
                    op+=1
                    i+=1
                else:
                    break
                ## print('j is:', j)

            values.append([value, ops[op]])
            value=''
            j=0
        else:
            j+=1
    if j!=0:
        ## print('\tINT', j-1)
        value+=str(j-1)
        j=0
    if value!='':
        values.append([value, None])
    ## print(value)
    ## print(values)
    return values
    # return value

def parse_string(command):
    ## print('parsing string...')
    length=len(command)
    j=0
    value=''
    for i in range(length):
        if command[i]=='.':
            ## print('\tCHAR', j+1, chars[j])
            value+=chars[j]
            j=0
        elif command[i]=='\t':
            return (value, i)
        else:
            j+=1
    ## print(value)
    # return value
    return (value, i)

def parse_value(command):
    if command[0]=='\t':
        return('VAR', parse_string(command[1:])[0])
    elif command[0]=='.':
        return('STR', parse_string(command)[0])
    else:
        return('NUM', calculate_number(parse_number(command)))

def parse_command(command):
    if command.startswith('... '):
        print('READ') # TODO
    elif command.startswith('.. '):
        ## print('print')
        ## print(command[3:])
        command=command[3:]
        # print('PRINT', parse_value(command))
        value=parse_value(command)
        if value[0] == 'VAR':
            try:
                print(variable[value[1]][1])
            except IndexError:
                print('not found')
        else:
            print(value[1])
    elif command.startswith('. '):
        ## print('define')
        ident=parse_string(command[2:])
        ## print(ident)
        ## print(command)
        ## print(command[ident[1]+3:])
        value=parse_value(command[ident[1]+3:])
        # print('DEFINE', ident[0], value)
        variable[ident[0]]=value

for command in commands:
    ## print(command)
    ## print(parse_command(command))
    parse_command(command)


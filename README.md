# Dot-Whitespace Interpreter

## DotWhitespace Programming Language

DotWhitespace is an esoteric programming language developed by Max Base. It was released on 17 July 2020. Its name is a reference to whitespace and dot characters. Unlike most programming languages, which ignore or assign little meaning to most whitespace characters, the DotWhitespace interpreter ignores any non-whitespace characters. Only spaces, tabs, dot, and linefeeds have meaning. A consequence of this property is that a Whitespace program can easily be contained within the whitespace characters of a program written in another language, except possibly in languages which depend on spaces for syntax validity such as Python, making the text a polyglot.

![DotWhitespace Programming Language](logo.png)

### Hello, World in `.Whitespace`

`$ python DotWhitespace.py examples/hello-world.ds`

```
.. .        .     .            .            .               ..                       .               .                  .            .    .
```

Output: `hello world`

### Sample Program

```
. . .  .   .	. .  .   .
. . .  .   .		. .  .   .
. . .  .   .	  .   .    . .
.. 	. .  .   .
.. . .  .   .
..   . .
..   . . .	   . .
..   . . 	   . 
```

It is actually equivalent to:

```
.S.S.SS.SSS.T.S.SS.SSS.     ; DEFINE abc ('STR', 'abc')
.S.S.SS.SSS.TT.S.SS.SSS.    ; DEFINE abc ('VAR', 'abc')
.S.S.SS.SSS.TSS.SSS.SSSS.S. ; DEFINE abc ('NUM', 1230)
..ST.S.SS.SSS.              ; PRINT ('VAR', 'abc')
..S.S.SS.SSS.               ; PRINT ('STR', 'abc')
..SSS.S.                    ; PRINT ('NUM', 10)
..SSS.S.S.TSSS.S.           ; PRINT ('NUM', 120) 
..SSS.S.STSSS.S             ; PRINT ('NUM', 120)
```

Output:

```
1230
abc
10
120
120
```

## DotWhitespace Commands

There are only three types of commands in this language.

`S` means whitespace character.

- Print to console (String or Number directly or from a variable)
```
..S
```

- Read input from console (not yet developed); __I need help from others.__
```
...S
```

- Variable definition
```
.S
```

### Operators

`T` means tab character. (`\t`)

| Syntax  | Operator |
| ------- | -------- |
|   T     | +        |
| TT      |  -       |
| TTT     | *        |
| TTTT    | /        |
| TTTTT   | ^        |
| TTTTTT  |  %       |

Note: There are no parentheses, So the priority of the operators will not support all mathematics expression.

### Debug

You can pass `-debug` argument, then you will see debug information in **stout**.

e.g: `$ python DotWhitespace.py examples/hello-world.ds -debug`
or `$ python DotWhitespace.py -debug examples/hello-world.ds`

Output:

```
('PRINT', ('STR', 'hello world'))
hello world
```

### Examples

- Input: `. . .  .   .\t. .  .   .\n`

DEFINE abcd ('STR', 'abcd')

- Input: `. . .  .   .\t\t. .  .   .\n`

DEFINE abcd ('VAR', 'abcd')

- Input: `. . .  .   .\t  .   .    . .\n`

DEFINE abcd ('NUM', 1230)

- Input: `.. \t. .  .   .\n`

PRINT ('VAR', 'abcd')

- Input: `.. . .  .   .\n`

PRINT ('STR', 'abcd')

- Input: `..   . .\n`

PRINT ('NUM', 10)

- Input: `..   . . .\t   . .\n`

PRINT ('NUM', 120)

- Input: `..   . . \t   . \n`

PRINT ('NUM', 120)

### Characters supported as string:

` abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_-=+?<>[]{}`

Note: You will not be able to print any characters other than the above.

### TODO

- Implement **float number**.
- Display Tree of program.
- Implement Read Input. (`input()` in python or `scanf()` in c)

# ChangeLog

- [x] 2020-07-23: Get filename from argument and reads from file.
- [x] 2020-07-23: Adding `whitespace` (\s) as supported character. (e.g: we want to display `Hello World`, Not `HelloWorld`)

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)


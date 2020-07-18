# DotWhitespace Programming Language

DotWhitespace is an esoteric programming language developed by Max Base. It was released on 17 July 2020. Its name is a reference to whitespace and dot characters. Unlike most programming languages, which ignore or assign little meaning to most whitespace characters, the DotWhitespace interpreter ignores any non-whitespace characters. Only spaces, tabs, dot, and linefeeds have meaning. A consequence of this property is that a Whitespace program can easily be contained within the whitespace characters of a program written in another language, except possibly in languages which depend on spaces for syntax validity such as Python, making the text a polyglot.

![DotWhitespace Programming Language](logo.png)

### Hello, World

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
.S.S.SS.SSS.T.S.SS.SSS.
.S.S.SS.SSS.TT.S.SS.SSS.
.S.S.SS.SSS.TSS.SSS.SSSS.S.
..ST.S.SS.SSS.
..S.S.SS.SSS.
..SSS.S.
..SSS.S.S.TSSS.S.
..SSS.S.STSSS.S
```

Output:

```
1230
abcd
10
120
120
```

### Operators

| Syntax  | Operator |
| ---- | ------------- |
|   T  | + |
| TT  |  - |
| TTT  | *  |
| TTTT  | / |
| TTTTT  | ^ |
| TTTTTT  |  % |

### Examples

- Input: `. . .  .   .\t. .  .   .\n`

DEFINE abcd ('STR', 'abcd')

- Input: `. . .  .   .\t\t. .  .   .\n``

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

---------

# Max Base

My nickname is Max, Programming language developer, Full-stack programmer. I love computer scientists, researchers, and compilers. ([Max Base](https://maxbase.org/))

## Asrez Team

A team includes some programmer, developer, designer, researcher(s) especially Max Base.

[Asrez Team](https://www.asrez.com/)


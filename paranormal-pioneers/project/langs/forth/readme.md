# PyFORTH
- an incomplete FORTH implementation in python
- based on http://lars.nocrew.org/forth2012/core/
## features
###implemented words - 102
|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
+|-|*|/|MOD|>|<|=|<>|AND|OR|INVERT|
XOR|LSHIFT|RSHIFT|ABS|MIN|MAX|.|CR|EMIT|DO|LOOP|+LOOP|
I|J|.R|."|S"|.S|DUP|2DUP|SWAP|2SWAP|ROT|2ROT|
OVER|2OVER|DROP|2DROP|.(|:|;|!|@|VARIABLE|CONSTANT|R>|
>R|R@|EXECUTE|C!|C@|TYPE|VALUE|TO|SOURCE|HERE|ALLOT|2R>
?DUP|SPACE|SPACES|0>|0<|0=|?DUP|1+|1-|2R@|TRUE|2>R
2+|2-|2*|2/|*/|/MOD|*/MOD|NEGATE|NIP|U.R|?|+!|
CREATE|,|C,|IF|ELSE|THEN|REPEAT|WHILE|UNTIL|BEGIN|FALSE|(|
'|0<>|BL|CELL+|2!|2@|


###missing words - 84
|||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
#|#>|#S|<#|>BODY|>IN|>NUMBER|ABORT|WITHIN|[COMPILE]|U>|UNUSED|
ABORT"|ALIGN|ALIGNED|BASE|CELLS|CHAR|CHAR+|CHARS|COUNT|DECIMAL|REFILL|ROLL
DEPTH|DOES>|ENVIRONMENT?|EVALUATE|EXIT|FILL|FIND|FM/MOD|HOLD|IMMEDIATE|LEAVE|LITERAL|
M*|MOVE|POSTPONE|QUIT|RECURSE|S>D|SIGN|SM/REM|STATE|U.|U<|UM*|
UM/MOD|UNLOOP|WORD|[|[']|[CHAR]|]|:NONAME|S\"|SOURCE-ID|TUCK|SAVE-INPUT|
?DO|ACTION-OF|AGAIN|BUFFER:|C"|CASE|COMPILE,|DEFER|DEFER!|DEFER@|ENDCASE|ENDOF|
ERASE|HEX|HOLDS|IS|MARKER|OF|PAD|PARSE|PARSE-NAME|PICK|
RESTORE-INPUT|KEY|ACCEPT

###special words - 2
as base is not implemented,
0X can be used to take the next word as a hexadecimal literal,
and .X can be used to print the number on top of the stack in hexadecimal format
##notes
due to dictionaries being hashtables, : will DELETE any definition of the same name from the current environment, rather than override it. Same with any other methods of adding entries to dictionaries

memory works differently than on most forth systems, so some more hacky FORTH tricks may not wor

there are no unsigned numbers

constants are not enforced
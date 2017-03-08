# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information - because only things that get measured get 
optimized. Words here are upper case to make reading easier, but are lower case in 
Liara Forth itself.

Last update: 08. March 2017

| Word                | Status   | Group         | Flags    | Size  | Cycles |
| :----------------   | -------- | ------------- | -------- | ----: | -----: | 
| .                   | fragment | ANSI core     | NC       | (TBA) |  (TBA) |
| .(                  | coded    | ANSI core ext | IM       | Forth | Forth  |
| ."                  | coded    | ANSI core     | CO NC    | (TBA) |  (TBA) |
| .BYTE               | coded    | Liara         | NC       | (TBA) |  (TBA) |
| .R                  | coded    | ANSI core ext | NC       | Forth |  Forth |
| .S                  | fragment | ANSI tools    | NC       | (TBA) |  (TBA) |
| /                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| /MOD                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| /STRING             | coded    | ANSI string   | NC       | (TBA) |  (TBA) |
| ,                   | coded    | ANSI core     | NC       | 11    |     29 |
| :                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ;                   | coded    | ANSI core     | CO IM NC | (TBA) |  (TBA) |
| # "number-sign"     | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| #> "number-greater" | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| #S "number-s"       | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ! "store"           | coded    | ANSI core     | NC       | 9     |  (TBA) |
| ? "question"        | coded    | ANSI tools    | NC       | (TBA) |  (TBA) |
| ?DUP                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| @ "fetch"           | coded    | ANSI core     | NC       | 4     |  (TBA) |
| (                   | coded    | ANSI core     | NC       | Forth |  Forth |
| \[                  | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| \['\] "brackettick" | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| \[CHAR\]            | coded    | ANSI core     | IM CO NC | (TBA) |  (TBA) |
| \]                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| \                   | coded    | ANSI core     | NC       | 4     |  (TBA) |
| ' "tick"            | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| *                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| */                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| */MOD               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| +                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| +!                  | coded    | ANSI core     | NC       | 15    |  (TBA) |
| -                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| -ROT                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| -TRAILING           | coded    | ANSI string   | NC       | (TBA) |  (TBA) |
| =                   | coded    | ANSI core     | NC       | 11    |  18-20 |
| <                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| <>                  | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| <# "less-number"    | coded    | ANSI core     | NC       |     8 |  (TBA) |
| >                   | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| >BODY               | coded    | ANSI core     | NC       | 3     |      6 |
| >IN                 | coded    | ANSI core     | NC       | 6     |  (TBA) |
| >NUMBER             | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| >R                  | coded    | ANSI core     | NC CO    | 7     |     22 |
| 0                   | coded    | Liara         | NC       | 7     |     12 |
| 0=                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| 0<                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| 0>                  | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| 0<>                 | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| 0BRANCH             | coded    | Liara         | CO IM    | (TBA) |  (TBA) |
| 1                   | coded    | Liara         | NC       | 7     |     12 |
| 1-                  | coded    | ANSI core     | NC       | 1     |      2 |
| 1+                  | coded    | ANSI core     | NC       | 1     |      2 |
| 2                   | coded    | Liara         | NC       | 7     |     12 |
| 2*                  | coded    | ANSI core     | NC       | 3     |  (TBA) |
| 2>R                 | coded    | ANSI core ext |    CO    | (TBA) |  (TBA) |
| 2R>                 | coded    | ANSI core ext |    CO    | (TBA) |  (TBA) |
| 2DROP               | coded    | ANSI core     | NC       | 6     |     13 |
| 2DUP                | coded    | ANSI core     | NC       | 10    |     23 |
| 2OVER               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| 2R@                 | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| 2SWAP               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| 2VARIABLE           | coded    | ANSI double   | NC       | (TBA) |  (TBA) |
| ABORT               | coded    | ANSI core     | (TBA)    | 6+    |     6+ | 
| ABORT"              | fragment | ANSI core     | NC       | (TBA) |  (TBA) |
| ABS                 | coded    | ANSI core     | NC       | 12    |  (TBA) |
| ACCEPT              | fragment | ANSI core     | -        | (TBA) |  (TBA) |
| AGAIN               | coded    | ANSI core ext | IM NC CO | 22    |     50 |
| ALIGN               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ALIGNED             | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ALLOT               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| AND                 | coded    | ANSI core     | NC       | 6     |  (TBA) |
| AT-XY               | fragment | ANSI facility | NC       | (TBA) |  (TBA) |
| BASE                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| BELL                | coded    | Gforth        | NC       | (TBA) |  (TBA) |
| BEGIN               | coded    | ANSI core     | IM CO NC | 6     |     13 |
| BL                  | coded    | ANSI core     | NC       | 7     |     12 |
| BOUNDS              | coded    | Gforth        | NC       | 9     |  (TBA) |
| BRANCH              | coded    | Liara         | IM CO NC | (TBA) |  (TBA) |
| BYE                 | coded    | ANSI tools    | NC       | 2     |    7-8 | 
| C,                  | coded    | ANSI core     | NC       | 13    |     28 |
| C!                  | coded    | ANSI core     | NC       | 11    |     29 |
| C@                  | coded    | ANSI core     | NC       | 11    |     16 |
| CELL+               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| CELLS               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| CHAR                | coded    | ANSI core     | NC       | 23    |  (TBA) |
| CHAR+               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| CHARS               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| CMOVE               | coded    | ANSI string   | NC       | (TBA) |  (TBA) |
| CMOVE>              | coded    | ANSI string   | NC       | (TBA) |  (TBA) |
| COLD                | coded    | Gforth        |          | (TBA) |  (TBA) |
| COMPILE,            | coded    | ANSI core ext | CO IM    | (TBA) |  (TBA) |
| COMPILE-ONLY        | coded    | Gforth        | NC       | 8     |  (TBA) |
| CONSTANT            | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| COUNT               | coded    | ANSI core     | NC       | 14    |  (TBA) |
| CR                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| CREATE              | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| D+                  | coded    | ANSI double   | NC       | (TBA) |  (TBA) |
| D-                  | coded    | ANSI double   | NC       | (TBA) |  (TBA) |
| D.                  | coded    | ANSI double   |          | Forth |  Forth |
| D.R                 | coded    | ANSI double   |          | Forth |  Forth |
| D>S                 | coded    | ANSI double   | NC       | (TBA) |  (TBA) |
| DABS                | coded    | ANSI double   | NC       | (TBA) |  (TBA) |
| DECIMAL             | coded    | ANSI core     | NC       | 7     |  (TBA) |
| DEFER               | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| DEPTH               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| DIGIT?              | coded    | Gforth        | NC       | (TBA) |  (TBA) |
| DNEGATE             | coded    | ANSI double   | NC       | 19    |  (TBA) |
| DOES>               | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| DROP                | coded    | ANSI core     | NC       | 4     |      9 |
| DUMP                | fragment | ANSI tools    | NC       | (TBA) |  (TBA) |
| DUP                 | coded    | ANSI core     | NC       | 4     |      9 |
| ELSE                | coded    | ANSI core     | IM CO    | Forth |  Forth |
| EMIT                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ERASE               | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| EVALUATE            | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| EXECUTE             | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| FALSE               | coded    | ANSI core ext | NC       | 7     |     12 |
| FILL                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| FIND                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| FIND-NAME           | coded    | Gforth        | NC       | (TBA) |    n/a |
| FM/MOD              | coded    | ANSI core     | NC       | Forth |  Forth |
| HERE                | coded    | ANSI core     | NC       | 6     |     13 |
| HEX                 | coded    | ANSI core     | NC       | 7     |  (TBA) |
| HOLD                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| IF                  | coded    | ANSI core     | IM CO    | Forth |  Forth |
| IMMEDIATE           | coded    | ANSI core     | NC       | 8     |  (TBA) |
| INPUT               | coded    | Liara         | NC       | (TBA) |  (TBA) |
| INT>NAME            | coded    | Liara         | NC       | (TBA) |  (TBA) |
| INVERT              | coded    | ANSI core     | NC       | 5     |  (TBA) |
| KEY                 | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| LATESTNT            | coded    | Liara         | NC       | 7     |  (TBA) |
| LATESTXT            | coded    | Gforth        | NC       | (TBA) |  (TBA) |
| LSHIFT              | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| LITERAL             | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| M*                  | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| MARKER              | coded    | ANSI core ext | IM NC    | (TBA) |  (TBA) |
| MAX                 | coded    | ANSI core     | NC       | 18    |  (TBA) |
| MIN                 | coded    | ANSI core     | NC       | 18    |  (TBA) |
| MOVE                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| NAME>INT            | coded    | Gforth        | NC       | 4     |      8 |
| NAME>STRING         | coded    | Gforth        | NC       | 16    |  (TBA) |
| NATIVE-COMPILE      | coded    | Liara         | NC       | (TBA) |  (TBA) |
| NEGATE              | coded    | ANSI core     | NC       | 6     |  (TBA) |
| NIP                 | coded    | ANSI core ext | NC       | 2     |      4 |
| NUMBER              | coded    | Liara         | NC       | (TBA) |  (TBA) |
| OR                  | coded    | ANSI core     | NC       | 6     |  (TBA) |
| OUTPUT              | coded    | Liara         | NC       | (TBA) |  (TBA) |
| OVER                | coded    | ANSI core     | NC       | 6     |     14 |
| PAD                 | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| PAGE                | coded    | ANSI facility | NC       | (TBA) |  (TBA) |
| PARSE               | coded    | ANSI core ext |          | 45    |    n/a |
| PARSE-NAME          | coded    | ANSI core ext |          | 41+   |    n/a |
| PICK                | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| POSTPONE            | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| QUIT                | fragment | ANSI core     |          | (TBA) |    n/a |
| R@                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| R>                  | coded    | ANSI core     | CO       | 7     |     23 |
| REFILL              | fragment | ANSI core ext |          | (TBA) |  (TBA) |
| REPEAT              | coded    | ANSI core     | IM CO    | Forth |  Forth |
| RSHIFT              | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| ROT                 | coded    | ANSI core     | NC       | 8     |  (TBA) |
| S"                  | coded    | ANSI core     | IM NC    | (TBA) |  (TBA) |
| S>D                 | coded    | ANSI core     | NC       | 14    |  (TBA) |
| SIGN                | coded    | ANSI core     | NC       | 13    |  (TBA) |
| SLITERAL            | coded    | ANSI string   | IM CO    | (TBA) |  (TBA) |
| SM/REM              | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| SOURCE              | coded    | ANSI core     | NC       | 12    |  (TBA) |
| SOURCE-ID           | coded    | ANSI core ext | NC       | 6     |     13 |
| SPACE               | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| SPACES              | coded    | ANSI core     | NC       | 12    |  (TBA) |
| STATE               | coded    | ANSI core     | NC       | 7     |     12 |
| SWAP                | coded    | ANSI core     | NC       | 5     |     12 |
| THEN                | coded    | ANSI core     | IM CO    | Forth |  Forth |
| TO                  | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| TRUE                | coded    | ANSI core ext | NC       | 7     |     12 |
| TUCK                | coded    | ANSI core ext | NC       | 8     |     19 |
| TYPE                | fragment | ANSI core     | -        | Forth |  Forth |
| U.                  | coded    | ANSI core     |          | Forth |  Forth |
| U.R                 | coded    | ANSI core ext |          | Forth |  Forth |
| UD.                 | coded    | ANSI core     |          | Forth |  Forth |
| UD.R                | coded    | ANSI core     |          | Forth |  Forth |
| UM*                 | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| UD/MOD              | coded    | Gforth        | NC       | (TBA) |  (TBA) |
| UM/MOD              | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| UNUSED              | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| VALUE               | coded    | ANSI core ext | NC       | (TBA) |  (TBA) |
| VARIABLE            | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| WORD                | coded    | ANSI core     | NC       | (TBA) |  (TBA) |
| WORDS               | coded    | ANSI tools    | NC       | (TBA) |  (TBA) |
| WORDS&SIZES         | coded    | Liara         | NC       | (TBA) |  (TBA) |
| WORDSIZE            | coded    | Liara         | NC       | (TBA) |  (TBA) |
| XOR                 | coded    | ANSI core     | NC       | 6     |  (TBA) |


### Entries

***Status*** - State of development. Either **fragment** or **coded**.

***Group*** - Which word group the word belongs to, especially ANSI or non-ANSI.
Words written especially for the board are marked with "Liara", words that come
from Gforth with "Gforth". See [the Forth Standard](https://forth-standard.org/)
for basis.

***Flags*** - **CO** (compile only), **IM** (immediate word), 
**NC** (Native Compile Allowed)

***Size*** - If a native word, number of bytes the code uses (without the
initial JSR call and final RTS, which together add 4 bytes and 12 cycles). If
the information is not available yet, size is "(TBA)". 

***Cycles*** - For native words, the number of machine cycles the routine uses.
For Forth words, this will usually be "n/a" because of the effort involved.  If
the information is not available yet, size is "(TBA)". If the routine calls
other words or includes loops, there will be a "+" after the cycle number. 

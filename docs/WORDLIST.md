# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information - because only things that get measured get 
optimized. Words here are upper case to make reading easier, but are lower case in 
Liara Forth itself. 

Last update: 18. September 2017

| Word                | Status   | Group         | Flags    | Size  | Cycles |
| :----------------   | -------- | ------------- | -------- | ----: | -----: | 
| .                   | fragment | ANSI core     |          | (TBA) |  (TBA) |
| .(                  | coded    | ANSI core ext | IM       | Forth | Forth  |
| ."                  | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| .BYTE               | coded    | Liara         |          | (TBA) |  (TBA) |
| .R                  | coded    | ANSI core ext |          | Forth |  Forth |
| .S                  | fragment | ANSI tools    |          | (TBA) |  (TBA) |
| /                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| /MOD                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| /STRING             | coded    | ANSI string   |          | (TBA) |  (TBA) |
| ,                   | coded    | ANSI core     |          | 11    |     29 |
| :                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ;                   | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| # "number-sign"     | coded    | ANSI core     |          | (TBA) |  (TBA) |
| #> "number-greater" | coded    | ANSI core     |          | (TBA) |  (TBA) |
| #S "number-s"       | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ! "store"           | coded    | ANSI core     |          | 9     |  (TBA) |
| ? "question"        | coded    | ANSI tools    |          | (TBA) |  (TBA) |
| ?DO                 | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ?DUP                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| @ "fetch"           | coded    | ANSI core     |          | 4     |  (TBA) |
| (                   | coded    | ANSI core     |          | Forth |  Forth |
| (+LOOP)             | coded    | Liara         | CO       | (TBA) |  (TBA) |
| (?DO)               | coded    | Liara         | CO       | (TBA) |  (TBA) |
| (DO)                | coded    | Liara         | CO       | (TBA) |  (TBA) |
| \[                  | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| \['\] "brackettick" | coded    | ANSI core     |          | (TBA) |  (TBA) |
| \[CHAR\]            | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| \]                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| \                   | coded    | ANSI core     |          | 4     |  (TBA) |
| ' "tick"            | coded    | ANSI core     |          | (TBA) |  (TBA) |
| *                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| */                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| */MOD               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| +                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| +!                  | coded    | ANSI core     |          | 15    |  (TBA) |
| +LOOP               | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| -                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| -ROT                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| -TRAILING           | coded    | ANSI string   |          | (TBA) |  (TBA) |
| =                   | coded    | ANSI core     |          | 11    |  18-20 |
| <                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| <>                  | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| <# "less-number"    | coded    | ANSI core     |          |     8 |  (TBA) |
| >                   | coded    | ANSI core     |          | (TBA) |  (TBA) |
| >BODY               | coded    | ANSI core     |          | 3     |      6 |
| >IN                 | coded    | ANSI core     |          | 6     |  (TBA) |
| >NUMBER             | coded    | ANSI core     |          | (TBA) |  (TBA) |
| >R                  | coded    | ANSI core     | CO       | 7     |     22 |
| 0                   | coded    | Liara         |          | 7     |     12 |
| 0=                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| 0<                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| 0>                  | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| 0<>                 | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| 0BRANCH             | coded    | Liara         | CO IM    | (TBA) |  (TBA) |
| 1                   | coded    | Liara         |          | 7     |     12 |
| 1-                  | coded    | ANSI core     |          | 1     |      2 |
| 1+                  | coded    | ANSI core     |          | 1     |      2 |
| 2                   | coded    | Liara         |          | 7     |     12 |
| 2*                  | coded    | ANSI core     |          | 3     |  (TBA) |
| 2>R                 | coded    | ANSI core ext | CO       | (TBA) |  (TBA) |
| 2R>                 | coded    | ANSI core ext | CO       | (TBA) |  (TBA) |
| 2DROP               | coded    | ANSI core     |          | 6     |     13 |
| 2DUP                | coded    | ANSI core     |          | 10    |     23 |
| 2OVER               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| 2R@                 | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| 2SWAP               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| 2VARIABLE           | coded    | ANSI double   |          | (TBA) |  (TBA) |
| ABORT               | coded    | ANSI core     |          | 6+    |     6+ | 
| ABORT"              | fragment | ANSI core     |          | (TBA) |  (TBA) |
| ABS                 | coded    | ANSI core     |          | 12    |  (TBA) |
| ACCEPT              | fragment | ANSI core     |          | (TBA) |  (TBA) |
| AGAIN               | coded    | ANSI core ext | IM    CO | 22    |     50 |
| ALIGN               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ALIGNED             | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ALLOT               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| AND                 | coded    | ANSI core     |          | 6     |  (TBA) |
| AT-XY               | fragment | ANSI facility |          | (TBA) |  (TBA) |
| BASE                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| BELL                | coded    | Gforth        |          | (TBA) |  (TBA) |
| BEGIN               | coded    | ANSI core     | IM CO    | 6     |     13 |
| BL                  | coded    | ANSI core     |          | 7     |     12 |
| BOUNDS              | coded    | Gforth        |          | 9     |  (TBA) |
| BRANCH              | coded    | Liara         | IM CO    | (TBA) |  (TBA) |
| BYE                 | coded    | ANSI tools    |          | 2     |    7-8 | 
| C,                  | coded    | ANSI core     |          | 13    |     28 |
| C!                  | coded    | ANSI core     |          | 11    |     29 |
| C@                  | coded    | ANSI core     |          | 11    |     16 |
| CELL+               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| CELLS               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| CHAR                | coded    | ANSI core     |          | 23    |  (TBA) |
| CHAR+               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| CHARS               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| CMOVE               | coded    | ANSI string   |          | (TBA) |  (TBA) |
| CMOVE>              | coded    | ANSI string   |          | (TBA) |  (TBA) |
| COLD                | coded    | Gforth        |          | (TBA) |  (TBA) |
| COMPILE,            | coded    | ANSI core ext | CO IM    | (TBA) |  (TBA) |
| COMPILE-ONLY        | coded    | Gforth        |          | 8     |  (TBA) |
| CONSTANT            | coded    | ANSI core     |          | (TBA) |  (TBA) |
| COUNT               | coded    | ANSI core     |          | 14    |  (TBA) |
| CR                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| CREATE              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| D+                  | coded    | ANSI double   |          | (TBA) |  (TBA) |
| D-                  | coded    | ANSI double   |          | (TBA) |  (TBA) |
| D.                  | coded    | ANSI double   |          | Forth |  Forth |
| D.R                 | coded    | ANSI double   |          | Forth |  Forth |
| D>S                 | coded    | ANSI double   |          | (TBA) |  (TBA) |
| DABS                | coded    | ANSI double   |          | (TBA) |  (TBA) |
| DECIMAL             | coded    | ANSI core     |          | 7     |  (TBA) |
| DEFER               | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| DEPTH               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| DIGIT?              | coded    | Gforth        |          | (TBA) |  (TBA) |
| DNEGATE             | coded    | ANSI double   |          | 19    |  (TBA) |
| DO                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| DOES>               | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| DROP                | coded    | ANSI core     |          | 4     |      9 |
| DUMP                | fragment | ANSI tools    |          | (TBA) |  (TBA) |
| DUP                 | coded    | ANSI core     |          | 4     |      9 |
| ELSE                | coded    | ANSI core     | IM CO    | Forth |  Forth |
| EMIT                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ERASE               | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| EVALUATE            | coded    | ANSI core     |          | (TBA) |  (TBA) |
| EXECUTE             | coded    | ANSI core     |          | (TBA) |  (TBA) |
| EXIT                | coded    | ANSI core     |    CO    | (TBA) |  (TBA) |
| FALSE               | coded    | ANSI core ext |          | 7     |     12 |
| FILL                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| FIND                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| FIND-NAME           | coded    | Gforth        |          | (TBA) |    n/a |
| FM/MOD              | coded    | ANSI core     |          | Forth |  Forth |
| HERE                | coded    | ANSI core     |          | 6     |     13 |
| HEX                 | coded    | ANSI core     |          | 7     |  (TBA) |
| HOLD                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| I                   | coded    | ANSI core     |    CO    | (TBA) |  (TBA) |
| IF                  | coded    | ANSI core     | IM CO    | Forth |  Forth |
| IMMEDIATE           | coded    | ANSI core     |          | 8     |  (TBA) |
| INPUT               | coded    | Liara         |          | (TBA) |  (TBA) |
| INT>NAME            | coded    | Liara         |          | (TBA) |  (TBA) |
| INVERT              | coded    | ANSI core     |          | 5     |  (TBA) |
| J                   | coded    | ANSI core     |    CO    | (TBA) |  (TBA) |
| KEY                 | coded    | ANSI core     |          | (TBA) |  (TBA) |
| KEY?                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| LATESTNT            | coded    | Liara         |          | 7     |  (TBA) |
| LATESTXT            | coded    | Gforth        |          | (TBA) |  (TBA) |
| LEAVE               | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| LITERAL             | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| LOOP                | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| LSHIFT              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| M*                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| MARKER              | coded    | ANSI core ext | IM       | (TBA) |  (TBA) |
| MAX                 | coded    | ANSI core     |          | 18    |  (TBA) |
| MIN                 | coded    | ANSI core     |          | 18    |  (TBA) |
| MOD                 | coded    | ANSI core     |          | (TBA) |  (TBA) |
| MOVE                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| NAME>INT            | coded    | Gforth        |          | 4     |      8 |
| NAME>STRING         | coded    | Gforth        |          | 16    |  (TBA) |
| NC-LIMIT            | coded    | Liara         |          | (TBA) |  (TBA) |
| NEGATE              | coded    | ANSI core     |          | 6     |  (TBA) |
| NEVER-COMPILE       | coded    | Liara         |          | (TBA) |  (TBA) |
| NIP                 | coded    | ANSI core ext |          | 2     |      4 |
| NUMBER              | coded    | Liara         |          | (TBA) |  (TBA) |
| OR                  | coded    | ANSI core     |          | 6     |  (TBA) |
| OUTPUT              | coded    | Liara         |          | (TBA) |  (TBA) |
| OVER                | coded    | ANSI core     |          | 6     |     14 |
| PAD                 | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| PAGE                | coded    | ANSI facility |          | (TBA) |  (TBA) |
| PARSE               | coded    | ANSI core ext |          | 45    |    n/a |
| PARSE-NAME          | coded    | ANSI core ext |          | 41+   |    n/a |
| PICK                | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| POSTPONE            | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| QUIT                | fragment | ANSI core     |          | (TBA) |    n/a |
| R@                  | coded    | ANSI core     |          | (TBA) |  (TBA) |
| R>                  | coded    | ANSI core     | CO       | 7     |     23 |
| RECURSE             | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| REFILL              | fragment | ANSI core ext |          | (TBA) |  (TBA) |
| REPEAT              | coded    | ANSI core     | IM CO    | Forth |  Forth |
| RSHIFT              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| ROT                 | coded    | ANSI core     |          | 8     |  (TBA) |
| S"                  | coded    | ANSI core     | IM       | (TBA) |  (TBA) |
| S>D                 | coded    | ANSI core     |          | 14    |  (TBA) |
| SIGN                | coded    | ANSI core     |          | 13    |  (TBA) |
| SLITERAL            | coded    | ANSI string   | IM CO    | (TBA) |  (TBA) |
| SM/REM              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| SOURCE              | coded    | ANSI core     |          | 12    |  (TBA) |
| SOURCE-ID           | coded    | ANSI core ext |          | 6     |     13 |
| SPACE               | coded    | ANSI core     |          | (TBA) |  (TBA) |
| SPACES              | coded    | ANSI core     |          | 12    |  (TBA) |
| STATE               | coded    | ANSI core     |          | 7     |     12 |
| SWAP                | coded    | ANSI core     |          | 5     |     12 |
| THEN                | coded    | ANSI core     | IM CO    | Forth |  Forth |
| TO                  | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| TRUE                | coded    | ANSI core ext |          | 7     |     12 |
| TUCK                | coded    | ANSI core ext |          | 8     |     19 |
| TYPE                | fragment | ANSI core     |          | Forth |  Forth |
| U.                  | coded    | ANSI core     |          | Forth |  Forth |
| U.R                 | coded    | ANSI core ext |          | Forth |  Forth |
| UD.                 | coded    | ANSI core     |          | Forth |  Forth |
| UD.R                | coded    | ANSI core     |          | Forth |  Forth |
| UD/MOD              | coded    | Gforth        |          | (TBA) |  (TBA) |
| UM*                 | coded    | ANSI core     |          | (TBA) |  (TBA) |
| UM/MOD              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| UNLOOP              | coded    | ANSI core     | CO       | (TBA) |  (TBA) |
| UNUSED              | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| VALUE               | coded    | ANSI core ext |          | (TBA) |  (TBA) |
| VARIABLE            | coded    | ANSI core     |          | (TBA) |  (TBA) |
| WITHIN              | coded    | ANSI core     |          | (TBA) |  (TBA) |
| WORD                | coded    | ANSI core     |          | (TBA) |  (TBA) |
| WORDS               | coded    | ANSI tools    |          | (TBA) |  (TBA) |
| WORDS&SIZES         | coded    | Liara         |          | (TBA) |  (TBA) |
| WORDSIZE            | coded    | Liara         |          | (TBA) |  (TBA) |
| XOR                 | coded    | ANSI core     |          | 6     |  (TBA) |


### Entries

***Status*** - State of development. Either **fragment** or **coded**.

***Group*** - Which word group the word belongs to, especially ANSI or non-ANSI.
Words written especially for the board are marked with "Liara", words that come
from Gforth with "Gforth". See [the Forth Standard](https://forth-standard.org/)
for basis.

***Flags*** - **CO** (Compile Only), **IM** (IMmediate word), 
**NN** (Never Natively compile), **AN** (Always Natively compile)

***Size*** - If a native word, number of bytes the code uses (without the
initial JSR call and final RTS, which together add 4 bytes and 12 cycles). If
the information is not available yet, size is "(TBA)". 

***Cycles*** - For native words, the number of machine cycles the routine uses.
For Forth words, this will usually be "n/a" because of the effort involved.  If
the information is not available yet, size is "(TBA)". If the routine calls
other words or includes loops, there will be a "+" after the cycle number. 

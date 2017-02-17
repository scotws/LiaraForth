# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information - because only things that get measured get 
optimized. 

Last update: *17. February 2017*

| Word                | Status   | Group         | Flags    | Size  | Cycles |
| :----------------   | -------- | ------------- | -------- | ----: | -----: | 
| . "dot"             | fragment | ANSI core     | PW NC    | (TBA) |  (TBA) |
| .( "dotparen"       | coded    | ANSI core ext | IM       | Forth | Forth  |
| ." "dotquote"       | coded    | ANSI core     | CO NC    | (TBA) |  (TBA) |
| .S "dot-s"          | fragment | ANSI tools    | PW NC    | (TBA) |  (TBA) |
| , "comma"           | coded    | ANSI core     | PW NC    | 11    |     29 |
| : "colon"           | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| ; "semicolon"       | coded    | ANSI core     | CO IM NC | (TBA) |  (TBA) |
| ! "store"           | coded    | ANSI core     | PW NC    | 9     |  (TBA) |
| ? "question"        | coded    | ANSI tools    | PW NC    | (TBA) |  (TBA) |
| @ "fetch"           | coded    | ANSI core     | PW NC    | 4     |  (TBA) |
| ( "paren"           | coded    | ANSI core     | PW NC    | Forth |  Forth |
| \[ "leftbracket"    | coded    | ANSI core     | PW CO IM | (TBA) |  (TBA) |
| \['\] "brackettick" | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| \[CHAR\]            | coded    | ANSI core     | IM CO NC | (TBA) |  (TBA) |
| \] "rightbracket"   | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| ' "tick"            | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| + "plus"            | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| - "minus"           | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| >IN "to-in"         | coded    | ANSI core     | PW NC    | 6     |  (TBA) |
| 0 "zero"            | coded    | 265SXB        | PW NC    | 7     |     12 |
| 0BRANCH             | coded    | 265SXB        | CO IM    | (TBA) |  (TBA) |
| 1 "one"             | coded    | 265SXB        | PW NC    | 7     |     12 |
| 1- "one-minus"      | coded    | ANSI core     | PW NC    | 1     |      2 |
| 1+ "one-plus"       | coded    | ANSI core     | PW NC    | 1     |      2 |
| 2 "two"             | coded    | 265SXB        | PW NC    | 7     |     12 |
| 2* "two-star"       | coded    | ANSI core     | PW NC    | 3     |  (TBA) |
| 2DROP               | coded    | ANSI core     | PW NC    | 6     |     13 |
| 2DUP                | coded    | ANSI core     | PW NC    | 10    |     23 |
| ABORT               | coded    | ANSI core     | (TBA)    | 6+    |     6+ | 
| ABS                 | coded    | ANSI core     | PW NC    | 12    |  (TBA) |
| ACCEPT              | fragment | ANSI core     | -        | (TBA) |  (TBA) |
| ALLOT               | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| AND                 | coded    | ANSI core     | PW NC    | 6     |  (TBA) |
| BASE                | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| BELL                | coded    | Gforth        | PW NC    | (TBA) |  (TBA) |
| BL                  | coded    | ANSI core     | PW NC    | 7     |     12 |
| BYE                 | coded    | ANSI tools    | PW NC    | 2     |    7-8 | 
| C, "c-comma"        | coded    | ANSI core     | PW NC    | 13    |     28 |
| C! "c-store"        | coded    | ANSI core     | PW NC    | 11    |     29 |
| C@ "c-fetch"        | coded    | ANSI core     | PW NC    | 11    |     16 |
| CELLS               | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| CHAR                | coded    | ANSI core     | PW NC    | 23    |  (TBA) |
| COLD                | coded    | 265SXB        | -        | (TBA) |  (TBA) |
| COMPILE,            | coded    | ANSI core ext | CO IM    | (TBA) |  (TBA) |
| COMPILE-ONLY        | coded    | Gforth        | PW NC    | 8     |  (TBA) |
| CONSTANT            | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| COUNT               | coded    | ANSI core     | PW NC    | 14    |  (TBA) |
| CR                  | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| CREATE              | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| DECIMAL             | coded    | ANSI core     | PW NC    | 7     |  (TBA) |
| DEPTH               | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| DOES>               | coded    | ANSI core     | CO IM    | (TBA) |  (TBA) |
| DROP                | coded    | ANSI core     | PW NC    | 4     |      9 |
| DUMP                | fragment | ANSI tools    | PW NC    | (TBA) |  (TBA) |
| DUP                 | coded    | ANSI core     | PW NC    | 4     |      9 |
| EVALUATE            | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| EXECUTE             | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| FALSE               | coded    | ANSI core ext | PW NC    | 7     |     12 |
| FIND-NAME           | coded    | Gforth        | PW NC    | (TBA) |    n/a |
| HERE                | coded    | ANSI core     | PW NC    | 6     |     13 |
| HEX                 | coded    | ANSI core     | PW NC    | 7     |  (TBA) |
| IMMEDIATE           | coded    | ANSI core     | PW NC    | 8     |  (TBA) |
| INVERT              | coded    | ANSI core     | PW NC    | 5     |  (TBA) |
| LITERAL             | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| MAX                 | coded    | ANSI core     | PW NC    | 18    |  (TBA) |
| MIN                 | coded    | ANSI core     | PW NC    | 18    |  (TBA) |
| NAME>INT            | coded    | Gforth        | PW NC    | 4     |      8 |
| NAME>STRING         | coded    | Gforth        | PW NC    | 16    |  (TBA) |
| NEGATE              | coded    | ANSI core     | PW NC    | 6     |  (TBA) |
| NIP                 | coded    | ANSI core ext | PW NC    | 2     |      4 |
| OR                  | coded    | ANSI core     | PW NC    | 6     |  (TBA) |
| OVER                | coded    | ANSI core     | PW NC    | 6     |     14 |
| PAD                 | coded    | ANSI core ext | PW NC    | (TBA) |  (TBA) |
| PAGE                | coded    | ANSI facility | PW NC    | (TBA) |  (TBA) |
| PARSE               | coded    | ANSI core ext | -        | 45    |    n/a |
| PARSE-NAME          | coded    | ANSI core ext | -        | 41+   |    n/a |
| POSTPONE            | coded    | ANSI core     | IM CO    | (TBA) |  (TBA) |
| QUIT                | fragment | ANSI core     | -        | (TBA) |    n/a |
| REFILL              | fragment | ANSI core ext | PW       | (TBA) |  (TBA) |
| ROT                 | coded    | ANSI core     | PW NC    | 8     |  (TBA) |
| S" "squote"         | coded    | ANSI core     | IM NC    | (TBA) |  (TBA) |
| SLITERAL            | coded    | ANSI string   | IM CO    | (TBA) |  (TBA) |
| SOURCE              | coded    | ANSI core     | PW NC    | 12    |  (TBA) |
| SOURCE-ID           | coded    | ANSI core ext | PW NC    | 6     |     13 |
| SPACE               | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| SPACES              | coded    | ANSI core     | PW NC    | 12    |  (TBA) |
| STATE               | coded    | ANSI core     | PW NC    | 7     |     12 |
| SWAP                | coded    | ANSI core     | PW NC    | 5     |     12 |
| TRUE                | coded    | ANSI core ext | PW NC    | 7     |     12 |
| TUCK                | coded    | ANSI core ext | PW NC    | 8     |     19 |
| TYPE                | fragment | ANSI core     | -        | 23+   |  (TBA) |
| UNUSED              | coded    | ANSI core ext | PW NC    | (TBA) |  (TBA) |
| VARIABLE            | coded    | ANSI core     | PW NC    | (TBA) |  (TBA) |
| WORDS               | coded    | ANSI tools    | PW NC    | (TBA) |  (TBA) |
| XOR                 | coded    | ANSI core     | PW NC    | 6     |  (TBA) |


### Entries

***Status*** - State of development. Goes from **planned, fragment, coded** to
finally **tested**.

***Group*** - Which word group the word belongs to, especially ANSI or non-ANSI.
Words written especially for the board are marked with "265SXB", words that come
from Gforth with "Gforth". See [the Forth Standard](https://forth-standard.org/)
for basis.

***Flags*** - **PW** (Primitive Word), **CO** (compile only), **IM** (immediate word), 
**NC** (Native Compile), or "-" for none

***Size*** - If a native word, number of bytes the code uses (without the final
RTS); if Forth word, number of characters. If the information is not available
yet, size is "(TBA)". 

***Cycles*** - For native words, the number of machine cycles the routine uses.
For Forth words, this will usually be "n/a" because of the effort involved.  If
the information is not available yet, size is "(TBA)". If the routine calls
other words, there will be a "+" after the cycle number. 

# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information. 

Last update: **31. Dec 2016**

| Word           | Status   | Group         | Flags  | Size  | Cycles |
| :------------- | -------- | ------------- | ------ | ----: | -----: | 
| , (COMMA)      | coded    | ANSI core     | PW, NC | 11    |     29 |
| + (PLUS)       | coded    | ANSI core     | PW, NC | (TBA) |  (TBA) |
| > (TO-IN)      | coded    | ANSI core     | PW, NC | 6     |  (TBA) |
| 0 (ZERO)       | coded    | 265SXB        | PW, NC | 7     |     12 |
| 1 (ONE)        | coded    | 265SXB        | PW, NC | 7     |     12 |
| 1+ (ONE-PLUS)  | coded    | ANSI core     | PW, NC | 1     |      2 |
| ABORT          | coded    | ANSI core     | (TBA)  | 6+    |     6+ | 
| ACCEPT         | fragment | ANSI core     | -      | (TBA) |  (TBA) |
| BYE            | coded    | ANSI tools    | PW, NC | 2     |    7-8 | 
| COUNT          | coded    | ANSI core     | PW, NC | 14    |  (TBA) |
| DROP           | coded    | ANSI core     | PW, NC | 4     |      9 |
| DUP            | coded    | ANSI core     | PW, NC | 4     |      9 |
| FALSE          | coded    | ANSI core ext | PW, NC | 7     |     12 |
| HERE           | coded    | ANSI core     | PW, NC | 6     |     13 |
| NIP            | coded    | ANSI core ext | PW, NC | 2     |      4 |
| PARSE          | coded    | ANSI core ext | -      | 45    |    n/a |
| PARSE-NAME     | coded    | Gforth        | -      | 41+   |    n/a |
| QUIT           | fragment | ANSI core     | -      | (TBA) |    n/a |
| REFILL         | fragment | ANSI core ext | PW     | (TBA) |  (TBA) |
| SOURCE         | coded    | ANSI core     | PW, NC | 12    |  (TBA) |
| SOURCE-ID      | coded    | ANSI core ext | PW, NC | 6     |     13 |
| STATE          | coded    | ANSI core     | PW, NC | 7     |     12 |
| SWAP           | coded    | ANSI core     | PW, NC | 5     |     12 |
| TRUE           | coded    | ANSI core ext | PW, NC | 7     |     12 |
| TUCK           | coded    | ANSI core ext | PW, NC | 8     |     19 |


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

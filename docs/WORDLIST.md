# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information. 

Last update: **07. Dec 2016**

| Word           | Status   | Group         | Flags  | Size  | Cycles |
| :------------- | -------- | ------------- | ------ | ----: | -----: | 
| + (PLUS)       | coded    | ANSI core     | PW, NC | 5     |     11 |
| 0 (ZERO)       | coded    | 265SXB        | PW, NC | 7     |     12 |
| 1 (ONE)        | coded    | 265SXB        | PW, NC | 7     |     12 |
| 1+ (ONE-PLUS)  | coded    | ANSI core     | PW, NC | 1     |      2 |
| ABORT          | fragment | ANSI core     | CO     | (TBA) |  (TBA) | 
| ACCEPT         | fragment | ANSI core     | -      | (TBA) |  (TBA) |
| BYE            | coded    | ANSI tools    | PW, NC | 2     |    7-8 | 
| DROP           | coded    | ANSI core     | PW, NC | 4     |      9 |
| DUP            | coded    | ANSI core     | PW, NC | 4     |      9 |
| FALSE          | coded    | ANSI core ext | PW, NC | 7     |     12 |
| HERE           | coded    | ANSI core     | PW, NC | 6     |     13 |
| NIP            | coded    | ANSI core ext | PW, NC | 2     |      4 |
| QUIT           | fragment | ANSI core     | -      | (TBA) |    n/a |
| REFILL         | fragment | ANSI core ext | PW     | (TBA) |  (TBA) |
| SOURCE-ID      | fragment | ANSI core ext | PW, NC | (TBA) |  (TBA) |
| SWAP           | coded    | ANSI core     | PW, NC | 5     |     12 |
| TRUE           | coded    | ANSI core ext | PW, NC | 7     |     12 |
| TUCK           | coded    | ANSI core ext | PW, NC | 8     |     19 |


### Entries

***Status*** - State of development. Goes from **planned, fragment, coded** to
finally **tested**.

***Group*** - Which word group the word belongs to, especially ANSI or
non-ANSI. Words written especially for the board are marked "265SXB". See [the
Forth Standard](https://forth-standard.org/) for basis.

***Flags*** - **PW** (Primitive Word), **CO** (compile only), **IM** (immediate word), 
**NC** (Native Compile), or "-" for none

***Size*** - If a native word, number of bytes the code uses (without the final
RTS); if Forth word, number of characters. If the information is not available
yet, size is "(TBA)". 

***Cycles*** - For native words, the number of machine cycles the routine uses.
For Forth words, this will usually be "n/a" because of the effort involved.  If
the information is not available yet, size is "(TBA)". If the routine calls
other words, there will be a "+" after the cycle number. 

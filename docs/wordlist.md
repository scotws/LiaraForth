# Wordlist for Liara Forth

This table is an alphabetical list of the words provided by Liara Forth, including
their status and other information. The information here is currently not
complete. 

Last update: **02. Dec 2016**

| Word        | Status   | Group      | Flags  | Size  | Cycles |
| :---------- | -------- | ---------- | ------ | ----: | -----: | 
| BYE         | coded    | ANSI tools | PW, NC | 2     |    7-8 | 
| DUP         | coded    | ANSI core  | PW, NC | 4     |      9 |
| QUIT        | fragment | ANSI core  | -      | (TBA) |    n/a |

### Entries

***Status*** - State of development. Goes from **planned, fragment, coded** to
**tested**.

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
the information is not available yet, size is "(TBA)".

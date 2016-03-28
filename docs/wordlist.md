# Wordlist for Liara Forth

This table is an alphabetical list of the words used by Liara Forth, including
their status and other information. The information here is currently not
complete. 

Last update: 28. March 2016

| Word | Status | Group | Flags | Size | Cycles |
| --- | --- | --- | --- | --- | --- | --- |
| DUP | planned | ANSI core | NC | (TBA) | (TBA) |

### Entries

***Status*** - State of development. Goes from planned, fragment, coded to
tested.

***Group*** - Which word group the word belongs to, especially ANSI or
non-ANSI. Words written especially for the board are marked "265SXB". 

***Flags*** - N (native word), C (compiled word), I (immediate word), or "-"
for "none"

***Size*** - If a native word, number of bytes the code uses (without the
final RTS); if Forth word, number of characters. 

***Cycles*** - For native words, the number of machine cycles the routine uses.
For Forth words, this will be "n/a" because of the effort involved.

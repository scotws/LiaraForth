# Comparison of Top of Stack (TOS) variants for Liara Forth

Summary of different native-coded ("primitive") Forth words with the TOS either
in the Direct Page, in register Y, or the accumulator A. See tos_szenarios.txt
for details on how the entries in this table were calculated. Number entries are
bytes/cycles used. Bold entries are the fastest, _not_ the smallest.


| Word | TOS DP | TOS A reg | TOS Y reg |
| :--- | ---- | ---- | ---- |
| @ | 4/12 | **4/7-8** | **4/7-8** |
| DROP | **2/4** | 4/9 | 4/9 |
| DUP | 6/14 | **4/9** | **4/9** |
| NIP | 6/14 | **4/9** | **4/9 ** |
| SWAP | 8/20 | **5/12** | **5/12** |
| TUCK | 12/29 | **8/19** | **8/19** |


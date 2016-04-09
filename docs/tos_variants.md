# Comparison of Top of Stack (TOS) variants for Liara Forth

Summary of different native-coded ("primitive") Forth words with the TOS either
in the Direct Page, in register Y, or the accumulator A. See tos_szenarios.txt
for details on how the entries in this table were calculated. Number entries are
bytes/cycles used. Bold entries are the fastest, _not_ the smallest. If all
three variants are the same speed, none is bold.


| Word | TOS DP b/c | TOS A b/c | TOS Y b/c |
| :--- | --- | --- | --- |
| ! | **11/24** | 12/26 | **11/24** |
| + | 10/21 | **5/11** | 7/15 |
| = | 18/33 | **14/20-23** | 15/22-25 | 
| >R | 5/13 | 5/13 | 5/13 |
| @ | 4/12 | **4/7-8** | **4/7-8** |
| DROP | **2/4** | 4/9 | 4/9 |
| DUP | 6/14 | **4/9** | **4/9** |
| INVERT | 7/9 | **3/3** | 5/7 | 
| NIP | 6/14 | **4/9** | **4/9** |
| OVER | 6/14 | 6/14 | 6/14 |
| R> | 5/14 | 5/14 | 5/14 |
| ROT | 12/30 | **8/20** | **8/20** |
| SWAP | 8/20 | **5/12** | **5/12** |
| TUCK | 12/29 | **8/19** | **8/19** |

Note that except for DROP, the TOS A and TOS Y variants are always faster. TOS A
and TOS Y are usually the same speed. 


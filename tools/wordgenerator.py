# Word Template Generator for Liara Forth 
# Scot W. Stevenson <scot.stevenson@gmail.com>
# First version: 02. Dez 2016
# This version: 04. Jan 2017

# Tool to create entries for the Dictionary and Code of a given Liara Forth
# word. Prints template to screen. For copy and paste into the code.

import sys

if sys.version_info.major != 3:
    print("FATAL: Python 3 required. Aborting.")
    sys.exit(1)

print("Word Template Generator for Liara Forth")
print("Scot W. Stevenson <scot.stevenson@gmail.com")
print("-- Remember to copy and paste with 'set paste' in vim --")

code_template = """
; -------------------------------------------------------------------
; {0} ( -- ) X bytes / X cycles
; {1}

a_{2:<14}nop
                nop
z_{2:<14}rts
"""

dict_template = """
h_{0:<5} .byte {2}, {{ PW + NC }}
        .word h_{1}, a_{0}, z_{0}
        .byte "{0}"
"""

entry_template = """
| {0:<15}| coded    | {1:<13} | PW, NC | (TBA) |  (TBA) |
"""

while True:

    i_name = input("Word name ('q' to quit): ")

    if i_name == "q":
        sys.exit(0)

    i_name_lower = i_name.strip().lower()
    i_name_upper = i_name_lower.upper()
    i_name_len = hex(len(i_name_lower))[2:]

    i_desc = input("Word description? ")
    i_group = input("Code group (eg 'ANSI core')? ")
    i_next = input("Next word in dictionary? ")

    i_next = i_next.strip().lower()

    print(code_template.format(i_name_upper, i_desc, i_name_lower)) 
    print(dict_template.format(i_name_lower, i_next, i_name_len)) 
    print(entry_template.format(i_name_upper, i_group))

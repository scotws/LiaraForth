# Jump Counter for Liara Forth 
# Scot W. Stevenson <scot.stevenson@gmail.com>
# First version: 06. March 2016
# This version: 06. March 2016

"""Tool that walks through the Liara Forth source code and prints the number of
subroutine jumps for each Forth word. The aim is to show which words have
speed-up potential. Assumes an assembler source file in Typist's Assembler Notation 
(TAN) that has correctly assembled.
"""

import argparse
import sys

if sys.version_info.major != 3:
    print("FATAL: Python 3 required. Aborting.")
    sys.exit(1)

print("Jump Counter for Liara Forth")
print("Scot W. Stevenson <scot.stevenson@gmail.com")

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', dest='source', required=True,\
        help='Liara Forth source file (required)')
args = parser.parse_args()

CYCLES_PER_JSR = 12     # Number of cycles that a JSR/RTS combo takes
CYCLES_PER_JMP = 3      # Number of cycles that a normal JMP takes
CYCLES_PER_JMPI = 5     # Cycles pro JMP.I instruction (would be 6 for 65C02)

words = {}
active_words = []

class Word:
    def __init__(self, name):
        self.name = name    # 'xt_<WORD>'
        self.jsr_count = 0
        self.jmp_count = 0
        self.jmpi_count = 0

with open(args.source, 'r') as f: 

    for l in f.readlines():

        # The xt of a forth word will be marked by the label 'xt_<WORD>' at the
        # beginning of the line, followed by one or more spaces. We look for
        # those. Do not strip for spaces. 
        if l.startswith('xt_'): 

            word = l.split()[0]
            words[word] = Word(word)
            active_words.append(word)
            print('WORD: {0}'.format(word))

            continue

        # 'z_<WORD>' marks the end of our definition, we print immediately to
        # have the rough sequence of words as in the source code
        if l.startswith('z_'): 

            # Construct the appropriate 'xt_<NAME>' string we use as an index
            endword = l.split()[0]
            w = 'xt_'+endword[2:]

            try:
                active_words.remove(w)
            except ValueError:
                print('Found end marker for {0} without {0}'.format(w))
                sys.exit(1)

            if words[w].jsr_count:
                print('      - {0} JSRs: {1} --> {2} cycles'.\
                        format(w, words[w].jsr_count,\
                        words[w].jsr_count*CYCLES_PER_JSR))

            if words[w].jmp_count:
                print('      - {0} JMPs: {1} --> {2} cycles'.\
                        format(w, words[w].jmp_count,\
                        words[w].jmp_count*CYCLES_PER_JMP))

            if words[w].jmpi_count:
                print('      - {0} JMP.Is: {1} --> {2} cycles'.\
                        format(w, words[w].jmpi_count,\
                        words[w].jmpi_count*CYCLES_PER_JMPI))

            continue

        # See if we have any jumps. Ignore jumps that are outside of the word
        # definitions. 
        cl = l.strip()

        # Skip empty lines, comments and directives. This should take care of
        # .byte lines with strings etc
        if (not cl) or cl.startswith(';') or cl.startswith('.'):
            continue

        # Count all jumps. We get false negatives if there is a label before
        # a jump in the line, but since we don't code that way, we can live with
        # that for the moment
        for w in active_words:

            if 'jsr ' in cl:
                words[w].jsr_count += 1
            
            if 'jmp ' in cl:
                words[w].jmp_count += 1

            if 'jmp.i ' in cl:
                words[w].jmpi_count += 1


# Print a list of the biggest JSR offenders
print('JSR offenders:')

offenders = []

for w in words.values():

    # Skip any word that doesn't have a JSR
    if not w.jsr_count:
        continue 

    offenders.append((w.jsr_count, w.name))
    offenders.sort(reverse=True)

# This is a total waste of time but pretty
longest_name = 0

for o in offenders:
    ol = len(o[1])

    if ol > longest_name:
        longest_name = ol 

# Print the table
for o in offenders:
    cycles = o[0]*CYCLES_PER_JSR
    print('{0:{l}}: {1:2} jsr --> {2:3} cycles'.format(o[1], o[0],\
            cycles, l=longest_name+1))

    
    




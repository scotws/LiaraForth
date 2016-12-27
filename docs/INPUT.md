# Input design for Liara Forth 
Scot W. Stevenson <scot.stevenson@gmail.com>
First version: 27. Dez 2016
This version: 27. Dez 2016

Liara Forth follows the ANS input model with REFILL instead of older forms. 

There are up to four possible input sources in Forth (C&D p. 155):

1. The keyboard ("user input device")

2. A character string in memory

3. A block file

4. A text file

To check which one is being used, we first would call BLK, which gives us the
number of a mass storage block being used or 0 for the "user input device"
(keyobard). In the second case, we use SOURCE-ID to find out where input is
coming from: 0 for the keyboard, -1 (0ffff) for a string in memory, and a number
n for a fileid.

Since Liara Forth currently doesn't support blocks, we can skip the BLK
instruction and go right to SOURCE-ID. 


## Starting up

The intial commands after reboot flow into each other:
``` 
COLD -> ABORT -> QUIT 
``` 

This is the same as with pre-ANSI Forths. However, QUIT calls REFILL to get the
input. There are four possible cases there, based on the four possible input
sources as defined by BLK and SOURCE-ID (see above):

1. **Keyboard entry.** This is the default. Get line of input via ACCEPT and
   return a TRUE flag even if the input string was empty.

2. **EVALUTE string.** Simply return a FALSE flag.

3. **Input from a buffer.** Not implemented yet.

4. **Input from a file.** Not implemented yet.


## The Command Line Interface

Liara Forth accepts input lines of up to 256 characters. It remembers one
previous input that can be accessed with CONTROL-p. 

This is done by having two input buffers, `ibuffer1` `ibuffer2`, and switching
between them. Which is the current one is stored in the current input buffer
(CIB) variable.


### SAVE-INPUT and RESTORE-INPUT

(see http://forth.sourceforge.net/standard/dpans/dpansa6.htm#A.6.2.2182)

### SOURCE

(http://forth.sourceforge.net/standard/dpans/a0006.htm)
(http://forth.sourceforge.net/standard/dpans/dpansa6.htm#A.6.1.2216)



### EVALUATE

(Automatically calls SAVE-INPUT and RESTORE-INPUT)
(http://forth.sourceforge.net/standard/dpans/a0006.htm)

### STATE 

(http://forth.sourceforge.net/standard/dpans/dpans6.htm#6.1.2250)

## Literature

[C&D] Conklin, Edward K.; Rather, Elizabeth D. *Forth Programmers Handbook,*
3.rd edition


# Input design for Liara Forth 
Scot W. Stevenson <scot.stevenson@gmail.com>
First version: 27. Dez 2016
This version: 27. Dez 2016

Liara Forth follows the ANS input model with REFILL instead of older forms. 

There are four possible input sources in Forth (C&D p. 155):

1. The keyboard ("user input device"):

## Starting up

The intial commands after reboot flow into each other:
``` 
COLD -> ABORT -> QUIT 
``` 

This is the same as with pre-ANSI Forths. However, QUIT calls REFILL to get the
input. There are various cases there:

1. **Keyboard entry.** This is the default. Get line of input via ACCEPT and
   return a TRUE flag even if the input string was empty.

2. **EVALUTE string.** Simply return a FALSE flag.

3. **Input from a buffer.** Not implemented yet.

4. **Input from a file.** Not implemented yet.


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


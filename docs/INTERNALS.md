# Internal Structure and Technical Notes for Liara Forth W65C265SXB 

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)

## Use of Registers

The 65816 only has three registers that can be used for general coding. Of
these, Liara Forth uses the Y register as the first element in the Data Stack
(Top of Stack, TOS), the X register as the Data Stack Pointer (DSP), and A for
various temporary use. All registers are assumed to be 16 bit wide unless
declared otherwise. 

## The Data Stack

The Data Stack (DS) is located in an area that starts at 00:02ff and grows
downwards (towards 00:0000). The DS itself starts at 00:02f0, leaving 15
bytes as a "flood plain" in case of stack underflow. 

The Data Stack Pointer (DSP) - the X register -
points to the _current_ element on the stack (Next On Stack, NOS), whereas the
top entry (Top of Stack, TOS) is the Y register. 

The actual DS consists of the 128 bytes (64 entries) addressed by a seven-bit
bit DSP. The eight bit of the DSP is used to detect over- or underflow
conditions. Because Liara Forth "runs with scissors" to enable fast speeds, this
bounds checking only takes place after the execution of a Forth word. 

## The Return Stack

The Return Stack (RS) is the 65816 system stack and starts at 00:07fff. It too
grows downwards (towards 00:0000). 

## The Dictionary 

The Dictionary consists of two parts: The Headers for each word, connected as a
simple linked list, and the code itself. 

Every header is at least nine bytes long:

### Links to Start and End of Code

Each word has two links defined in its header that point to the start of the
code ```(a_word)``` and the end - more exactly, to the first byte that is not
included in the code, usually the RTS instruction ```(z_word)```. These are used
for words that are natively compiled, that is, instead of including a subroutine
jump to this word when compiled, the actual code is included. Usually this is
the case with short primitive words.

## Aspects of Coding

Liara Forth is focussed on being fast, not small. For each primitive word, the
size in bytes and the speed in cycles are recorded in the source code. A list of
the size and execution time of the most used instructions in 16 bit mode is
included in the documentation folder. 


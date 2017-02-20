# Internal Structure and Technical Notes for Liara Forth 

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)

## Design Principles

Liara Forth started with a bunch of general principles.

1. **Speed over size (within reason).** Liara Forth aims to make up for the
   relastively slow clock speed of the 65816 MPU in the 265SXB package. 
2. **Run with scissors.** There is very little safety checking in the individual
   words. Liara Forth will rarely tell you if there is an under- or overflow,
   for instance. During the design phase, these sort of checks were considered,
   but they added so much code that the first principle was violated.
3. **Use only the most basic hardware-dependent routines,** which are `put_chr` and
   `get_chr`. This is to make it easier for other people to port Liara Forth to
   other 65816 machines. 


## Use of Registers

The 65816 only has three registers that can be used for general coding. Of
these, Liara Forth uses the Y register as the first element in the Data Stack
("Top of Stack", TOS), the X register as the Data Stack Pointer (DSP), and A for
various temporary use. All registers are assumed to be 16 bit wide unless
declared otherwise. 


## The Data Stack

The Data Stack (DS) is located in an area that starts at 00:02ff and grows
downwards (towards 00:0000). The DS itself starts at 00:02f8, leaving some bytes
as a "flood plain" in case of stack underflow. Except for special cases,
underflow is only checked for after a word has been executed. We do not check
for overflow. 

The Data Stack Pointer (DSP) - the X register - points to the second element on
the stack (Next On Stack, NOS). This means that when the DS is empty, X is equal
to the initial value of the pointer (called `dsp0` in the code). The content of
this cell is garbage.  When there is one element on the DS, X is `dsp0-2`, but
the value at that location is also garbage, because TOS is in the Y register.
When there are two elements on the DS, X is `dsp0-4`, and the value at that
location is NOS. See Mike Barry's
[discussion](http://forum.6502.org/viewtopic.php?p=50546#p50546) of this at
6502.org for drawings of the various stack stages.

The DS grows towards the system variables that begin at 00:200 in single-user
mode. Currently (February 2017) there are 40 bytes used this way.


## The Return Stack

The Return Stack (RS) is the 65816 system stack and starts at 00:07fff in
single-user mode. It too grows downwards (towards 00:0000). 


## The Dictionary 

The Dictionary consists of two parts: The headers for each word, connected as a
simple linked list, and the code itself. Headers and code are kept separately to
enable various tricks in the code. 

Each word has a "name token" (``nt_word`` in the code) that points to the first
byte of the header, and an "execution token" (``xt_word``) that points to the
start of the code. There is a third pointer that references the byte _after_ the
end of the code (``z_word``) to enable native compilation of the word if
appropriate. 

Each header consists of one byte for the length of the word's string, a status
byte (see below), a link to the next word in the Dictionary (``0000`` marks its
end), the pointer to the beginning of the code (``xt_word``), the pointer to the
end of the code (``z_word``), and then the word's name string in plain ASCII,
without terminating space or zero.

The Dictionary consists of hard-coded routines in assembly, and Forth-coded
words that are generated when the system starts up (or after the COLD word). The
first hard-coded word is always DROP, the last one always BYE - use WORDS to get
a complete list. Any word that appears before DROP was automatically generated.

(During development, a large number of words were first included as high-level
Forth code or simple series of subroutine jumps, and then later optimized in
native code. The aim was to get the system up and running first.) 


## Compiling

Liara Forth follows the model of Subroutine Threaded Code (STC). As with a
Forths, there are two kinds of words: Natively coded "primitives" and high-level
sequences of subroutine jumps. These look something like this code fragment:

```
       jsr xt_allot       ; ALLOT
       jsr xt_nip         ; NIP
       jsr xt_execute     ; EXECUTE

```
This results in a structure that is simple and uses few registers, which is
important for the 65816. However, the resulting words can be large and slow. 
NIP looks like this in assembly:
```
       inx
       inx
       rts
```
Though the two INX instructions are 1 byte and 2 cycles each, the 
JSR/RTS combination adds 4 bytes and 12 cycles, for at total of 6 bytes and 16
cycles. 

To combat this, Liara Forth also _native compilation_, where the machine code
between the pointers ``xt_word`` and ``z_word`` is copied into the new word. If
in the example above, NIP were to be natively compiled, the resulting code would
be
```
       jsr xt_allot       ; ALLOT
       inx                ; NIP (natively compiled)
       inx
       jsr xt_execute     ; EXECUTE
```
This way, the NIP instruction is a short as it can be, compensating for a lot of
the problems with STC code.

There are two levels involved in native coding. First, a word must have the
Native Code Enabled flag (NC) set in the Dictionary header to enable the process
(not all words may be natively compiled, because some require the address of the
calling word on the Return Stack to function). Second, the compiler (in the word
``COMPILE,``) calculates the size of the machine code on the fly by subtracting
``xt_word`` from ``z_word`` and comparing it to a threshold value. If the size
is below that value, the word is natively compiled. 

(Because we are focussed on speed, it would be more logical to compare the
number of cycles used per word and then calculate the percentage of the JSR/RTS
overhead. If the code base ever stabilizes, this might be worth the effort.) 


## Aspects of Coding

Liara Forth is focussed on being fast, not small. A list of the size and
execution time of the most used instructions in 16 bit mode is included in the
documentation folder. 


## Notes (convert these later)

We use SM/REM instad of FM/MOD where the difference is not apparent

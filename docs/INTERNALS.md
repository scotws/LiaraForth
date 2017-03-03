# Internal Structure and Technical Notes for Liara Forth 

(THIS TEXT IS UNDER HEAVY DEVELOPMENT AND MERELY A COLLECTION OF NOTES)

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

The 65816 has three registers that can be used for general coding. Of these,
Liara Forth uses the Y register as the first element in the Data Stack ("Top of
Stack", TOS), the X register as the Data Stack Pointer (DSP), and A for various
temporary use. All registers are assumed to be 16 bit wide unless declared
otherwise. 


## The Data Stack

The Data Stack (DS) is located on the Direct Page (the 65816's version of the
6502's Zero Page), which is set to 00:0000 during Liara's startup. It grows
"downwards" (towards 00:0000). The DS itself starts at 00:01FF. Except for
special cases, underflow is only checked for after a word has been executed.
Liara does not check for overflow at all. 

Despite its name, the Data Stack Pointer (DSP) - the X register - points to the
_second_ element on the stack (Next On Stack, NOS), since the TOS is in the Y
register.
```
                   LSB       MSB
               +---------+---------+           
   Y register  |        TOS        |  
               +---------+---------+           

               +---------+---------+           
      00:02E6  |               ... |  
               +-     (empty)     -+           
      00:02E8  |                   |  
               +=========+=========+           
      00:02EA  |        NOS        |  00,X  <-- DSP (X register) 
               +---------+---------+           
      00:02EC  |        3OS        |  02,X
               +=========+=========+           
      00:02EE  |     (garbage)     |  04,X
               +---------+---------+           
      00:02F0  |     (garbage)     |  06,X  <-- DSP0
               +---------+---------+           
      00:02F2  |                   |  08,X
               +-   (floodplain)  -+
      00:02F4  |               ... |  0A,X  
               +---------+---------+           
```
_Snapshot of the Data Stack with three entries._ 

For push and pop (pull) actions, Y must be copied to the main body of the stack.
To push the number 0 on the stack (the **0** (ZERO) word), we use:
```
        dex
        dex
        sty.dx 00 
        ldy.# 0000
```

This means that when the DS is empty, X is equal to the initial value of the
pointer (called `dsp0` in the code). The actual content of this cell is garbage.
When there is one element on the DS, the value at that location is also garbage,
because TOS is in the Y register. When there are two elements on the DS, the DSP
points to NOS.  See Mike Barry's
[discussion](http://forum.6502.org/viewtopic.php?p=50546#p50546) of the stack
behavior for more details. 

**Double cell values:** The top cell is stored below (closer towards 00:0000)
the single cell. This places the sign bit at the beginning of the word in
the Y register.


## The Return Stack

The Return Stack (RS) is the 65816 system stack and starts at 00:01ff in
single-user mode. It too grows downwards (towards 00:0000). This way, an
underflow of the Data Stack will land in unused parts of the Return Stack, as
there is no page boundry wrapping in native mode (see
[http://6502.org/tutorials/65c816opcodes.html#5.1.1](http://6502.org/tutorials/65c816opcodes.html#5.1.1).


## The Dictionary 

The Dictionary consists of two parts: The headers for each word, connected as a
simple linked list, and the code itself. Headers and code are kept separately to
enable various tricks in the code. 

Each word has a "name token" (nt, ``nt_word`` in the code) that points to the
first byte of the header, and an "execution token" (xt, ``xt_word``) that points
to the start of the code. There is a third pointer that references the byte
_after_ the end of the code (``z_word``) to enable native compilation of the
word if allowed. 

Each header consists of one byte for the length of the word's string, a status
byte (see below), a link to the next word in the Dictionary (``0000`` marks its
end), the pointer to the beginning of the code (``xt_word``), the pointer to the
end of the code (``z_word``), and then the word's name string in plain ASCII,
without any terminating space or zero.

The Dictionary consists of hard-coded routines in assembly and Forth-coded words
that are generated when the system starts up (or after the COLD word). The first
hard-coded word is always DROP, the last one always BYE (use WORDS to get a
complete list and WORDS&SIZES for a list with the size of the code). Any word
that appears before DROP was automatically generated at boot from the Forth code.

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
Note the RTS instruction is removed. This way, the NIP instruction is a short as it can be, 
compensating for a lot of the problems with STC code.

There are two levels involved in native coding. First, a word must have the
Native Code enabled flag (NC) set in the Dictionary header to enable the process
(not all words may be natively compiled, because some require the address of the
calling word on the Return Stack to function). Second, the compiler (in the word
``COMPILE,``) calculates the size of the machine code on the fly by subtracting
``xt_word`` from ``z_word`` and comparing it to a threshold value ``nc-limit``.
If the size is below that value, the word is natively compiled. 

(Because we are focussed on speed, it would be more logical to compare the
number of cycles used per word and then calculate the percentage of the JSR/RTS
overhead. If the code base ever stabilizes, this might be worth the effort.) 


## Input of text

Liara Forth follows ANSI Forth by discarding the traditional word WORD for
REFILL and PARSE-NAME. FIND-NAME from Gforth is used instead of FIND. 
(See http://forum.6502.org/viewtopic.php?f=9&t=4364 for a discussion)


## Conversion of input numbers

- See https://www.forth.com/starting-forth/10-input-output-operators/ for a
  version of NUMBER ( addr u -- n | d )

  The Definition given is
```
VARIABLE punct  \ Hold the flag TRUE if number contains valid punctuation
: NUMBER ( addr u -- n | d )
  0 punct !             \ initialize flag, no punctuation occurred
  OVER C@               \ get the first digit
  [CHAR] - =            \ Is it a minus sign?
  DUP >R                \ Save flag on Return Stack
  IF 1 /STRING THEN     \ If is '-', strip the '-' character and continue
  0. 2SWAP              \ Provide double length zero as accumulator
  BEGIN
        >NUMBER
        DUP             \ While there are still chars left, get the digit
        WHILE
        OVER C@ DUP [CHAR] : =         \ a colon
        SWAP [CHAR] , [CHAR] /          \ a comma, hyphen, perido, slash
        1+
        WITHIN OR
        DUP punct !     \ set flag for punctuation
        0= ABORT" ? "   \ otherweise error message
        1 /STRING       \ skip punctionation character
 REPEAT                 \ exit if blank, else repeat conversion
 2DROP                  \ Drop string form stack
 R> IF DNEGATE THEN     \ If flag for minus is true, negate the d
 punct @  0= IF         \ If no punctuation, return single-value 
        DROP THEN
; 
```

- NUMBER is discussed page 87 in "Forth Programmer's Handbook" with the same
  format but no implementation

- Gforth uses S>NUMBER? and S>UNUMBER? which take a string and return either ( d
  f ) or ( ud f ), see
  https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/Line-input-and-conversion.html
  https://www.complang.tuwien.ac.at/forth/gforth/Docs-html/Number-Conversion.html


Gforth uses this for >NUMBER:
```
: >NUMBER  
  0 
  ?DO    COUNT DIGIT? 
         IF     ACCUMULATE 
         LOOP
         0 
  ELSE   1- I' I - UNLOOP 
  THEN ; 
```
with DIGIT? as
```
: DIGIT?  
  TOUPPER 48 - DUP 9 U> 
  IF     7 - DUP 9 U<= 
         IF     DROP FALSE EXIT 
         THEN 
  THEN 
  DUP USERADDR <112>  @ U>= 
  IF     DROP FALSE EXIT 
  THEN 
  TRUE ;
```
and ACCUMULATE as
```
: ACCUMULATE SWAP >R SWAP USERADDR <112>  @ UM* DROP ROT 
  USERADDR <112>  @ UM* D+ R> ;
```

pForth's version (see
https://github.com/philburk/pforth/blob/master/fth/numberio.fth)

```
: >NUMBER ( ud1 c-addr1 u1 -- ud2 c-addr2 u2 , convert till bad char , CORE )
    >r
    BEGIN
        r@ 0>    \ any characters left?
        IF
            dup c@ base @
            digit ( ud1 c-addr , n true | char false )
            IF
                TRUE
            ELSE
                drop FALSE
            THEN
        ELSE
            false
        THEN
    WHILE ( -- ud1 c-addr n  )
        swap >r  ( -- ud1lo ud1hi n  )
        swap  base @ ( -- ud1lo n ud1hi base  )
        um* drop ( -- ud1lo n ud1hi*baselo  )
        rot  base @ ( -- n ud1hi*baselo ud1lo base )
        um* ( -- n ud1hi*baselo ud1lo*basello ud1lo*baselhi )
        d+  ( -- ud2 )
        r> 1+     \ increment char*
        r> 1- >r  \ decrement count
    REPEAT
    r>
; 

```

One common example for >NUMBER includes
```
: TEST  0 0 BL WORD COUNT >NUMBER .S ; 
```
which in modern terms is 
```
: TEST 0 0 PARSE-NAME >NUMBER .S ; 
```
later followed by 
```
: TEST 0 0 PARSE-NAME >NUMBER 2DROP D>S . ; 
```


## Notes (convert these later)

- We use SM/REM instad of FM/MOD where the difference is not apparent
- Coding: Use MVN/MVP whenever possible. See
  http://forum.6502.org/viewtopic.php?f=2&t=1685&p=50975#p50975 for details. 

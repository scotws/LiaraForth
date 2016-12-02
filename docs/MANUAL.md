# Manual for Liara Forth for the W65C265SXB

Scot W. Stevenson <scot.stevenson@gmail.com>

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)
(SEE THE MANIFEST FOR AN OVERVIEW)

## Overview 

Liara Forth is a bare-metal Forth written specifically for the W65C265SXB
("265SXB") single-board computer from WDC based on the 65816 8/16-bit hybrid
CPU. It based on ANSI Forth and designed to be a "first Forth" that users can
install immediately after buying the board and additional Flash memory. The
final system includes an editor. 

Technically, Liara Forth based on the [Subroutine Threaded
Model](http://www.bradrodriguez.com/papers/moving1.htm) with a 16 bit cell size.
When complete, it will be a single-user system with round-robin multitasking.
Priority is "speed over size" (within reason). 

### Memory Map

![Liara Forth Memory Map]
(https://github.com/scotws/LiaraForth/blob/master/images/memorymap_20160401.png
"Liara Forth Memory Map")


## Further Information

There is a discussion thread at
[6502.org](http://forum.6502.org/viewtopic.php?f=9&t=3649) for Liara Forth.


## Setting Up the Hardware

The information in this section is based on the [Most Very Unofficial Guide to
the W65C265SXB](https://github.com/scotws/265SXB-Guide). 

### Accessing the 265SXB via a Terminal

### Adding Flash Memory

### Uploading Liara Forth


## Liara Forth Internals

(Included in the docs folder of this project is a file that describes the inner
workings of Liara Forth in more detail. In future, that information will be
included in this document.)

Liara Forth is heavily based on [Tali Forth for the
65c02](https://github.com/scotws/TaliForth) and shares the basic subroutine
threaded structure. 


### Typist's Assembler Notation (TAN)

Liara Forth is written in [Typist's Assembler
Notation](https://docs.google.com/document/d/16Sv3Y-3rHPXyxT1J3zLBVq4reSPYtY2G6OSojNTm4SQ/),
an alternative syntax to the "traditional" 6502/65816 notation. This code 
can be natively compiled with the [Tinkerer's
Assembler](https://github.com/scotws/tinkasm), or first semi-automatically
converted to the traditional syntax with
[typ65conv](https://github.com/scotws/type65conv). Coding in TAN is aided by
[syntax files for vim](https://github.com/scotws/Typist-VIM-Syntax) and an
automatic formatter that is part of the Tinkerer's Assembler. 

TAN provides various advantages over the traditional notation, especially when
spotting errors. The first stable version of Liara Forth will probably include a
version converted to traditional syntax.


## Testing Liara Forth with an Emulator

There are very few emulators for the 65816. Liara Forth was developed with
the [Crude Emulator for the 65816](https://github.com/scotws/crude65816).
It is written in Forth, but don't let that scare you. To use it, enable the
Mock Mensch Monitor ROM file must be in config.fs. 

Then, start [GNU Forth](https://www.gnu.org/software/gforth/) with extra 
memory:

```
gforth -m 64M
```
Then include the Crude Emulator, switch to native 65816 mode, and start Liara
Forth at 00:8000:

```
include crude65816.fs
native
8000 PC !
run
```

## Various Stuff


### License

Forth has a long tradition of being placed in the public domain. Liara Forth 
continues this. Where external code was used, it was also from the
public domain; see source code for documentation of individual routines. 

Liara Forth is provided on an "as is" basis without any warranty of any kind,
including, without limitation, the implied warranties of merchantability and
fitness for a particular purpose and their equivalents under the laws of any
jurisdiction. Put briefly, use this at your own risk.  


### About the Name

[Tali Forth](https://github.com/scotws/TaliForth) started as name I liked, but
(probably unavoidably) morphed into a reference to the "Mass Effect" character
Tali'Zorah vas Normandy, created by BioWare / Electronic Arts (EA). When it
became time to pick an name for the bigger, more powerful version for the
265SXB, the Asari character [Liara
T'Soni](http://masseffect.wikia.com/wiki/Liara_T'Soni) was the obvious
choice. This software has absolutely nothing to do with either the game or the
companies and neither do I, expect that I've played the games and enjoyed them.


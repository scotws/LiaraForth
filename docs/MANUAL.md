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
Model](http://www.bradrodriguez.com/papers/moving1.htm) (STC) with a 16 bit cell
size. When complete, it will be a single-user system with round-robin
multitasking. Priority is "speed over size" (within reason). Because of this,
there is little safety checking done - Liara "runs with scissors". 

### Memory Map

![Liara Forth Memory Map]
(https://github.com/scotws/LiaraForth/blob/master/images/memorymap_20160401.png
"Liara Forth Memory Map")


## Setting Up the Hardware

The information in this section is based on the [Most Very Unofficial Guide to
the W65C265SXB](https://github.com/scotws/265SXB-Guide). 

### Accessing the 265SXB via a Terminal

(Based on [Setting up the
265SXB](https://github.com/scotws/265SXB-Guide/blob/master/setup.md))

Getting the 265SXB up and running requires the board itself, a USB cable, and a
host computer. The board draws power via the USB connection, which is also used
for the terminal. This gives you access to the built-in monitor program.

**For Linux (Ubuntu):**

1. Attach a USB cable to the board at J6, the power jack in the bottom middle.
Attach the other end to your computer. This should make the power LED light up.

2. On the Ubuntu machine, we will use `putty` as a terminal program. If not
   already present, install it with `sudo apt-get install putty` from a shell.
   To start the terminal program, you might need to type `sudo putty` instead of
   just `putty`. Instead of putty, the command-line program `minicom` can be
   used. 

3. To find out which USB port on the host computer we are using, run `dmesg |
   grep tty` from the shell. In our case, the port is `/dev/ttyUSB0`.

4. Configure putty: Under the Terminal setting, enable "implicit LF in every
   CR". Under the Session setting, select "Serial" and use the port address
   found in the previous set as the Serial Line. Click "Open" at the bottom of
   the window to create the connection.

5. On the 265SXB, push the Reset button to the right of the power jack J6. This
   should bring up the Mensch Monitor


### Adding Flash Memory

(TBA, see https://github.com/scotws/265SXB-Guide/blob/master/flash.md )

### Uploading Liara Forth

(TBA) 

## Getting Started

Forth is a command-line based language. 

### Command Line Basics

Liara Forth does not distinguish between upper and lower case. Internally, all
words are converted to lower case.

## Liara Forth Internals

(Included in the docs folder of this project is a file that describes the inner
workings of Liara Forth in more detail. In future, that information will be
included in this document.)

Liara Forth is heavily based on [Tali Forth for the
65c02](https://github.com/scotws/TaliForth) and shares the basic subroutine
threaded structure. 


## Assembling Liara Forth

Liara Forth includes the source code to allow changes and modifications. See the
file COPYING.txt for details on license issues.

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
spotting errors. The first stable version of Liara Forth will include a version
converted to a traditional syntax.

### Assembly with the Tinkerer's Assembler

To assemble the source code, download [Tinkerer's
Assembler](https://github.com/scotws/tinkasm) which is coded in Python 3. Then,
in Liara Forth's main directory, run

```
python3 [PATH]/tinkasm -i liaraforth.tasm -v -d -l -x
```

where `[PATH]` is the correct file to where you stored the assembler. This will
produce lots of output, as well as a listing (because of `-l`), a binary file
`(tink.bin)` and a hex dump (`-x`). By default, the code is assembled to start
at 00:0000. 


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

[Tali Forth](https://github.com/scotws/TaliForth) started simply as name I
liked, but (probably unavoidably) morphed into a reference to the "Mass Effect"
character Tali'Zorah vas Normandy, created by BioWare / Electronic Arts (EA).
When it became time to pick an name for the bigger, more powerful version for
the 265SXB, the Asari character [Liara
T'Soni](http://masseffect.wikia.com/wiki/Liara_T'Soni) was the obvious choice.
This software has absolutely nothing to do with either the game or the companies
and neither do I, expect that I've played the games and enjoyed them.

### Further Information

There is a discussion thread at
[6502.org](http://forum.6502.org/viewtopic.php?f=9&t=3649) for Liara Forth.


### Links

See also the [list of
links](https://github.com/scotws/265SXB-Guide/blob/master/links.md) of the 
265SXB guide.

http://www.westerndesigncenter.com/wdc/documentation/W65C265SXB.pdf
265SXB Data Sheet

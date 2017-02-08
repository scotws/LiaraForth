# Manual for Liara Forth for the W65C265SXB

Scot W. Stevenson <scot.stevenson@gmail.com>

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)
(THE SETUP PART OF THIS TEXT IS CURRENTLY UNDERGOING MAJOR REVISIONS)

## Overview 

Liara Forth is a bare-metal Forth written specifically for the W65C265SXB
("265SXB") single-board computer from WDC based on the 65816 8/16-bit hybrid
CPU. It based on ANSI Forth and designed to be a "first Forth" that users can
install immediately after buying the board. 

Technically, Liara Forth based on the [Subroutine Threaded
Model](http://www.bradrodriguez.com/papers/moving1.htm) (STC) with a 16 bit cell
size. When complete, it will be a single-user system with round-robin
multitasking. Priority is "speed over size" (within reason). Because of this,
there is little safety checking done - Liara "runs with scissors". 

## Setting Up the Hardware

First, be aware that you are doing all this at your own risk. See the file
COPYING.txt for details and the section on the license at the end of this
document. 

On a more cheerful note, you might want to read the
more detailed instructions in the [Most Very Unofficial Guide to the
W65C265SXB](https://github.com/scotws/265SXB-Guide) for most of the steps here. 


### Accessing the 265SXB via a Terminal

We use two USB connections to work with LiaraForth: One for power and the
initial upload, the other for the terminal connection. 


**For Linux (Ubuntu):**

Currently, Liara Forth works best if you use two different terminal programs for
the two different connections: `minicom` to upload the code as an S-record (S28,
see below) and `putty` for the actual work. How to do this is described in
[Setting up the
265SXB](https://github.com/scotws/265SXB-Guide/blob/master/setup.md) in the Most
Very Unofficial Guide for the moment - when Liara Forth is out of Alpha, this
section here will be more detailed. 

For **minicom** (upload and power):

1. Attach a USB cable to the board at J6, the power jack in the bottom middle.
   Attach the other end to your computer. This should make the power LED light
   up.

2. To find out which USB port on the host computer we are using, run `dmesg |
   grep tty` from the shell. The port will be something like `/dev/ttyUSB0`.

3. If not already present, install `minicom` with `sudo apt-get install minicom`
   from a shell. To start the terminal program, you will need to type `sudo
   minicom -s` (sudo because Linux won't let normal people play with the USB
   ports like this).

4. Configure the serial device as `/dev/ttyUSB0` and the Bps speed as `9600`.
   Under the entry "Screen and keyboard", enable the adding of line feeds and
   carriage returns. Save the configuration as "265sxb".

5. After configuration, you can call the 265sxb with `sudo minicom 265sxb`.
   Press the reset button on the 265sxb if you don't see anything at first.

This drops you into the Mensch Monitor, a simple basic operating system. 


To set up **putty** (interface) :

1. Attach the second serial cable to UART 0 (see [the schematic and
   photos](https://github.com/scotws/265SXB-Guide/blob/master/serial_lines.md)
   in the 265SXB Guide). Use dmesg as above to figure out which USB port this is
   connecte to (probably `/dev/ttyUSB1`). 

2. If not already present, download with `sudo apt-get install putty`. Start it
   from a second terminal with `sudo putty`. 

3. Configure a Session as `Serial` and with the USB port as the serial line. Use
   `19200` as the speed. Make sure we have `8n1`. Further settins are `Backspace
   is ^H`, `Function keys vt100+`, `Implicit CR in every LF` and `Autowrap on`.
   If you don't like the default font (and you probably won't), change it to
   something more useful.

4. Save the session as `Liara Forth`. Follow the instructions below to upload
   the S-record file to the 265SXB and start the program. 


### Uploading Liara Forth to RAM 

At the beginning, you'll probably want to test Liara Forth by loading it to
RAM. This is an option as long as the code base is small enough - it is expected
that at some point, Liara will outgrow the available RAM.

Included in the main directory is a file `liaraforth.s28` (or possibly
`tink.s28` for PRE-ALPHA and ALPHA builds) which is a "S-record" of the code
that minicom (and other programs) know how to upload. It is set up to be saved
at 00:6000, which is also the starting address. 

From minicom connected to the Mensch Monitor as described above, type `s`. The
265sxb will now wait for the transmission of data to start. Now, type `CONTROL-a
z` to enter the minicom menu. Type `s` to start the upload, and then pick
`ascii` out of the following menu of transmission protocols. You will be offered
a file selector - mark the Liara Forth S28 file with SPACE, and select it with
ENTER. You should see an upload indicator.

![Minicom S-record upload]
(https://github.com/scotws/LiaraForth/blob/master/images/minicom_upload_20161227.png
"Minicom S-record upload")

The Mensch Monitor will offer the prompt again. To start Liara Forth, type `g`,
and then enter `00:6000` as the starting address. This will start your Forth
session on the second `putty` interface line. 


## Getting Started with Liara Forth

Liara Forth is based on the ANSI, but heavily influenced by
[Gforth](https://www.gnu.org/software/gforth/). Liara's code should run on
Gforth without changes, or have a good reason not to. Words taken from Gforth
are marked as such in the wordlist. 


### A Most Very Brief Introduction to Forth

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


## Modifying and Assembling Liara Forth

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
Forth at 00:8000 (for testing the Flash version):

```
include crude65816.fs
native
8000 PC !
run
```

### Creating a new S-Record to upload

After working on Liara Forth in the emulator, you will probably want to test it
on the real hardware. To start with RAM tests, you'll need to be able to convert
the binary file you assembled to a S-record we can upload. 

**For Ubuntu**, install
[srec_cat](http://srecord.sourceforge.net/man/man1/srec_examples.html) via
```
sudo apt-get install srecord
```

Convert the binary file (for example, ```tink.bin```) via
```
srec_cat tink.bin -binary -offset 0x6000 -o tink.s28 -address-length=3
-execution-start-address=0x6000
```
To make sure we have the correct format, use ```srec_info mensch.s28``` to
inspect the contents:
```
Format: Motorola S-Record
Header: "http://srecord.sourceforge.net/"
Execution Start Address: 00008000
Data:   6000 - 63F2
```
The second number in the "Data" field will be different. Then, upload the
S-record as described above.


## Installing Liara Forth to Flash memory

If you decide you want to install Liara Forth permanently, you'll probably want
to buy Flash memory chip and install it there. 


### Adding Flash Memory

(TBA, see https://github.com/scotws/265SXB-Guide/blob/master/flash.md )


### Memory Map with Flash

![Liara Forth Memory Map]
(https://github.com/scotws/LiaraForth/blob/master/images/memorymap_20160401.png
"Liara Forth Memory Map")


## Various Stuff


### License

Forth has a long tradition of being placed in the public domain. Liara Forth 
continues this. Where external code was used, it was also from the
public domain; see source code for documentation of individual routines. 

Liara Forth is provided on an "as is" basis without any warranty of any kind,
including, without limitation, the implied warranties of merchantability and
fitness for a particular purpose and their equivalents under the laws of any
jurisdiction. Put briefly, use this at your own risk.  


### Thanks 

A big thanks to the crew at 6502.org, without whom none of this would have
happend. Also, special thanks to Mike Barry for a steady stream of
most very clever code optimizations. 


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

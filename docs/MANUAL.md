# Manual for Liara Forth for the W65C265SXB

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)
(SEE THE MANIFEST FOR AN OVERVIEW)




## Typist's Assembler Notation (TAN)

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
version in traditional syntax.


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


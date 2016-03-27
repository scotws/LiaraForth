# Liara Forth, an "initial" ANSI(ish) Forth for the W65C265SXB (65816 CPU)

This is a project to create a (mostly) ANSI-compliant Forth for the 
W65C265SXB ("265SXB") that will work with the basic board and a single Flash
memory chip out of the box. 

The 265SXB is an engineering development board -- basically a single-board
computer in the same sense as the Raspberry Pi -- produced by the Western Design
Center (WDC). It is based on the W65C265S microcontroler, which in turn has a
65816 MPU at its core, the 8/16-bit hybrid "big sibling" of the famous 6502 MPU
that powered classic computers such as the VIC-20 and Apple II. Because of the
hybrid nature of the 65816, the 265SXB is pretty much the simplest way to get
started with a 6502 system.

This project is in the very, _very_ early design stage. See the Initial Design
Manifest in the docs folder for details. 

There is a discussion thread for Liara Forth [at
6502.org](http://forum.6502.org/viewtopic.php?f=9&t=3649).

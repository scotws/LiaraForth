# Liara Forth, an "initial" ANSI(ish) Forth for the W65C265SXB (65816 CPU)

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)



## Testing Liara Forth with an Emulator

For crude65816, the Mock Mensch Monitor ROM file is required in config.fs.
```
gforth -m 64M
include crude65816.fs
native
8000 PC !
run
```


# Manual for Liara Forth for the W65C265SXB

(THIS TEXT IS UNDER DEVELOPMENT AND MERELY A COLLECTION OF NOTES)


## Testing Liara Forth with an Emulator

For crude65816, the Mock Mensch Monitor ROM file is required in config.fs. Start
Forth with extra memory:
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


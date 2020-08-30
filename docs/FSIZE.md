# FSIZE

Returns the number of bytes in a file. Use FSIZE to determine the size
of the file, which is the same as the position of the last byte in the
file.

**Syntax**

**FSIZE**(**file\_num**)

File\_num&nbsp;&nbsp;&nbsp;&nbsp;is the unique ID number of the file
whose size you want to know. File\_num is returned by a previously
executed FOPEN function. If file\_num is not valid, FSIZE returns the
\#VALUE\! error value.

**Example**

The following function returns the size in bytes of the open file
identified as FileNumber:

FSIZE(FileNumber)

**Related Functions**

[FOPEN](FOPEN.md)&nbsp;&nbsp;&nbsp;Opens a file with the type of permission
specified

[FPOS](FPOS.md)&nbsp;&nbsp;&nbsp;Sets the position in a text file



Return to [README](README.md#F)


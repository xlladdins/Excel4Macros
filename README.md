# Excel4Macros

The ancient [Excel SDK](...) for creating C add-ins gives you access to the even more ancient
[Excel4 Macro language](...).
The SDK functions `Excel4` and `Excel12` use _function numbers_ defined in `XLCALL.H` to call any Excel function or macro.
In order to use those you need to know the arguments they take.

Microsoft Word documentation from  [Excel Forum](https://www.excelforum.com/tips-and-tutorials/1170158-xl4-macro-functions.html)
have been converted from `.doc` format to `.docx` format by opening the files in Word and saving them as `.docx`.

Run `make` to convert these to HTML documentation. 

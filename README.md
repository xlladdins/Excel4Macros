# Excel4Macros

The ancient
[Excel SDK](https://docs.microsoft.com/en-us/office/client-developer/excel/welcome-to-the-excel-software-development-kit)
for creating C add-ins gives you access to the even more ancient
[Excel4 Macro language](https://outflank.nl/blog/2018/10/06/old-school-evil-excel-4-0-macros-xlm/).
The SDK functions `Excel4` and `Excel12` use _function numbers_ defined in `XLCALL.H` to call any Excel function or macro.
In order to use those you need to know the arguments they take.

Microsoft Word documentation from
[Excel Forum](https://www.excelforum.com/tips-and-tutorials/1170158-xl4-macro-functions.html)
have been converted from `.doc` format to `.docx` format by opening the files in Word and saving them as `.docx`.

Run `make` to convert these to HTML documentation in the `/docs` directory.  
Run `make clean` to remove all build artifacts.

The documentation is published to [GitHub Pages](https://xlladdins.github.io/Excel4Macros/)

[Security Baseline](https://docs.microsoft.com/en-us/archive/blogs/secguide/security-baseline-for-office-2016-and-office-365-proplus-apps-final)

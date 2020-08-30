# OPTIONS.LISTS.GET

Returns contents of custom AutoFill lists as an array of text strings.

**Syntax**

**OPTIONS.LISTS.GET**(**list\_num**)

**OPTIONS.LISTS.GET**(**string\_array**)

List\_num&nbsp;&nbsp; is a number specifying which list to return, as a
horizontal string array. If list\_num is zero, then FALSE is returned.

String\_array&nbsp;&nbsp;&nbsp;&nbsp;is an array or cell reference to
store the returned list.

**Example**

OPTIONS.LIST.GET(3) returns the twelve months of the year in the form
{"Jan", "Feb", "Mar"}

**Remarks**

If list\_num is zero or omitted, then FALSE is returned.

**Related Functions**

[OPTIONS.LISTS.ADD](OPTIONS.LISTS.ADD.md)&nbsp;&nbsp;&nbsp;Adds a new custom list

[OPTIONS.LISTS.DELETE](OPTIONS.LISTS.DELETE.md)&nbsp;&nbsp;&nbsp;Deletes a custom list

[OPTIONS.VIEW](OPTIONS.VIEW.md)&nbsp;&nbsp;&nbsp;Sets various view settings



Return to [README](README.md#O)


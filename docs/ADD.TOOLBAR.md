# ADD.TOOLBAR

Creates a new toolbar with the specified buttons.

**Syntax**

**ADD.TOOLBAR**(**bar\_name**, tool\_ref)

Bar\_name&nbsp;&nbsp;&nbsp;&nbsp;is a text string identifying the
toolbar you want to create.

Tool\_ref&nbsp;&nbsp;&nbsp;&nbsp;is either a number specifying a
built-in button or a reference to an area on the macro sheet that
defines a custom button or set of buttons (or an array containing this
information).

For a complete description of tool\_ref, see ADD.TOOL.

**Remarks**

If you create a toolbar without buttons, use ADD.TOOL to add them. Use
SHOW.TOOLBAR to display the toolbar.

**Example**

The following macro formula creates Toolbar9 with one button in it. The
cell range B7:I7 contains tool\_ref.

ADD.TOOLBAR("Toolbar9", B7:I7)

**Related Functions**

[ADD.TOOL](ADD.TOOL.md)&nbsp;&nbsp;&nbsp;Adds a button to a toolbar

[DELETE.TOOL](DELETE.TOOL.md)&nbsp;&nbsp;&nbsp;Deletes a button from a toolbar

[DELETE.TOOLBAR](DELETE.TOOLBAR.md)&nbsp;&nbsp;&nbsp;Deletes custom toolbars

[RESET.TOOLBAR](RESET.TOOLBAR.md)&nbsp;&nbsp;&nbsp;Resets a built-in toolbar to its default
initial setting

[SHOW.TOOLBAR](SHOW.TOOLBAR.md)&nbsp;&nbsp;&nbsp;Hides or displays a toolbar



Return to [README](README.md#A)


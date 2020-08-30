# RELREF

Returns the reference of a cell or cells relative to the upper-left cell
of rel\_to\_ref. The reference is given as an R1C1-style relative
reference in the form of text, such as "R\[1\]C\[1\]".

**Syntax**

**RELREF**(**reference, rel\_to\_ref**)

Reference&nbsp;&nbsp;&nbsp;&nbsp;is the cell or cells to which you want
to create a relative reference.

Rel\_to\_ref&nbsp;&nbsp;&nbsp;&nbsp;is the cell from which you want to
create the relative reference.

**Tip**&nbsp;&nbsp;&nbsp;If you know the absolute reference of a cell
that you want to include in a formula, but your formula requires a
relative reference, use RELREF to generate the relative reference. This
is especially useful with the FORMULA function, since its formula\_text
argument requires R1C1-style references, and RELREF returns relative
R1C1-style references. You can also use the FORMULA.CONVERT function to
convert absolute references to relative references.

**Examples**

RELREF($A$1, $C$3) equals "R\[-2\]C\[-2\]"

RELREF($A$1:$E$5, $C$3:$G$7) equals "R\[-2\]C\[-2\]:R\[2\]C\[2\]"

RELREF($A$1:$E$5, $C$3) equals "R\[-2\]C\[-2\]:R\[2\]C\[2\]"

**Related Functions**

[ABSREF](ABSREF.md)&nbsp;&nbsp;&nbsp;Returns the absolute reference of a range of
cells to another range

[DEREF](DEREF.md)&nbsp;&nbsp;&nbsp;Returns the value of the cells in the reference

[FORMULA](FORMULA.md)&nbsp;&nbsp;&nbsp;Enters values into a cell or range or onto a
chart

[FORMULA.CONVERT](FORMULA.CONVERT.md)&nbsp;&nbsp;&nbsp;Changes the reference style and type



Return to [README](README.md#R)


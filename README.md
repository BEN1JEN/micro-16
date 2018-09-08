# micro-16
monochrome raspberry-pi powered hand-held console OS.
## Physical device:
### Parts:
* [raspberry zero](https://www.adafruit.com/product/3775)
* [st7565 display](https://www.adafruit.com/product/250)
* [clicky buttons](https://www.adafruit.com/product/1009)
* [joystick](https://www.adafruit.com/product/512)
* a custom pcb (maybe)
* a custom case (also maybe)

## Programming:
you can program the board with my custom-made programming language bpf. (Ben Programming Format)
it is designed to be similar to [lua](https://www.lua.org/) and [python](https://www.python.org/).

### syntax:
* strings do not need quote marks around them.
* variables use the ~ prefix to indicate to swap the following value with a variable of that value.
* a table can be easily referenced as a variable then the index will be taken:
 * an index should be in square brackets.
 * a double-layered index can be taken ether with separate brackets around each, or in one set of brackets separated by commas (eg: `table[x, y][z]`.)
 * an index can be of any data type, including tables.
 * any index is evaluated the same way function parameters are.
* functions do not need any prefix, as functions are separate from variables.
* setting variables can be done only on a new line and can't be done inline.
* operators are:
 * +, -, \*, /, ^, and -^ for addition subtraction, multiplication, devision, power, and nth root.
 * %, and @ for modulo, and log root x of y
 * =, ==, >, <, <=, and >= for equal, reference equal, grater than, less than, grater than or equal, less than or equal (inverted forms have an exclamation point prepended.)
 * &, |, ^|, !&, !|, and !^ for and, or, xor, and their inverted forms
 * word operators are never allowed.

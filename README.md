# PostfixCalculator

This is a Postfix Calculator designed using Python 3.6.

An arithmetic expression is said to be in postfix notation if operators appear after the operands for example, ab+ mean a+b, ab∗ mean a∗b, abc+∗d− means a∗(b+c)−d, etc.

You may try it out for yourself at https://www.mathblog.dk/tools/infix-postfix-converter/

The code uses arguments from the command line. If one is not provided, the program will ask for the input.

An example is postfix_eval("9 20 * 12 + 7 -") = 185

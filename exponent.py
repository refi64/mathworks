"""
This work is licensed under the Creative Commons
Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or
send a letter to Creative Commons,
444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
"""
"""
exponent.py can square, cube, and the like numbers.
Example:
>>> import mathworks as mw
>>> mw.exponent.calc(4, 6)
4096
calc raises the first argument to the power of the second
argument.
square and cube are easier; just hand it the number to square/cube.
"""
def square(base):
    result = base * base
    return result
def cube(base):
    result = base * base * base
    return result
def calc(base, power):
    newbase = base
    i = 1
    while i < power:
        newbase = newbase * base
        i = i + 1
    return newbase

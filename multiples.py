"""
This work is licensed under the Creative Commons
Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or
send a letter to Creative Commons,
444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
"""
""" This module just returns a list of a number's multiples
Example:
>>> import mathworks as mw
>>> mw.getMuliples(4, 7)
This gets 4's first 7 multiples.
"""
def getMultiples(number, count):
    counter = 0
    multiples = 0
    result = []
    total = count
    while multiples < total:
        counter +=  1
        if counter % number != 0:
            continue
        multiples += 1
        result.append(counter)
    return result

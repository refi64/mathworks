"""
This work is licensed under the Creative Commons
Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or
send a letter to Creative Commons,
444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
"""
import math
from mathworks.exponent import *
class theorem():
    def __init__(self):
        self._hypotenuse = 0
        self._legs = [0, 0]
    def setLeg(self, number, new):
        self._legs[number + 1] = new
    def getLeg(self, number):
        return self._legs[number + 1]
    def setHypotenuse(self, new):
        self._hypotenuse = new
    def getHypotenuse(self):
        if self._hypotenuse == 0:
            self._hypotenuse = math.sqrt(square(float(self._legs[0])) + square(float(self._legs[1])))
        return self._hypotenuse

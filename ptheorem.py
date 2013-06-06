"""
Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
import math
from mathworks.exponent import square
class theorem():
    def __init__(self):
        self._hypotenuse = 0
        self._legs = [0, 0]
    def setLeg(self, number, new):
        num = number - 1
        self._legs[num] = float(new)
    def getLeg(self, number):
        if self._leg[number - 1] == 0:
            if number == 1:
                self._leg[0] = float(math.sqrt(square(self._hypotenuse) - square(self._legs[1])))
            if number == 2:
                self._leg[1] = float(math.sqrt(square(self._hypotenuse) - square(self._legs[0])))
            num = number - 1
        return self._legs[num]
    def setHypotenuse(self, new):
        self._hypotenuse = new
    def getHypotenuse(self):
        if self._hypotenuse == 0:
            self._hypotenuse = math.sqrt(square(float(self._legs[0])) + square(float(self._legs[1])))
        return self._hypotenuse

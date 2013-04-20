"""
This work is licensed under the Creative Commons
Attribution-ShareAlike 3.0 Unported License.
To view a copy of this license, visit
http://creativecommons.org/licenses/by-sa/3.0/ or
send a letter to Creative Commons,
444 Castro Street, Suite 900, Mountain View, California, 94041, USA.
"""
"""
I don't have the time right now to give examples
for this very large module(or at least in comparison
to the others). Please bear with me.
"""
class square:
    def __init__(self):
        self._length = 0
        self._perimeter = 0
        self._area = 0
    def setLength(self, length):
        self._length = float(length)
        self._perimeter = 0
        self._area = 0
    def getLength(self):
        return self._length
    def getPerimeter(self):
        if self._perimeter == 0:
            self._perimeter = float(self._length * 4)
        return self._perimeter
    def getArea(self):
        if self._area == 0:
            self._area = float(self._length * self._length)
        return self._area
class rectangle:
    def __init__(self):
        self._length = 0
        self._width = 0
        self._perimeter = 0
        self._area = 0
    def setLength(self, length):
        self._length = float(length)
        self._perimeter = 0
        self._area = 0
    def getLength(self):
        return self._length
    def setWidth(self, width):
        self._width = float(width)
        self._perimeter = 0
        self._area = 0
    def getWidth(self):
        return self._width
    def getPerimeter(self):
        if self._perimeter == 0:
            perim1 = float(self._length * 2)
            perim2 = float(self._width * 2)
            self._perimeter = float(perim1 + perim2)
        return self._perimeter
    def getArea(self):
        if self._area == 0:
            self._area = float(self._length * self._width)
        return self._area
class circle:
    def __init__(self):
        try:
            import math
            self._pi = math.pi
        else:
            self._pi = 3.14159265
        self._radius = 0
        self._diameter = 0
        self._circumference = 0
        self._area = 0
    def setRadius(self, radius):
        self._radius = float(radius)
        self._diameter = float(self._radius * 2)
        self._circumference = 0
        self._area = 0
    def setDiameter(self, diameter):
        self._diameter = float(diameter)
        self._radius = float(self._diameter / 2)
        self._circumference = 0
        self._area = 0
    def getRadius(self):
        return self._radius
    def getDiameter(self):
        return self._diameter
    def getPi(self):
        return self._pi
    def getCircumference(self):
        if self._circumference == 0:
            self._circumference = float(self._diameter * self._pi)
        return self._circumference
    def getArea(self):
        if self._area == 0:
            self._area = float(self._pi * (self._radius * self._radius))
class triangle:
    # The triangle is by far the most complex shape here.
    def __init__(self):
        self._side = [0, 0, 0, 0]
        self._angle = [0, 0, 0, 0]
        self._perimeter = 0
        self._area = 0
    def setSide(self, side, length):
        self._side[side] = float(length)
    def getSide(self, side):
        return self._side[side]
    def getPerimeter(self):
        if self._perimeter == 0:
            self._perimeter = self._side[1] + self._side[2] + self._side[3]
        return self._perimeter
    def setAngle(self, angle, measure):
        self._angle[angle] = float(measure)
    def getAngle(self, angle):
        if self._angle[angle] == 0:
            if angle == 1:
                angle1 = self._angle[2]
                angle2 = self._angle[3]
            elif angle == 2:
                angle1 = self._angle[1]
                angle2 = self._angle[3]
            elif angle == 3:
                angle1 = self._angle[1]
                angle2 = self._angle[2]
            anglet = angle1 + angle2
            angler = float(180) - anglet
            self._angle[angle] = angler
        return self._angle[angle]

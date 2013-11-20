#!/usr/bin/env python
from mathworks import shapes, exponent, multiples, ptheorem
import unittest, math

class TestModules(unittest.TestCase):
    def test_square(self):
        sq = shapes.square()
        sq.setLength(5)
        self.assertEquals(sq.getPerimeter(), 20)
        self.assertEquals(sq.getArea(), 25)
    def test_rect(self):
        rect = shapes.rectangle()
        rect.setLength(5)
        rect.setWidth(7)
        self.assertEquals(rect.getPerimeter(), 24)
        self.assertEquals(rect.getArea(), 35)
    def test_exponent(self):
        self.assertEquals(exponent.calc(5, 7), math.pow(5, 7))
        self.assertEquals(exponent.calc(-5, 7), math.pow(-5, 7))
        self.assertEquals(exponent.square(17), 17*17)
        self.assertEquals(exponent.cube(17), 17*17*17)
    def test_multiples(self):
        self.assertEquals(multiples.getMultiples(15, 20), [15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300])
    def test_theorem(self):
        tri = ptheorem.theorem()
        tri.setLeg(1, 4)
        tri.setLeg(2, 7)
        self.assertEquals(tri.getHypotenuse(), math.sqrt(4*4+7*7))

if __name__ == '__main__':
    unittest.main()


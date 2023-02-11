# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation
@author: jrr
@author: rk
"""

import unittest

def my_brand(assignmentName):
    myName = "=*=*=*= Ajay Kundu =*=*=*="
    course = "=*=*=*= Course 2023S-SSW567-WS =*=*=*="
    assignmentName = "=*=*=*= "+ assignmentName +" =*=*=*="
    dateTime = "=*=*=*= "+ str(datetime.datetime.now()) +" =*=*=*="
    print(myName + "\n" + course + "\n" + assignmentName + "\n" + dateTime)
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*"+"\n")
assignmentName = "HW 02-Testing a legacy program and reporting on testing results"
my_brand(assignmentName)

def classifyTriangle(a, b, c):
    if a == b and b == c:
        return 'Equilateral'
    elif a == b or b == c or a == c:
        return 'Isosceles'
    elif a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == b ** 2 + a ** 2:
        return 'Right'
    elif a != b and b != c:
        return 'Scalene'
    # require that the input values be >= 0 and <= 200
    elif a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    elif a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    elif not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'

    # This information was not in the requirements spec but
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a - b)):
        return 'NotATriangle'



def runClassifyTriange(a, b, c):
    print(classifyTriangle(a, b, c))


class TestTriangle(unittest.TestCase):

    def testSet1(self):
        self.assertEqual(classifyTriangle(10, 10, 10), 'Equilateral')

    def testSet2(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')

    def testSet3(self):
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right')

    def testSet4(self):
        self.assertEqual(classifyTriangle(7, 8, 9), 'Scalene')

    def testSet5(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')

    def testSet6(self):
        self.assertEqual(classifyTriangle(20, 20, 20), 'Equilateral')

    def testSet7(self):
        self.assertEqual(classifyTriangle(4, 2, 4), 'Isosceles')

    def testSet8(self):
        self.assertEqual(classifyTriangle(11, 15, 18), 'Scalene')

    def testSet9(self):
        self.assertEqual(classifyTriangle(9, 40, 41), 'Right')

    def testSet10(self):
        self.assertEqual(classifyTriangle(9, 10, 12), 'Scalene')

    def testSet11(self):
        self.assertEqual(classifyTriangle(6, 7, 8), 'Scalene')

    def testSet12(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def testSet13(self):
        self.assertEqual(classifyTriangle(12, 5, 13), 'Right')

    def testSet14(self):
        self.assertEqual(classifyTriangle(1, 3, 3), 'Isosceles')


if __name__ == '__main__':
    unittest.main()
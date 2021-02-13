import unittest
import Assignment.primesInRange as primesInRange
from pickle import NONE

class PrimeInRangeTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

# Sample happy path test
    def test100_100_ShouldDeterminePrimesInNominalRange(self):
        lowBound = 2
        highBound = 10
        expectedResult = [2, 3, 5, 7]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
# Test when the Low Bound is greater than the High Bound
    def test_LowBound_GT_HighBound(self):
        lowBound = 10
        highBound = 5
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
# Testing bounds that are negative
    def test_BoundasNegative(self):
        lowBound = -3
        highBound = 1
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
   
# Testing bounds that are both zero     
    def test_BoundsToZero(self):
        lowBound = 0
        highBound = 0
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
# Test bounds containing no prime numbers
    def test_NoPrimeNumbers(self):
        lowBound = 1000
        highBound = 1004
        expectedResult = []
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
        
#Test bounds that are not integers
    def test_IntegerInputs(self):
        lowBound = 'a'
        highBound = 10
        expectedResult = None
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertEqual(expectedResult, actualResult)
        
# Test both bounds are the same prime number
    def test_SameBounds(self):
        lowBound = 11
        highBound = 11
        expectedResult = [11]
        actualResult = primesInRange.primesInRange(lowBound, highBound)
        self.assertListEqual(expectedResult, actualResult)
    
# Testing no parameters
    def test_NoInputs(self):
        expectedResult = None
        try:
            actualResult = primesInRange.primesInRange()
            self.assertListEqual(expectedResult, actualResult)
        except Exception as e:
            print("Exception:", e.__class__)
           
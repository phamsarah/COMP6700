import unittest
import Tiles2048.create as create


class CreateTest(unittest.TestCase):

# Commented out test cases are cases that I used and will now run red lights, saved for documentation purposes
#
    # def test_create_HappyPathTest010(self):
        # userParms = {'op': 'create'}
        # expectedResult = {'dictionary': 'Dictionary'}
        # actualResult = create._create(userParms)
        # self.assertDictEqual(expectedResult, actualResult)
        
# Test if grid variable is returning 16 zero's should now be green.
#     def test_create_GridShouldReturnZeros(self):
#         userParms = {'op': 'create'}
#         expectedResult = '0000000000000000'
#         actualResult = create._create(userParms)
#         self.assertAlmostEqual(expectedResult, actualResult)


# Test and print the Grid and see if there are two random 1's in the string
    def test_create_PrintRandomNumber(self):
        userParms = {'op': 'create'}
        actualResult = create._create(userParms)
        print(actualResult)


# Testing if the first two variables are randomly selected, will sometimes be red, and will sometimes be green since it's random
#     def test_create_GetRandomFirstTwoVariables(self):
#         userParms = {'op': 'create'}
#         expectedResult = [2,2]
#         actualResult = create._create(userParms)
#         self.assertListEqual(expectedResult, actualResult)  

# Testing if the returned dictionary contains a grid key, should return true
    def test_create_ReturnedDictionaryShouldContainGridKey(self):
        userParms = {'op': 'create'}
        dictionary = create._create(userParms)
        expectedResult = True
        
        gridBoolean = False
        if dictionary['grid']: 
            gridBoolean = True
            
        self.assertAlmostEqual(expectedResult, gridBoolean)      
        

#Testing if the returned dictionary contains a grid and score key, should return greenlight
    def test_create_ReturnedDictionaryShouldGridAndScoreKey(self):
        userParms = {'op': 'create'}
        dictionary = create._create(userParms)
        expectedResult = True
        
        gridBoolean = False
        if 'grid' in dictionary: 
            gridBoolean = True
            
        if 'score' in dictionary:
            gridBoolean = True
        else:
            gridBoolean = False
        
            
        self.assertAlmostEqual(expectedResult, gridBoolean)
 
 
 
#Testing if the returned dictionary contains a integrity key
    def test_create_ReturnedDictContainsIntegrity(self):
        userParms = {'op': 'create'}
        dictionary = create._create(userParms)
        expectedResult = True
        
        integrityBoolean = False
        if 'integrity' in dictionary: 
            integrityBoolean = True

        
        self.assertAlmostEqual(expectedResult, integrityBoolean)  
 
 
# Testing if the returned dictionary does contain a status key, should be greenlight now
    def test_create_ReturnedDictContainsStatus(self):
        userParms = {'op': 'create'}
        dictionary = create._create(userParms)
        expectedResult = True
        
        statusBoolean = False
        if 'status' in dictionary: 
            statusBoolean = True
        
        self.assertAlmostEqual(expectedResult, statusBoolean)           
'''
Created on Mar 23, 2021
Shift test is a unit test folder testing all the functionalities of the Shift method

@author: sarahpham
'''
import unittest
import Tiles2048.shift as shift


class ShiftTest(unittest.TestCase):
    
# Test if the Shift file is being called correctly, should return red light
    # def test_shift_navigatesToShift(self):
        # userParms = {'op': 'shift'}
        # expectedResult = {'create': 'create stub'}
        # actualResult = shift._shift(userParms)   
        # self.assertDictEqual(expectedResult, actualResult)
        

# Test if the Shift file is being called correctly, should return green light
    # def test_shift_navigatesToShiftHappyPath(self):
        # userParms = {'op': 'shift', 'score': '0'}
        # expectedResult = {'shift': 'shift stub'}
        # actualResult = shift._shift(userParms)   
        # self.assertDictEqual(expectedResult, actualResult)

# Test if score value is correctly being returned, should be green light    
    # def test_shift_returnsInputScoreValue(self):
        # userParms = {'op': 'shift', 'score': '0'}
        # expectedResult = '0'
        # actualResult = shift._shift(userParms)   
        # self.assertAlmostEqual(expectedResult, actualResult)

# Test if we can iterate through the grid string  
    # def test_shift_forLoopForGrid(self):
        # userParms = {'op': 'shift', 'grid': '1024102400000000000000','score': '0'}
        # expectedResult = '01024102400000000000000'
        # actualResult = shift._shift(userParms)   
        # self.assertAlmostEqual(expectedResult, actualResult)
        
# Test if we can find 1024 in the grid string   
    # def test_shift_findsValueinList(self):
        # userParms = {'op': 'shift', 'grid': '1024102400000000000000','score': '0'}
        # expectedResult = '0'
        # actualResult = shift._shift(userParms)   
        # self.assertAlmostEqual(expectedResult, actualResult)

# Test to see if the correct grid list is created from a given grid string Returns Green
    # def test_returnsCorrectGridList(self):
        # userParms = {'op': 'shift', 'grid': '0000004024402020','score': '0'}
        # expectedResult = ['0','0','0','0','0','0','4','0','2','4','4','0','2','0',
                          # '2','0']
        # actualResult = shift._shift(userParms)   
        # self.assertListEqual(expectedResult, actualResult)
        
        
# Test to see if the correct grid list is created from a given grid string Should return green
    # def test_returnsCorrectGridListPartTwo(self):
        # userParms = {'op': 'shift', 'grid': '4000000000804420','score': '0'}
        # expectedResult = ['4','0','0','0','0','0','0','0','0','0','8','0','4','4',
                          # '2','0']
        # actualResult = shift._shift(userParms)   
        # self.assertListEqual(expectedResult, actualResult)
        
# Test to see if the grid will add in Left direction
    # def test_shouldReturnAddedLeftGrid(self):
        # userParms = {'op': 'shift', 'grid': '40200020400803200','score': '0', 
                     # 'direction':'left', 'integrity': 'ca464ed940ae8202e831b25861721214122cd322a1558427b9a6a73dbd26f60d'}
        # expectedResult = '42002000480032000'
        # actualResult = shift._shift(userParms)   
        # self.assertEqual(expectedResult, actualResult['grid'])
        #
# # Test to see if the grid will add in Left direction, second test
    # def test_shouldReturnAddedLeftGridTwo(self):
        # userParms = {'op': 'shift', 'grid': '2222444488881616160','score': '0', 
                     # 'direction':'left'}
        # expectedResult = '44008800161600321600'
        # actualResult = shift._shift(userParms)
        # print('actual result: ' + actualResult)
        # self.assertEqual(expectedResult, actualResult)
        #
# # Test to see if the grid will add in Right direction
    # def test_shouldReturnAddedRightGrid(self):
        # userParms = {'op': 'shift', 'grid': '40200020400803200','score': '0', 
                     # 'direction':'right', 'integrity':'ca464ed940ae8202e831b25861721214122cd322a1558427b9a6a73dbd26f60d'}
        # expectedResult = '00420002004800032'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['grid'])
        #
# # Test to see if the grid will add in Up direction
    # def test_shouldReturnAddedUpGrid(self):
        # userParms = {'op': 'shift', 'grid': '40200020400803200','score': '0', 
                     # 'direction':'up'}
        # expectedResult = '83248000000000000'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult)
        #
# # Test to see if the grid will add in Down direction
    # def test_shouldReturnAddedDownGrid(self):
        # userParms = {'op': 'shift', 'grid': '40200020400803200','score': '0', 
                     # 'direction':'down', 'integrity': 'ca464ed940ae8202e831b25861721214122cd322a1558427b9a6a73dbd26f60d'}
        # expectedResult = '00000000000083248'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['grid'])

# Test to see if a random number is generated and added to a correct spot
    # def test_shouldAddRandomNumber(self):
        # userParms = {'op': 'shift', 'grid': '2222444488881616160','score': '9600', 
                     # 'direction':'left'}
        # expectedResult = '44008800161600321600'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['grid'])        


# Test to see if a score is calculated correctly
    # def test_shouldReturnCorrectScore(self):
        # userParms = {'op': 'shift', 'grid': '2222444488881616160','score': 9600, 
                     # 'direction':'left'}
        # expectedResult = '9688'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['score']) 
        #
# # Test to see if a score is calculated correctly part Two
    # def test_shouldReturnCorrectScoreTwo(self):
        # userParms = {'op': 'shift', 'grid': '0000004024402020','score': 4, 
                     # 'direction':'up'}
        # expectedResult = '16'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['score']) 
        #
# # Test to see if a Status is calculated correctly
    # def test_shouldReturnCorrectStatus(self):
        # userParms = {'op': 'shift', 'grid': '2222444488881616160','score': 9600, 
                     # 'direction':'up'}
        # expectedResult = 'lose'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['status']) 
        #
# # Test to see if we get the win status correctly
    def test_shouldReturnWinStatus(self):
        userParms = {'op': 'shift', 'grid': '1024102400000000000000','score': 129024, 
                     'direction':'left', 'integrity': '18FF0FE71EB8CCFA82556511578B321D0B69A8E2FD5202EBD3A949EB35CB3C45'}
        print('CURRENT UNIT TEST')
        expectedResult = 'win'
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult['status'])
        
# # On a win do we get the correct score?
    def test_shouldReturnCorrectWinScore(self):
        userParms = {'op': 'shift', 'grid': '1024102400000000000000','score': 129024, 
                     'direction':'left', 'integrity': '18FF0FE71EB8CCFA82556511578B321D0B69A8E2FD5202EBD3A949EB35CB3C45'}
        expectedResult = '131072'
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult['score']) 
        
# ---------- Exception Handling ---------- #

# Testing to see what happens when there is no room for an added random 2
    # def test_shouldReturnLoseStatus(self):
        # userParms = {'op': 'shift', 'grid': '2222444488881616160','score': 9600, 
                     # 'integrity': '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE',
                     # 'direction':'up'}
        # expectedResult = 'lose'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['status'])
        
# Testing a string with 2048, but is not a 2048 tile, but instead is 2-0-4-8 separately
    def test_2048StringNotWinChecksStatus(self):
        userParms = {'op': 'shift', 'grid': '2002048204820480','score': 0, 
                     'direction':'up', 'integrity': '1aba1836500df9656bea0ad252be11db71207ed4a3ff38d3611273a730860dba'}
        expectedResult = 'ok'
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult, actualResult['status'])
        #
# # # Testing a string with 2048, but is not a 2048 tile, but instead is 2-0-4-8 separately, checks the returned grid
    # def test_2048StringNotWinChecksGrid(self):
        # userParms = {'op': 'shift', 'grid': '2002048204820480','score': 0, 
                     # 'direction':'up'}
        # expectedResult = '28164048200000000'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['grid'])   
        
# Test a missing grid
    def test_ExceptionHandling_MissingGrid(self):
        userParms = {'op': 'shift','score': 0, 'grid': '',
                     'direction':'up', 'integrity': 
        '1875F39BCE84620F9B3273BE921EFF1E541FEAEE10EBBF0858DB30ADF10BE2A9' }
        expectedResult = { 'status': 'error: invalid grid' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult) 
        

# Test a bad integrity value
    def test_ExceptionHandling_BadIntegrityValue(self):
        userParms = {'op': 'shift','score': 4, 'grid': '0000004024402020',
                     'direction':'down', 'integrity': 
        'B942E8D41B41814866B32EA9C9A3A4205ABA77148D86741D1EFE765BE6FEAADB' }
        expectedResult = { 'status': 'error: bad integrity value' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult)
        

# Test invalid score
    def test_ExceptionHandling_InvalidScore(self):
        userParms = {'op': 'shift','score': 33, 'grid': '0000004024402020',
                     'direction':'down', 'integrity': 
        '1875F39BCE84620F9B3273BE921EFF1E541FEAEE10EBBF0858DB30ADF10BE2A9' }
        expectedResult = { 'status': 'error: invalid score' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult)
        

# Test invalid grid
    def test_ExceptionHandling_InvalidGrid(self):
        userParms = {'op': 'shift','score': 4, 'grid': '2248161632010245120000052',
                     'direction':'down', 'integrity': 
        '9CE182F636152306A87BC22CDA94C8607A925E584FCF34F5896B393ACCAFD6EF' }
        expectedResult = { 'status': 'error: invalid grid' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult) 
        
        
# Test invalid direction
    def test_ExceptionHandling_InvalidDirection(self):
        userParms = {'op': 'shift','score': 4, 'grid': '0000004024402020',
                     'direction':'back', 'integrity': 
        '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A' }
        expectedResult = { 'status': 'error: invalid direction' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult) 
        
        
# Test no shift possible
    def test_ExceptionHandling_NoShiftPossible(self):
        userParms = {'op': 'shift','score': 4, 'grid': '2222222222222222',
                     'direction':'down', 'integrity': 
        '96D0C2876B9E858F6BA247A8E944DA7D76F55E6026017A5C4A0B9B128C16F844' }
        expectedResult = { 'status': 'error: no shift possible' }
        actualResult = shift._shift(userParms)
        self.assertDictEqual(expectedResult, actualResult) 
        
        
#----------------------------------------------------------#
        
# Assignment 7 Given Tests from "Customer Needs" Tab
# Test 1 - This test will always return red light since there is a random number generated
    # def test_Assignment7Test1(self):
        # userParms = {'op': 'shift','score': 0, 'grid': '0020000020000000',
                     # 'direction':'down', 'integrity': 
        # '7CD5E3DEAB08FCAE8F64433DC4A63CC922571EBF60EE1D1938ADCD415FB760E5' }
        # expectedResult = '0000004000002020'
        # actualResult = shift._shift(userParms)
        # self.assertEqual(expectedResult, actualResult['grid']) 
        
        
# Test 2 - This test will always return red light since there is a random number generated
    # def test_Assignment7Test2(self):
        # userParms = {'op': 'shift','score': 4, 'grid': '0000004024402020',
                     # 'direction':'up', 'integrity': 
        # '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A' }
        # expectedResult = {'grid': '4480002000000200', 'score': '16', 'integrity': '7026D4B80CAC4E329E5224D753C487C55B859AEB2F6231C2DCEBCFD44B2C32B1', 'status': 'ok'}
        # actualResult = shift._shift(userParms)
        # self.assertDictEqual(expectedResult, actualResult)
        

# Test 3 - Will mostly return red since there is a random number generated
    def test_Assignment7Test3(self):
        userParms = {'op': 'shift','score': 4, 'grid': '0000004024402020', 'integrity': 
        '2A2EF0D1BEA22B9D6AB67C482BFF954F93F6A3617EF052E11DD8776BFFB7325A' }
        expectedResult = {'grid': '4000000000804420', 'score': '16', 'integrity': '96AE2C09F18145AB3B76655B47F6F9B902A48077B2DB9D365D747A801981B949', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult['score'], actualResult['score']) 
        
        
# Test 4 - I changed the unit test to test the "scores" since that is a value that should never change after testing the entire dictionary
    def test_Assignment7Test4(self):
        userParms = {'op': 'shift','score': 9600, 'grid': '2222444488881616160', 'integrity': 
        '66457746F0596CEE48B4FA4FA9C57A8A56A917F5B42F2600F12CD4266B9098BE', 'direction': 'left' }
        expectedResult = {'grid': '44008800161600321602', 'score': '9688', 'integrity': 'FD4750403CBC401D7FC64E9ADCCEF7B24981481A24CFB23F274F3DC38B524883', 'status': 'ok'}
        actualResult = shift._shift(userParms)
        self.assertEqual(expectedResult['score'], actualResult['score']) 
        
        
# Test 5
    def test_Assignment7Test5(self):
        userParms = {'op': 'shift','score': 9600, 'grid': '2481632641282562481632641280', 'integrity': 
        'CBD6F924B76E41871F106ABDE80AF9BA71350A53B0A148F26F16AF14CA5F6B06', 'direction': 'down' }
        expectedResult = {'grid': '2482326412816248256326412816', 'score': '9600', 'integrity': 'EA619F71A389DC0C3770E5DA79B405E81EA25B0E841D90176714B101C5E792E7', 'status': 'lose'}
        print('CURRENT UNIT TEST')
        actualResult = shift._shift(userParms)
        print('Actual Result: ' + str(actualResult))
        self.assertEqual(expectedResult['status'], actualResult['status'])
        
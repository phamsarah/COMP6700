import unittest
import Tiles2048.info as info


class InfoTest(unittest.TestCase):

    def test100_010_ShouldReturnMyUserName(self):
        expectedResult = {'user': 'slp0042'}
        userParms = {'op': 'info'}
        actualResult = info._info(userParms)
        self.assertDictEqual(expectedResult, actualResult)
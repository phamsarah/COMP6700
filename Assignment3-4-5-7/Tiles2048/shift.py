'''
    Created on Mar 23, 2021
    
    Shift folder will take the inputs: grid, score, integrity, and direction
    and validate each parameter and return a dictionary of the moved grid
    or of a status if there is an error.

    @author:  Sarah Pham
'''

import Tiles2048.create as create
import random

# Global variable score
score = 0
status = ''
integrity = ''
gridString = ''
methodStatus = ''

# Main shift function that handles moving the 2048 grid
def _shift(userParms):
    global score
    global integrity
    global status
    global gridString
    global methodStatus 
    
    methodStatus = 'shift'
    
    tempGrid = ''
    
    gridString = userParms.get('grid')
    score = int(userParms.get('score'))
    direction = str(userParms.get('direction'))
    integrity = str(userParms.get('integrity'))
    
    status = _validateInputParameters(gridString, score, direction)
    
    # If there is no direction, the default is down
    if status == 'direction':
        direction = 'down'
        status = 'ok'
    elif status != 'ok':
        return _errorReturnStatus(status)

    gridList = _createGridList(gridString)
    
    if gridList == 0:
        return _errorReturnStatus('error: invalid grid')
    elif isinstance(gridList, str):
        return _errorReturnStatus(gridList)
    else:
        tempGrid = ''.join([str(a) for a in gridList])
    
    # We need to validate the given Integrity from the given user parameters
    unvalidatedIntegrity = create._encrypt(tempGrid + '.' + str(score))
    
    status = _validateIntegrity(unvalidatedIntegrity)
    
    if status != 'ok':
        return _errorReturnStatus(status)
    else:
        integrity = unvalidatedIntegrity
    
    
    movedGridList = _moveTile(gridList, direction)
    status = _checkStatus(movedGridList)

    
    integrity = create._encrypt(gridString + '.' + str(score))
    
    
    result = { 'grid': gridString, 'score': str(score), 'integrity': integrity, 'status': status }

    return result


def _errorReturnStatus(error):
    global status
    status = error
    invalidInput = { 'status': status }
    return invalidInput


# This function validates the input parameters 
def _validateInputParameters(grid, score, direction):
    validDirections = ['left', 'right', 'up', 'down']
    checkScore = (score % 2) == 0
    
    if grid is None:
        failedVariable = 'missing grid'
    elif (len(grid) < 16):
        failedVariable = 'invalid grid'
    elif score is None or (score < 0) or checkScore is False:
        failedVariable = 'invalid score'
    elif direction == 'None':
        return 'direction'         
    elif (direction.lower() not in validDirections):
        failedVariable = 'invalid direction'     
    else:
        return 'ok'
    
    return 'error: ' + failedVariable


# This function validates the given integrity value, will check this after the
#    grid input is check as valid
def _validateIntegrity(unvalidatedIntegrity):
    
    if integrity is None or (unvalidatedIntegrity != integrity.upper()):
        return 'error: bad integrity value'
    else:
        return 'ok'



# This function calls the function that will move the tile in terms of direction
#    sends the direction column
def _moveTile(grid, direction):
    # If 'up', then we look at the 0-3 index spaces, each space will look down at their
    #    column for similar numbers, if similar then add
    
    if direction == 'left':
        left = [0, 4, 8, 12]
        return _moveInDirection(grid, left, direction)
    elif direction == 'right':
        right = [3, 7, 11, 15]
        return _moveInDirection(grid, right, direction)
    elif direction == 'up':
        up = [0, 1, 2, 3]
        return _moveInDirection(grid, up, direction)
    elif direction == 'down':
        down = [12, 13, 14, 15]
        return _moveInDirection(grid, down, direction)
    else:
        return None
    
    
def _moveInDirection(grid, directionIndexes, direction):

    global score
    global status
    global gridString

    i = 0
    j = 0
    k = 0
    addedGridList = [0] * 16
    
    # We use a integer list so that we can add the values together
    tempGrid = []
    
    # First loop covers the beginning of each row, in the case of the 
    #    left direction, it would be the indexes containing [0,4,8,12]
    while j < len(directionIndexes):
        if direction == 'left':
            tempGrid = [int(grid[directionIndexes[j]]), int(grid[directionIndexes[j] + 1]), int(grid[directionIndexes[j] + 2]), int(grid[directionIndexes[j] + 3])]
        elif direction == 'right':
            tempGrid = [int(grid[directionIndexes[j]]), int(grid[directionIndexes[j] - 1]), int(grid[directionIndexes[j] - 2]), int(grid[directionIndexes[j] - 3])]
        elif direction == 'up':
            tempGrid = [int(grid[directionIndexes[j]]), int(grid[directionIndexes[j] + 4]), int(grid[directionIndexes[j] + 8]), int(grid[directionIndexes[j] + 12])]
        else:
            tempGrid = [int(grid[directionIndexes[j]]), int(grid[directionIndexes[j] - 4]), int(grid[directionIndexes[j] - 8]), int(grid[directionIndexes[j] - 12])]
            
        # Fist we remove all occurrences of Zero in the list
        #    this will make our calculations easier.
        tempGrid = [i for i in tempGrid if i != 0]
        
        # Second loop covers each column in each row, for the first row, it would be 
        #    [0,1,2,3], second row would be (from left to right), starting at 
        #    index 4 and adding indexes [4,5,6,7]
        while i < len(tempGrid) - 1:
            squareOne = tempGrid[i]
            squareTwo = tempGrid[i+1]
            
        # If first and second square are the same we add.
        #     Then we remove the second square
            if squareOne == squareTwo:
                squareOne = squareOne + squareTwo
                if methodStatus == 'shift':
                    score = score + squareOne
                tempGrid[i] = squareOne
                tempGrid.pop(i+1)

                
        # We move the first square to the next space whether or not we combined squares
            i = i + 1

        a = directionIndexes[j]
        while k < 4:
            if 0 <= k < len(tempGrid):
                addedGridList[a] = tempGrid[k]
            else:
                addedGridList[a] = 0
            k = k + 1
            if direction == 'left':
                a = a + 1
            elif direction == 'right':
                a = a - 1
            elif direction == 'up':
                a = a + 4
            else:
                a = a - 4

        
        k = 0
        i = 0
        j = j + 1
        
    # We add the random 2 in any zero located in a grid list
    randomAdded = _addRandomTwoOrFour(addedGridList)
    gridString = ''.join([str(a) for a in randomAdded])

    return gridString


# This function checks if the grid can be shifted again
# Compares the grid with other shifted grids, if 
def _canBeShiftedAgain():
    tempGrid = _createGridList(gridString)

    leftShift = _moveTile(tempGrid, 'left')
    if gridString != leftShift:
        return True
    elif gridString != _moveTile(tempGrid, 'right'):
        return True
    elif gridString != _moveTile(tempGrid, 'up'):
        return True
    elif gridString != _moveTile(tempGrid, 'down'):
        return True

    return False
    
    


# This function will check the 'status' of any given list
#    'ok' -> Grid can be shifted once and no 2048
#    'win' -> Tile has 2048 value
#    'lose' -> Cannot be shifted, all values less than 2048
# 
# Parameters: gridList - list of moved grid
#             movedGridString - string of moved grid
#             gridString - global parameter of the user parameter


def _checkStatus(gridList):
    global methodStatus
    methodStatus = 'checkStatus'
    
    
    if '2048' in gridList:
        return 'win'
    elif (_canBeShiftedAgain() is True) and ('2048' not in gridList):
        return 'ok'
    elif (_canBeShiftedAgain() is False) and ('2048' not in gridList):
        return 'lose'
    else:
        return None



# This function will add a random 2 or 4. We do this by randomly picking an index
#    within the list length and check if there is a zero there. If there is
#    a zero then replace that value with 2 or 4, else randomly pick another index and so on.

def _addRandomTwoOrFour(grid):
    highBound = len(grid) - 1
    randomList = [2,4]
    randomAdded = False
    i = 0

    if 0 in grid:
        while randomAdded == False:
            randomNumIndex = random.randint(0,highBound)
            if grid[randomNumIndex] == 0 or grid[randomNumIndex] == '0':
                grid[randomNumIndex] = random.choice(randomList)
                randomAdded = True
                i = i + 1
    
    return grid


# Converts the given grid string into a list format, since the index of the string
#    does not represent the index/individual tile number, so this will be a little tricky

def _createGridList(grid):
    tile = []

# We loop through the string in increments of 4, comparing the string to
#     the list of valid numbers in digits of 4's and so forth.
    tileLength = 16
    j = 4
    i = 0
    k = len(grid)
    endOfString = False
    added = False
    validNum = 1
    
    while i < len(grid) and j >= 0 and validNum != 0:

        # This if statement checks if we have reached the end of the string
        # If we have, then only look at the last bit of the string
        if(i + 4) > len(grid):
            endOfString = True
            if added == False:
                tempTile = grid[i:k]
            else:
                tempTile = grid[i:]

        # If we have not reached the eos, then keep incrementing by 4
        else:
            tempTile = grid[i:i+j]
            
        validNum = _findNumber(tempTile)
        
        # If the given string we are looking at is valid, then add it to the grid/tile list
        # Reset J to 4, since we have found a match and increment i by the number of digits of the valid number
        # If we are looking at the end of the string, reset the k to the length of the grid, otherwise decrement
        if validNum is not None:
            tile.append(tempTile)     
            i = i + validNum
            j = 4
            if endOfString == True:
                added = True
                k = len(grid)
                
        elif validNum == 0:
            return validNum
        
        # If invalid, then decrement J or K and revalidate
        else:
            j = j - 1
            if endOfString == True:
                added = False
                k = k - 1
    
    if '2048' in tile and (len(tile) < tileLength):
        tile = _validate2048(tile)

    if validNum == 0:
        return validNum
    elif '0' not in tile and methodStatus == 'shift':
        return 'error: no shift possible'
        
    return tile



# This function validates a '2048'. In some cases, there may be a 2048 that is not
#    actually a 2048 but a separate 2-0-4-8, we check with the length of the tile and
#    separate the 2048
def _validate2048(gridList):
    
    twentyFourEight = '2048'
    occurrences = gridList.count('2048')
    countOccurrences = 0
        
    while countOccurrences < occurrences:
        indexOf2048 = gridList.index('2048')
        gridList.pop(indexOf2048)
        counter = 0
        while counter < len(twentyFourEight):
            gridList.insert(indexOf2048, twentyFourEight[counter])
            counter = counter + 1
            indexOf2048 = indexOf2048 + 1
        countOccurrences = countOccurrences + 1
            
    return gridList
    
        
    
    
# Checks if given string is a valid 2048 number. Returns the number of digits
#    of the valid number, so we know which index of i to look at next. If it is an invalid
#    number then keep decrementing the right side until we find a valid number
def _findNumber(checkString):
    fourDigits = ['1024', '2048']
    threeDigits = ['128', '256', '512']
    twoDigits = ['16', '32', '64']
    oneDigit = ['0','2', '4', '8']
    
    
    if len(checkString) == 4 and any(element in checkString for element in fourDigits):
        return 4
    
    elif len(checkString) == 3 and any(element in checkString for element in threeDigits):     
        return 3
        
    elif len(checkString) == 2 and any(element in checkString for element in twoDigits):     
        return 2
        
    elif len(checkString) == 1 and any(element in checkString for element in oneDigit):     
        return 1
    
    elif len(checkString) == 1 and (checkString not in oneDigit):
        return 0
    
    else:
        return None

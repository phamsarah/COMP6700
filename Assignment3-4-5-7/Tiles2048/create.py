'''
    Created on Mar 23, 2021


    @author:  Sarah Pham
'''

import random
import hashlib

def _create(userParms): 
    
# Creation of empty 16 tile grid
    grid = '0000000000000000'
    
# We generate two random, unique, index numbers from 0 to 15 
    randomNumIndex = list(random.sample(range(0,16), 2))

# Randomly placing 2's by using random index values
    grid = grid[:randomNumIndex[0]] + '2' + grid[randomNumIndex[0] + 1:]
    grid = grid[:randomNumIndex[1]] + '2' + grid[randomNumIndex[1] + 1:]
    
# Concatenate score to grid, score is initially zero when we create the grid
    grid = grid + '.0'
    
    
# Send grid string to be encrypted in sha256
    integrity = _encrypt(grid)
    
# Add all necessary values to the dictionary
    dictionary = { 'grid': grid, 'score': 0, 'integrity': integrity, 'status': 'ok' }
    print(dictionary)
        
    return dictionary


def _encrypt(grid):
    
    encryption = hashlib.sha256(grid.encode()).hexdigest()
    
    return encryption.upper()
    
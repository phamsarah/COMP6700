def primesInRange(lowerBound, upperBound):  
    
    prime = []
    
    if type(lowerBound) != int or type(upperBound) != int:
        return None
    if lowerBound >= 0 and upperBound > 0 and lowerBound <= upperBound:
        for i in range(lowerBound, upperBound + 1):
            for j in range(2, i):
                if i % j == 0:
                    break;
            else:
                prime.append(i)
    else:
        return None;
    
    return prime
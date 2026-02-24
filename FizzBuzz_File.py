def FizzBuzz(start, finish):
    outlist = []
    
    for value in range(start, finish + 1):  # inclusive range
        
        if value % 15 == 0:
            outlist.append("fizzbuzz")
        elif value % 3 == 0:
            outlist.append("fizz")
        elif value % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(value)
    
    return outlist

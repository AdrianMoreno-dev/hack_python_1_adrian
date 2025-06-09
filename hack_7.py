"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = [] 
    i = 0 
    while i < 6:
        result.append(i)
        i += 1 
    result.reverse()
    return result


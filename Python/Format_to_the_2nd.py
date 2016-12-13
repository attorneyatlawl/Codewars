'''Given some positive integers, I wish to print the integers such that all take up the same width by adding a minimum number of leading zeroes. 
No leading zeroes shall be added to the largest integer.

For example, given 1, 23, 2, 17, 102, the following string should be printed out:

001
023
002
017
102
'''

def print_nums(*arr):
    if not arr: return ''
    ln = len(str(max(arr)))
    return '\n'.join(str(c).zfill(ln) for c in arr)

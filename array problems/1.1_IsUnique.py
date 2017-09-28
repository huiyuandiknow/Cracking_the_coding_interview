# Is Unique: implement an algorithm to determine if
# a string has all unique characters. What if you
# cannot use additional data structures? 

import sys

def IsUnique(s):
    for i in s:
        if s.count(i) > 1: return False
    return True
            

if __name__ == '__main__':
    input = sys.stdin.readline()
    #data = int(input)
    print(IsUnique(input))
    

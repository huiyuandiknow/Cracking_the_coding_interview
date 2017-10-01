# Check Permutation: Given two strings, write a method
# to decide if one is a permutation of the other

import sys

def perm(s1, s2):
    if len(s1) != len(s2):
        return False
    
    for i in s1:
        if s1.count(i) != s2.count(i):
            return False
    return True

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(input.strip().split(' '))
    print(perm(data[0], data[1]))
    

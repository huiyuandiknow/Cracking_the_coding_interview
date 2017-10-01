# Palindrome Permutation: Given a string, write a function to check if
# it is a permutation of a palindrome. A palindrome is a word or phrase
# that is the same forwards and backwards. A permutation is a rearrangement
# of letters. The palindrome does not need to be limited to just dictionary
# words. 

import sys

def permPalindrome(st):
    # remove space
    s = st.replace(' ', '').strip()
    s = s.lower()
    if len(s) % 2 == 0:
        for i in s:
            if s.count(i) % 2 != 0:
                return False
        return True
    else:
        length= []
        for i in s:
            if s.count(i) % 2 == 0:
                length.append(0)
            else:
                length.append(1)
        if sum(length) != 1:
            return False
        else:
            return True

if __name__ == '__main__':
    input = sys.stdin.readline()
    print(permPalindrome(input))
    

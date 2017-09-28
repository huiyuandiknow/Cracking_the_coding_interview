# URLify: Write a method to replace all string with '%20'. You may
# assume that the string has sufficient space at the end to hold the
# additional characters, and that you are given the "true" length of
# the string. 

import sys

def URLify(s, n):
    s = s.strip()
    l = list(s.split(' '))
    k = ''
    num_blank = n - len(l)
    for i in l:
        if num_blank > 0: 
            k+= i + '%20'
            num_blank -= 1
        else:
            k+= i
    return k

if __name__ == '__main__':
    input = sys.stdin.readline()
    data = list(input.split(','))
    s = data[0][1:]
    index = s.index('"')
    s = s[:index].strip()
    n = int(data[1].strip())
    print(URLify(s, n))
    

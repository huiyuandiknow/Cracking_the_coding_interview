# Given a string s, find and return the first instance of a non-repeating
# char in it. If there is no such char, return '_'. 

def firstNotRepeatingCharacter(s):
    seen = set(); ignore_list = []
    for i in s:         
        if i in seen: 
            ignore_list.append(i)
        else: 
            seen.add(i)
    for i in s: 
        if i not in ignore_list: 
            return i
    return '_'

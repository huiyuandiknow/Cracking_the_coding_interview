# given an array a that contains only numbers in the range from 1 to
# a.length, find the first duplicate number for which the second occurrence
# has the minimal index. 

def firstDuplicate(a):
    seen=set()
    for el in a:
        if el in seen:
            return el
        seen.add(el)
    return -1

# Given a singly linked list of integers l and an integer k,
# remove all elements from list l that have a value equal to k.

def removeKFromList(l, k):
    begin = l 
    head = True
    
    # check first node
    if l is not None:
        while l is not None and l.value == k: 
            l = l.next 
        begin = l 
        
        if l is not None and l.value != k:         
            while l.next is not None:
                if l.next.value == k:
                    l.next = l.next.next
                else:
                    l = l.next     
    return begin


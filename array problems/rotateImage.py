# Given a n x n 2D matrix that represents an image. Rotate the image
# by 90 degree clockwise. 

def rotateImage(a):
    overall = []
    
    for i in range(len(a)): 
        current = []
        n = len(a)
        while n!= 0:
            current.append(a[n-1][i])
            n-= 1
        overall.append(current)
    return overall

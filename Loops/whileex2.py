### Make two lists such that A = [positive number only, include 0 ] , B = [negative numbers only ]

L = [0, 1, 2, -10, 90, 98, -203, -12]
A= []
B =[]
i = 0
while i < len (L):
    if L [i] >= 0 :
        A.append(L[i])
    else:
        B.append (L[i])
    i += 1
print ("A is : " , A )
print ("B is : " , B)
### I will learn how to use while loop to iterate 
# 
# through list and apply condition to
#  separate positive and negative numbers 
# into two different lists.  
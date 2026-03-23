### Filtering even numbers from a list using while loop.

L = [ 10 , -3, 8 , 7 , 25 , 30 , 35]
E = []
i = 0 
while i< len (L):
    if L[ i] %2 == 0:
        E.append(L[i])
    i+=1
print (E)

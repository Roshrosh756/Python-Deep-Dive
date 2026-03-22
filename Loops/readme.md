Loops in python -> Iterative Programming 

1. WHILE LOOP
    a = 5
    n =1
    while n < a: 
        print (f"n is {n}")
        n+=1
    
    output :n is 1
            n is 2
            n is 3
            n is 4


2. learning append

n= int(input ("enter number upto which multiple of 3 or 5 is to be found "))
L = []
a = 1
while (a <= n):
    if a % 3 == 0 or a % 5 == 0:
        L.append (a)
    a +=1
print (f"list of multiples of 3 or 5 upto {n} is {L} " )

output : 
enter number upto which multiple of 3 or 5 is to be found  27
list of multiples of 3 or 5 upto 27 is [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27]




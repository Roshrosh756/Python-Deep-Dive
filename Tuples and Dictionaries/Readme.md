## Let's compare List vs Tuples
## LIST

<!-- 1. list is collection of homogeneous or heterogeneous element. 

2. [ ... , ... ,]
    A= [1, 12, 20, 40] -                   homogeneous
    B= [10, True, 'element' , [5,6]] --> - heterogeneous 

<!-- 3. Two main properties:
    - Elements in lists are always ordered. 
        A =[ 10, 20, 15 , -10, 24]
            0    1    2    3    4      #indexed --> positice index
            -5   -4   -3  -2   -1            negative index


<!-- L =[ 10 , 20 , -10 , 25, 50 , 75 ]
print (L[2])
print (L[-1])
print (len (L))
print (L[2:5])     this is called slicing.   L[inclusive : exclusive ]

output :-10
        75
        6
        [-10, 25, 50] -->

Again one example: use cases of slicing
L = [2 , -3 , 10 , 7 , 14 , 25 , 8 , 92, 87 ]
print (L[3:7])
print (L[:4])                   [start:stop:step]
print (L[5:])                   [start:stop] - default step 1
print (L[1:7:2])                [start::step] - no stopping array
print (L[2::2])
print (L[::1])
print (L[-2: -7 :-1])
print (L[-7 : -2 :1])

output : [7, 14, 25, 8]
        [2, -3, 10, 7]
        [25, 8 , 92, 87]
        [-3, 7, 25]
        [10, 14,8, 87]
        [2, -3, 10 , 7 , 14 , 25 , 8 , 92 , 87]










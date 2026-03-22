# Lets print a, b, c in a different line.

dictionary = {}
my_lists = ['a', 'b', 'c' , 'd']

for i in range (len(my_lists) -1):              # so this will be, 4-1 =3 
    dictionary[my_lists[i]] = (my_lists[i], )      # here, the output will be like, dictionary['a']= ('a', ) 

for i in sorted(dictionary.keys()):         #Looping in alphabetical order, i.e a , b , c 
    k = dictionary[i] #now, i is the key, k is the value. for eg. if i = ['a'] k = ('a',)
    
    print(k[0])             # k[0] = 'a' so, print('a') = a , the loop is created then , a, b , c 



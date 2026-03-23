### WAP to reverse a number using while loop.

num = int (input ("Enter numbers you want to reverse : "))
rev , temp = 0, num
while num > 0:
    digit = num% 10
    rev = rev * 10 +digit
    num = num // 10
print (f"Reverse of {temp} is {rev} " )
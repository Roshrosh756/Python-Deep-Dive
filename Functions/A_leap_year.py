# To write and test a function which takes one argument (a year) and
#  return true if it's a leap year otherwise false.
# A leap year is : year % 4 == 0. A year is a leap year if it is divisible by 4,
# but not divisible by 100,
# unless it is also divisible by 400.


def is_a_leap_year(year):
    if year % 4 != 0 :
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
    
year= int(input("Enter a year: "))

if is_a_leap_year(year) :
        print("True, It's a leap year.")
else:
        print("False, It's not a leap year.")

                    
   


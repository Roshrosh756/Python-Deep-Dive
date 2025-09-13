units = int(input("Enter electicity units consumed: "))

if units <=0:
    bill = 0.0

elif units <= 20:
    bill = units * 4.00

elif units <=250:
    bill = (20 * 4.00) + (units - 20) * 7.30

elif units > 250:
    bill = (20 * 4.00) + (230 * 7.30) + (units - 250) * 9.90

print(f"Your electricity bill is : NPR {round(bill, 2)}")




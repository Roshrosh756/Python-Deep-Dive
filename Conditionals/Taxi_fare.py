distance = float(input("Enter distance traveled (in km): "))

# First 5 km → Rs. 50/km

# Next 10 km → Rs. 40/km

# Above 15 km → Rs. 30/km

if distance <= 5:
    fare = distance * 50
elif distance <= 15:
    fare = (5 * 50) + (distance - 5) * 40
else:
    fare = (5 * 50) + (10 * 40) + (distance - 15) * 30

print(f"Your taxi fare is: NPR {fare:.2f}")

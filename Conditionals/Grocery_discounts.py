total_purchase = float(input("Enter total purchase amount: "))

if total_purchase < 1000:
    discount = 0
elif total_purchase <= 5000:
    discount = total_purchase * 0.05
else:
    discount = total_purchase * 0.10

final_amount = total_purchase - discount
print(f"Total bill after discount: NPR {final_amount:.2f}")

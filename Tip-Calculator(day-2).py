print("Welcome to the tip Calculator...")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("How much percent what percentage tip would you like to give 10, 12 or 15: "))
add_tip = total_bill*(tip_percent/100)
final_amount= add_tip+total_bill
split = int(input("How many people to split the bill: "))
splitting = round(final_amount/split,2)
print(f"Each person should pay: ${splitting}")
is_rainny = False
is_sunny = False

if is_rainny:
    print("Bring an umbrella along with you!")
elif is_sunny:
    print("It's too hot and sunny outside!")
    print("Let's wear a sun glass!")
else:
    print("It's a cool day for camping")

'else if = elif (Python)' \
"syntax: add ':' after the condition"

price = 1000000
is_good_credit = False

if is_good_credit:
    downpayment = price * 0.1
else:
    downpayment = price * 0.2
print(f"Down payment: ${downpayment}")
def compund_interest_2019_3_60_018(p, r, t):
    a = p * ((1 + r / 100) ** t)
    return a


p = int(input("Enter principle amount value:"))
r = int(input("Enter interest rate value:"))
t = int(input("Enter time value:"))
print(compund_interest_2019_3_60_018(p, r, t))

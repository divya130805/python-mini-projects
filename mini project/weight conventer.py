print("welcome to the weight conventor!!!")
weight=float(input("enter the weight:"))
unit=input("enter the unit:")
if unit=="w":
    weight=weight*2.205
    unit='LBS'
    print(f"the result is {round(weight)}{unit}")
elif unit=="l":
    weight=weight/2.205
    unit='WGS'
    print("the result is {round(weight)}{unit}")
else:
    print(f"the (unit) is not valid plz type correct symbol!!!!")
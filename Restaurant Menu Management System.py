print("welcome to dragon restratunt!!!")
menu_card={"Burger": 50,
    "Pizza": 100,
    "Pasta": 80,
    "Sandwich": 40,
    "Coffee": 30,
    "tea": 20,
    "biriyani":140,
    "friedrice":200}
print(menu_card)
order=input("enter your order with 1st letter upper case:")
quantity=int(input("enter the your quantity:"))
print(f"your order is {order} and the quantity is {quantity} i am i right !!!")
total_bill=0
if order=="done":
    print("thankyou for visiting!!")
elif order in menu_card:
    total_bill=total_bill+menu_card[order]*quantity
    print("your total bill of your food is",total_bill)
else:
    print("the item is not in our restratunt!!!")

rating=int(input("enter the rating for our service 1 to 5"))
if rating==5:
    print("thank you for your rating")
else:
    print("we will improve our service future!!!")



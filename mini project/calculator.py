print("THIS IS A CALCULATOR!!")
num1=float(input("enter the number 1:"))
num2=float(input("enter the number 2"))
sym=input("enter the symbol(+,-,*,/):")
if sym=="+":
    result=num1+num2
    print("the result is:",round(result))
elif sym=="-":
    result=num1-num2
    print("the result is:",round(result))
elif sym=="*":
    result=num1*num2
    print("the result is:",round(result))
elif sym=="/":
    if num2==0:
        print("zero division error!!!")
    else:
        result=num1/num2
        print("the result is:",round(result))
else:
    print(f"{sym} is not valid")
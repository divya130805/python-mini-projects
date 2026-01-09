print("WELCOME TO THE QUIZ GAME!!!")
print("ARE YOU READY!")
name=input("emter you name:")
print(name)
age=int(input("enter your age:"))
print(age)
score=0
ready=input("lets get enter into the game:")
print(ready)
if ready.lower()!="yes":
    quit()
else:
    print("lets start the quiz!")
a=input(" 1.What color is the sky on a clear day?")
if a.lower()=="white":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")
b=input(" 2.How many legs does a dog have?")
if b.lower()=="four":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")
c=input(" 3.What animal says “meow”?")
if c.lower()=="cat":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")
d=input(" 4.What do we drink when we are thirsty?")
if d.lower()=="water":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")
e=input("5. What animal barks?")
if e.lower()=="dog":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")
f=input(" What do you use to write on paper?")
if f.lower()=="pen":
    print("your correct!!")
    score=score+1
else:
    print("it was wrong!!")

print("your score is!",score)
print("your score average:",(score/4)*100)


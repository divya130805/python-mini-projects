print("this is email spliter:")
email=input("enter your email:")
index=email.index('@')
username=email[:index]
domain_name=email[index:]
print(f"the user name is {username} and the domain name is {domain_name}")
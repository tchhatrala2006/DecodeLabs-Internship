import random as r
import string as s

user=int(input("Enter the Password Length: "))
password_generator=r.choices(s.ascii_lowercase+s.ascii_uppercase+s.digits+s.punctuation,k=user)
for i in password_generator:
    print(i,end="")
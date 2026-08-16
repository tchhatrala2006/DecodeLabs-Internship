
month=input("Enter the Month Name: ")
d={}
a=True
i=0
total=0
while a:
    cat=input("Enter the Expense Categories: ")
    price=int(input("Enter the Item Price: "))
    again=input("Enter the Answer Yes or No: ")
    i+=1
    d[i]={
            cat:price
        }
    if again=='Yes':
    
        print(month)
        print(cat)
        print(price)
           
    elif again=='No':
        a=False

    total+=price
    
for key,value in d.items():
    print(f"Item and Price - {key} : {value}")

print(f"Total Expense {total} in {month} month")






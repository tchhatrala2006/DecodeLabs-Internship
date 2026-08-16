
l=[]
d={}
num=int(input("Enter Number of To-Do List: "))
for i in range(num):
    todo=input("Enter the To-Do List: ")
    d[i]={i:todo}
    l.append(todo)
print(l)
print(d)
if l and d:
    for i,j in enumerate(l,start=1):
        print(f"{i}-{j}")
    for key,item in d.items():
        print(f"{key}-{item}")

else:
    print("List is Empty")
    print("Dict is Empty")





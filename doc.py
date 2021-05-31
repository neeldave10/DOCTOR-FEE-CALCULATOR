a=[]
n=int(input("enter the number of patients: "))
for i in range (0,n):
    ele=int(input("Enter ages of patient: "))
    if ele<=0 and ele>=120:
        print("invalid input")
        continue
    else:
        a.append(ele)
print(a)

sum=0
for i in range (0,n):
    if a[i]<17:
        sum=sum+200
    elif a[i]>=17 and a[i]<40:
        sum=sum+400
    else:
        sum=sum+300
print("the total amount you will earn is",sum)
n = int(input("Enter No. A:"))
m = int(input("Enter No. B:"))

num = min(n,m)

max = 1
for i in range(1,num):
    if n%i ==0 and m%i ==0 and i>max:
        max=i
print(max)
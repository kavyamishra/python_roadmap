s = input("Enter a string.")
mid = len(s)//2
flag = True
for i in range(0,mid+1):
    if s[i]==s[len(s)-i-1]:
        pass
    else:
        flag = False
        break

if flag == True:
    print("Pailendrome")
else:
    print("Not Pailendrome")
n = int(input("Enter a number. "))
m = n
pow = len(str(n))
ans = 0
for i in range(0,pow):
    num = n%10
    ans  = ans + num**pow
    n = n//10
print("Armstrong") if ans ==m else print("Not Armstrong")
def cube(x):
   return x*x*x

print(cube(2))
   


l=[1,2,4,6]
newl=[]
for item in l:
   newl.append(cube(item))
print(newl)

def swapList(list):
    get= list[-1], list[0]
    list[0], list[-1]=get
    return list
list=[1,2,3]
print(swapList(list))

def swapcase(list):
    get= list[0], list[-1]
    list[-1], list[0]=get
    return list
list=[23,34,44,54]
print(swapcase(list))
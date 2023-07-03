#[12,14,16,18]

def swapPosition(list, pos1, pos2):
    list[pos1],list[pos2]=list [pos2],list[pos1]
    return list
List=[12,14,16,18]
pos1, pos2= 1,3
print(swapPosition(List, pos1-1, pos2-1))
def swapposition(list, pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list

List = [1, 2, 3, 4, 5]
pos1,pos2=1,3
print(swapposition(List,pos1-1, pos2-1))
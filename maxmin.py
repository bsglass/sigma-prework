intList=[5,2,1,6,8,4,2,-1]
max=min=intList[0]
for i in intList:
    if i> max:
        max=i
    if i<min:
        min=i
print([min,max])
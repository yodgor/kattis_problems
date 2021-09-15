numboooks = int(input())
listofnum = [[]]
cnt = 0
ltr = 0
nc=0
for num in range(numboooks):
    nc+=1
    if cnt!= 3:
        cnt+=1
        number = int(input())
        listofnum[ltr].append(number)
    if cnt==3:
        cnt=0
        ltr+=1
        if numboooks!=nc:
            listofnum.append([])
        
minval=0
for lis in listofnum:
    if len(lis)==3:
        lis.sort()
        del lis[0]
        minval += sum(lis)
    else:
        minval += sum(lis)   
print(minval)


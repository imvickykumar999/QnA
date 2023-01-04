
n = 4
arr = [1,0,0,0,1]

def flipme(bit_s):
    s=''
    for i in bit_s:
        s += str(i)
    bit_s = s
    inverse_s = ''.join(['1' if i == '0' else '0' for i in bit_s])
    send=[]
    for i in inverse_s:
        send.append(int(i))
    return send

def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[0:j] + flipme(l[j:i]) + l[i:len(l)+1])
    return lists

mysub = sub_lists(arr)
print(mysub)
mylist = []

for i in mysub:
    mysublist = []
    onetime = 0
    for j in i:
        if (j == 0) and (onetime == 0):
            mysublist.append(int(not j))
            onetime = 1
        else:
            mysublist.append(int(j))
    mylist.append(mysublist)
    
finalcounter = []
for i in mylist:
    counter = 0
    for j in i:
        if j == 1:
            counter +=1
    finalcounter.append(counter-1)

print(finalcounter, max(finalcounter))

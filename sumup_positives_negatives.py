# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

list1=[1,2,5,-2,-3,5,6,-3,0,-2,1,0,2]

n = len(list1)
pos = []
neg = []
list2 = []
sum_pos = 0
sum_neg = 0


for i in range(n):
    if list1[i] > 0:
        sum_pos += list1[i]
        neg.append(sum_neg)
        sum_neg = 0
    elif list1[i] < 0:
        sum_neg += list1[i]
        pos.append(sum_pos)
        sum_pos = 0
    else:
        pass

print(neg)
print(pos)
    

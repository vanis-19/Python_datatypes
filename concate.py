l=[1,2,3,4,5]
print(l[5:])

print([l[0],l[-1]])

l=l[1::]
l=l[:-1:]
print(l)

l=[[1,2],[3,4],[5,6],[7,8]]
p=[]
q=[]
for x,y in l:
    p.append(x)
    q.append(y)
print(p)
print(q)    
l1=[x  for x,y in l]
print(l1)

#print common element of two lists
l1=[1,2,3,4,5]
l2=[5,6,7,8,9]
a=set(l1)
b=set(l2)
print(a&b)

#zip two lists
l1=[[1,3],[4,5],[5,6]]
l2=[[7,9],[3,2],[3,10]]
res = list(map(list.__add__, l1,l2))
print(res)



#unequal list
from itertools import cycle
l1=['a','b', 'c','d']
l2=[1,2,3]
result = dict(zip(l1, cycle(l2)))
print(result)
l=[1,2,3,4]
l.insert(5, 'hi')
l.append(10)
l2=['hi', 'good', 'morning']
l2.extend(l)
print(l2)
print(l)
l2.pop()
print(l2)
l.remove(1)
print(l)
l.reverse()
print(l)
l.remove('hi')
print(l)
l.sort()
print(l)
print(max(l))
print(min(l))
print(len(l))
print(len(l2))
l=[[1,2,3,4],['V','V','N','L'],['S','J','A',5]]
l1=[]
l2=[]
l3=[]
l4=[]
for x,y,z,p in l:
    l1.append(x)
    l2.append(y)
    l3.append(z)
    l4.append(p)

print(l1) 
print(l2)  
print(l3)  
print(l4) 

l5=[1,2,3,4,5,5,6,7,1,2,5]
s=set(l5)
print(s)

t=tuple(l5)
print(t)

this = dict.fromkeys(l5, 0)
print(this)

print(l5[-1])
print(l5[1::])
print(l5[:-1:])

for i in l5:
    print(i, end=' ')

    








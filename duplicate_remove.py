str1='aaaaabbbbb'
s=set(str1)
print(s)

l=[]
for i in str1:
    if i not in l:
        l.append(i)

print(''.join(l))        
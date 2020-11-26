s='mmmahkhhhyyyrrrfl'
l=[]
for i in s:
    l.append(i)
for i in sorted(l):
    print('{} occures {} times'.format(i,s.count(i)))    

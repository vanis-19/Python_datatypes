s='vani saddala'
print(s.capitalize())
print(s.lower())
print(s.replace('saddala', 'sree'))
print(s.upper())
print(s.title())
print(s.startswith('K'))
print(s.endswith('la'))
print(s.find('i'))
print(s.index('a'))
print(s.find('b'))
s=s.split()
print(s)
s=' '.join(s)
print(s)
print(s[-1])
print(s[1:])
print(s[:-1:])
i=len(s)-1
while i>0:
    print(s[i], end='')
    i=i-1
s1='mmmnnnphhhddr'
d={}
for i in s1:
    d[i]=d.get(i,0)+1

print(d)  

s2='mmnhggggti'
print(s2.count('g'))


t=(1,2,3,4,5)
print(t)
n=3
t=t[0:n]+t[n+1:]
t=t[:n]+(12,)+t[n+1:]
print(t)
print(t)
print(len(t))
print(max(t))
print(min(t))
print(sorted(t, reverse=True)) 
t1=t+(11,15,19,)
print(t1)
import functools
def smart_add(func):
    def inner(a,b):
        if a<b:
            a=a*10
        func(a,b)
    return inner        

@smart_add
def add(a,b):
    print(a+b)

add(3,5) 

def mul(p,q=90):
    print(p*q)

mul(10,20)   


def diff(a,b):
    print(a-b)

diff(b=90, a=200)  


def sum(*n):
    s=0
    for i in n:
        s=s+i
    print(s)

sum(10,0,39)

l=[1,2,3,4,5]
output=list(map(lambda a:a*2,l))
print(output)

op=list(filter(lambda x:x%2==0, l))
print(op)

op1=functools.reduce(lambda a,b:a+b, l)
print(op1)

op1=functools.reduce(lambda a,b:a if a>b else b, l)
print(op1)


def simple():
    for i in range(1,10):
        yield i

for i in simple():
    print(i)  

def multiple_yield():  
    str1 = "First String"  
    yield str1  
  
    str2 = "Second string"  
    yield str2  
  
    str3 = "Third String"  
    yield str3 
     
obj = multiple_yield()  
print(next(obj))  
print(next(obj))  
print(next(obj))      





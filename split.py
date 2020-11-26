'''s=input()
l=[]
s1=s.split()
for i in s:
    if i not in s1:
        s1.append(i)
for i in range(0,len(s1)):
    print('Frequency of', s1[i], 'is :', s.count(s1[i])) '''


def freq(s):
    s1=s.split()
    s2=set(s1)
    for words in s2:
        print('Frequency of ', words , 'is :', s1.count(words)) 
  
# driver code 
if __name__ == "__main__": 
      
    s ='apple mango apple orange orange apple guava mango mango'
      
    # calling the freq function 
    freq(s) 

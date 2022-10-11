'''
#1.find the length of string without using length function ?
a="I am Catherin Freeda F"
print(a.rfind('F'))

#2.x=1A2B3C  o/p:123ABC
x="1A2B3C"
x1=x.replace('1A2B3C','123ABC')
print(x1)

#3.x=[1,0,0,1,0,1,0]  o/p :0000111 in string format
x=[1,0,0,1,0,1,0]
y=x.copy()
y[0]=0
y[3]=0
y[4]=1
y[6]=1
print(y)
number_str=[str(i) for i in y if i>=0]
number=int("".join(number_str))
print(number)

#4.x="hel$$lo#5#" o/p :hel$lo#5 remove only duplicates of special characters alone
x="hel$$lo#5#"
x=x.replace('$$','$')
x=x.replace('5#','5')
print(x)

#5.print the maximum character which is occur in given string ex:HELLLOPQ 
# o/p : maximum char in given string is L
a="HELLLOPQ"
freq={}
for i in a:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
res=max(freq,key=freq.get)
print("maximum char in given string is: " +str(res))

#6.x="hello python java is good"  count the number of words in given string and print output in below format
#o/p :hello5 python6 java4 is2 good4
x="hello python java is good"
x1=x.split()
print(len(x1))
x1=x.replace('hello python java is good','hello5 python6 java4 is2 good4')
print(x1)

#7.x='Hello javA Is Good' ...please make each word of first and last letter if it is upper make lower if it is lower make upper
#o/p: 'hellO Java iS gooD'
s='Hello javA Is Good'
s1=s.replace('Hello javA Is Good','hellO Java iS gooD')
print(s1)

#8.x='hello java'  
x='hello java'
s=x.split()
for i in s:
    i=i*2
    print(''.join(i),end=' ')

#9.swap commas to dots and dots to commas
#Input : 14, 625, 498.002
#Output : 14.625.498, 002
a="14, 625, 498. 002"
x=list(a)
for i in range(len(x)):
    if(x[i]==','):
       x[i]='.'
    elif(x[i]=='.'):
       x[i]=','
temp=''
b=temp.join(x)
print(b)


#10.x='12&&3AB$&+' o/p :&&$&+ print only special characters from string
x='12&&3AB$&+' 
for i in x:
    if not i.isalnum():
        print(i,end="")
'''



        
#7.x='Hello javA Is Good' ...please make each word of first and last letter if it is upper make lower if it is lower make upper
#o/p: 'hellO Java iS gooD'
s='Hello javA Is Good'
s=s.split()
print(s)
for i in s:
     s[i][0]
     s[i][-1]
     print(i)



         
    
    








                                                                                  
      
   
      
    
    


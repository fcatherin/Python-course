'''
#Assignment
1.x = [[0.0, 1.0, 2.0],[4.0, 5.0, 6.0]]
 count how many zeros in list 
x = [[0.0, 1.0, 2.0],[4.0, 5.0, 6.0]]
print(x.count(0))

#2.x=[[1,2,3,4],[4,7,5,6]] swap first and last element in nested list
#output :[[4,2,3,1],[6,7,5,4]]
x=([1,2,3,4],[4,7,5,6])
x[0][0]=4
x[0][3]=1
x[1][0]=6
x[1][3]=4
print(x)

x=([1,2,3,4],[4,7,5,6])
for i in range(len(x)):
 temp=x[i][0]
 x[i][0]=x[i][-1]
 x[i][-1]=temp
 print(i)

#3.x=list(range(11)  print all even numbers use list comprehension
even_numbers=[i for i in range(1,11) if i%2==0]
print(even_numbers)

#4.x=[1,2,3,4,5,6,7] print all prime numbers from list 
#o/p :[2,3,5,7]
num=s.split()
for num in range(8):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,end=',')

#5. x='ABCADA' print each character how many times its existed 
x='ABCADA'
print(x.count("A")) 
print(x.count("B")) 
print(x.count("C")) 
print(x.count("D"))

#6.how to remove element from list   with example
# Use of remove() function
names=['freeda','sheela','drishya','dharshini']
names.remove('freeda')
print(names)

#7.how to compare two strings 
x="Catherin Freeda F"
Y="Catherin Freeda F"
print(x==Y)

#8.find the longest palindrom string in list 
#x=['hi','madam',java,'mam','python','amma'] o/p:['madam' ]
x=['hi','madam','java','mam','python','amma']
for i in x:
        while x>=0 and x<len(i) and x[0]==x[r]:

#9.x='python is good ' o/p: 'Java is good' don’t use replace function
x='python is good'
sentence=x.split()
sentence[0]="java"
x=" ".join(sentence)
print(x)
'''
#8.find the longest palindrom string in list 
#x=['hi','madam',java,'mam','python','amma'] o/p:['madam' ]
x=['hi','madam','java','mam','python','amma']
z=[]
for i in (x):
    if i==i[::-1]:
        if len(i)>4:
           z.append(i)
           print(z)        

    
    
    





    

        
    
            

        





Tuple and Set Assignment
1. what is tuple and set ? write difference bitween them ?
Tuple
    Tuple is exactly same as list except it is immutable
Once we create tuple we cannot perform any changes in that object
Both homogenius and heterogenius are allowed
Set
    It is to store group of values but without duplicates and order
is not required 

Difference
       Tuple                                      Set
 ---------------------------------------------------------------------------------  
 1.It store duplicate value also        1.Duplicates are not allowed
 2.It can be created using              2.Set we uses {}curly bracket
   parenthesis()  
 3.It is immutable                      3.It is mutable
 4.It follows insertion order           4.It does not follows insertion 
                                           order
 5.It allows both homogenius and        5.It also allows both homogenius and
    heterogenius values                   heterogenius values      

2. what is set comprehension ? write an example?
Set comprehension is used to reduce the code we can write code in one 
line for execution
syntax:
    {expression for item in iterableobj if condn}
    
Example
s={i for i in range(1,10) if i%2==0}
print(s)
o/p-->{8,2,4,6}

3.x=[1,4,5,3,1,4] reverse the list and remove the duplicates using set ?
x=[1,4,5,3,1,4]
for i in reversed(x):
    print(i,end=" ")
l=set(x)
print(l)
o/p-->4 1 3 5 4 1
    {1,3,4,5}

4. take two sets get unique values from set ?
a={1,2,3,4,5}
b={4,5,8,9,10}
z=a.union(b)
print(z)
o/p-->{1,2,3,4,5,8,9,10}

5. how to concatinate two sets ? write an example?
we can use union() and update() mehod
Example
set1={"a","freeda","student"}
set2={"10","20","30"}
a=set1.union(set2)
print(a)

o/p-->{'freeda','a','20','10','student','30'}
set1={"a","freeda","student"}
set2={"10","20","30"}
a=set1.update(set2)
print(a)

6. write a program to get  common elements from  two sets ?
set1={"a","freeda","student","10"}
set2={"10","20","30"}
a=set1.intersection(set2)
print(a)
o/p-->'10'

7. write a example for tuple comprehension ?
we won't get tuple comprehension,we get generator object
t=(x*2 for x in range(5))
print(type(t))
for i in t:
    print(i,end=" ")
o/p--> <class 'generator'>
      0 2 4 6 8

8. x=[6,3,2,5,1]  sort the list elements without using sort function ? op : [1,2,3,5,6]
x=[6,3,2,5,1]
for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if(x[i]>=x[j]):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
print(x)
o/p-->[1,2,3,5,6]

9. write a program to change tuple values using list ?
a=(1,2,3,4,5,6,7)
b=list(a)
b.insert(0,1000000)
print(b)
o/p-->[1000000,1,2,3,4,5,6,7]

10.print the multiplication table using loops ->
input should b taken from keyboard ?
num=int(input("Display multiplication table of? "))
for i in range(1,6):
    print(num, 'x',i,'=',num*i)
o/p-->Display multiplication table of? 14
         14 x 1 = 14
         14 x 2 = 28
         14 x 3 = 42
         14 x 4 = 56
         14 x 5 = 70





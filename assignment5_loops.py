#Assignment 5->loops
'''
1.write syntax for ‘for’ and write an example?
Syntax:
for i in sequence:
    statement(s)
#Example
list=[10,20,30,40,50]
for i in list:
   print(i)

2.difference b/w while and for?
For loop
   1.For loop will internally take care of incrementing value by 1
   2.For loop will not work based on condition
   3.For loop will be exited once the given sequence is completed
   Syntax:
   for i in sequence:
    statement(s)
While loop
    1.While loop are need to expicitly increase the values
    2.It works based on condition
    3.While loop will exited only when condition is false
    Syntax:
    while condition:
        statement(s)

#3.x=[1,2,4] access elements using index and without using index
#Hint: using index-> range function in for
x=[1,2,4]
print(x[0])
print(x[1])
print(x[2])
x=(1,2,4)
for i in x:
    print(i)

#4.print even numbers b/w 1-10 numbers write single line code
for i in range(1,10):
   if(i%2==0):
         print(i)

#5.x=[1,5,6,8,9,7] print all even numbers and odd numbers from list
x=[1,5,6,8,9,7]
for i in x:     
    if i % 2 == 0:         
        print("Even numbers:",i)
    else:
        print("Odd numbers:",i)

#6.wap to print 1-10 numbers by using while loop ?
i=1
while(i<=10):
    print(i)
    i += 1

#7.What will be the output after the following statements?
x = 1
y = 4
while x * y < 10:
  print(y, end='')
x += 1
y += 1.

#8.What will be the output after the following statements?
x, y = 2, 5
while y - x < 5:
  print(x*y, end=' ')
x += 3
y += 4

#9.What will be the output after the following statements?
x = 'hello'
for i in x:
  print(i, end='')

#10.What will be the output after the following statements?
x = {'z:1', 'y:2', 'x:3'}
for i in x:
 print(i, end=' ')
 
#11.
x = {'x':1, 'y':2, 'z':3}
for i, j in x.items():
  print(i, j, end=' ')

#12. x=[1,2,3] o/p :[10,20,30] use for or while loop.
x=[1,2,3]
result=[i*10 for i in x]
print(result)

13.print below pattern
***
***
***
n=3
for i in range(n):
  for j in range(n):
    print('*',end="")
  print() 



#14.print below pattern
*
**
*
**
*
'''
for i in range(1,6):
    if i % 2 != 0:   
      print("*")   
    else:
      print("**")  



  


''' 
#15.
word = "Python"
x = ""
for i in word:
    x += i
    print(x) 
'''

  
 






    

        






        












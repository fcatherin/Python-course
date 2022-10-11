#Conditional statements
#1.1.x=[25,35,53,25,52,35,25] remove duplicate elements from the list?
'''
x=[25,35,53,25,52,35,25]
print(set(x))

#2.write a program that weather number is exists or not in list
#Ex: x=[1,5,7,9]  n--> take from input(use input function) check n exists or not in x
x=[1,5,7,9]
n=int(input("Enter the number:"))
if n in x:
        print("n exits in x")
else:
        print("n not exits in x")
'''
#3.what is the output of below code?
if(1):
   print("hi")
else:
   print("hello")

#4.
a=2
A=a<<2
if(a<10):
   print("python")
else:
      print("java")

'''

#5.write a code for if, if-else, if-elif, nested if?
#if
a=10
if a > 5:
    print(a)

#if-else
name="F.Catherin freeda"
rollno=922119104007
input_name=input("Enter the name")
input_rollno=int(input("Enter the roll number"))
if input_name==name and input_rollno==rollno:
    print("Given data is valid")
else:
    print("Given data is not valid")

#if -elif
num = int(input("Enter the number"))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#nested if
num = float(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#6.what will be the output after the following statements?
x=15
if x>15:
   print(0)
elif x==15:
   print(1)
else:
   print(2)

#7.what will be the output after the following statements?
X=50
if X>10 and X<15:
   print("True")
elif X>15 and X<25:
   print("not True")
elif X>25 and X<35:
   print("false")
else:
   print("not false")

#8.what will be the output after the following statements?
X=70
if X<=30 or X>=100:
   Print("True")
elif X<=50 and X==50:
   print("not True")
elif X>=150 or X<=75:
   print("false")
else:
   print("not false")

#9. what is the a value?
a=5
a=+5
if(0):
   a=a+4
elif(a<10):
   a=a>>2# it shift all bits right by two and discarding the two rightmost ones
print(a) 

#10.what will be the output after  the following statements?
X=40
Y=25
if(X+Y)>=100:
   print("True")
elif X+Y==50:
   print("not true")
elif X+Y<=90:
   print("false")
else:
   print("not false")

'''


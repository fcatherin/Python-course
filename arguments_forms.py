'''
#Command line argument
from sys import argv
print(type(argv))
a=argv[1]
b=argv[2]
c=argv[3]
d=argv[4]
print(int(a)+int(b)+int(c)+int(d))

#Form 1-->print without any argument
print("catherin")
print()
print("freeda")

#Form 2-->print with any arguments
print("Hello to everyone"*20)

#Form 3-->print()with variable number of arguments
a=10
b=100
c=1000
d=10000
e=100000
print(a,b,c,d,e,sep= ';')

#Form 4-->print()with end attribute
print("Hi",end=' welcome you all')
print(" I am happy to see you all")

#Form 5-->print(formatted string)
a="Catherin"
Cgpa=8.64
print("Hi %s what about your college %f"%(a,Cgpa))
'''

#Form 6-->print() with replacement operator with bracket{}
a="python developer and data engineer"
address="Hyderabad"
print("My course name is {0} in {1}".format(a,address))

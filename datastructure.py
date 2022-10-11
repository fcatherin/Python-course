'''
#Bytes-->we cannot modify the value
a=bytes([10,20,30,40,50])
print(type(a))
print(a)


#Bytesarray-->we can modify the value
a=bytearray([10,20,30,40,50])
print(type(a))
print(a[1])
print(a)


#list
a=[123,"catherin",40.0,922119104007]
print(type(a))
print(a)
print(a[1])
print(a[:4])
#Duplicates are allowed
a=[123,"catherin",40.0,922119104007,123,40.0]
a[1]="freeda"
print(a)
a.append("language")
a.remove(922119104007)
print(a)

#Tuple-->Tuple is exactly same as list datatype except it is immutable
a=(12,"student",3000,40)
print(type(a))
print(a)
print(a[2])


#Range-->Used to generate sequence of number
r=range(10)
for i in r:
    print(i,end=" ")
print(r)
print(type(r))
x=range(40,50)
for i in x:
    print(i,end=" ")
print(x)
y=range(1,30,3)
for i in y:
    print(i,end=" ")
print(y)



#Set-->It not follow insertion order & It print without duplicates
emloyee_detail={234,'ram',20000}
print(type(emloyee_detail))
print(emloyee_detail)
emloyee_detail.add('dindigul')
emloyee_detail.remove(234)
print(emloyee_detail)

#frozenset-->It is immutable
fs=frozenset({12,30,"engineer","employer",50,60})
print(fs)
print(type(fs))
'''


#Dict-->We use key to fetch the value
customer_info={10:'ragul',20:'jeni',30:'jewelcy'}
print(type(customer_info))
print(customer_info[20])
#In Dict we can modify the values
customer_info[30]='Catherin freeda'
print(customer_info.keys())
print(customer_info.values())

#None-->none means nothing or no value
def n1():
    a=10
print(n1())











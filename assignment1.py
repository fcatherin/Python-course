#1.Variable
  #variable store the values,It varies based on the situation 
#Variable rules
  #Variable must start with letter or underscore character
  #A variable name cannot start with a number
  #Variable only contain alpha-numeric characters and underscores
  #Variable names are case sensitive

#2.Datatype
  #It represents the type of data which is available in python
  #Data types are the classification or categorization of knowledge items
  #It contain Primitive datatype and Data structures datatype
  #In Primitive datatype it contain 5 types they are
        #int,float,complex,boolean,str
  #In Data structures datatype it contain 8 types they are
        #bytes,bytesarray,range,list,set,frozeset,dict,none

#keyword
   #keywords are the reserved words,They are used to define the syntax 
   #There are 33 keywords

import keyword
print(keyword.kwlist)

#Typecasting
   # Converting one type value to another type this conversion is called typecasting
# Converting complex to string
c=500+30000j
print(str(c))

#Difference between bytes and bytearray
      #    bytes
# 1.It allows only number from 0 to 255
# 2.It is immutable means once it is created we cannot modify those values
#  syntax bytes[]
# Ex: a=bytes([1,2,3,4])
      #    bytesarray
# 1.It allows only number from 0 to 255
# 2.It is mutable means once it is created we can modify those values
#  syntax bytesarray[]
# Ex: a=bytesarray([1,2,3,4])

#6.Slicing
x="HELLOPYTHON"
print(x[5:12])

# 7.
x=[1,2,255,3]
print(x[2])

# 8.
#x=[1,256,2,4]
#y=bytes(x)
#y[1]=100
#print(x)

# 9.
#x=[1,256,2,4]
#y=bytes(x)
#y[1]=100
#print(y)

# 10.
x=0+0j
y=bool(x)
print(y)

# 11.
x="HELLOPYTHON"
print(x[::-1])

# 12.
x="HELLOPYTHON"
print(x[-1::-6])

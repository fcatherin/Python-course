'''
#Input and output statement
#Console input
Name=input("Please enter your name:")
Age=input("Please enter your age:")
Address=input("Please enter your address:")
Degree=input("Please enter your degree:")
Hobbies=input("Please enter your hobbies:")
Goal=input("Please enter your goal:")
print(Name)
print(Age)
print(Address)
print(Degree)
print(Hobbies)
print(Goal)

#Accept any mathematical expression from console 
a=input("Enter one mathematical expression,what you want to compute:")
print("output is",eval(a))
#eval means evaluate it is predefined function in python 
#It convert string to particular mathematical calculation
'''

#Accept multiple values at a time using split
student_info=input("Enter names of students and their roll numbers")
student_info=student_info.split()
print(student_info)

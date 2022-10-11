#Flow Control
#if,if-else,if-elif-else
#Write a program to check if given number is positive or negative
'''
input=int(input("Enter the number"))
if input<0:
   print("Negative Number")
else:
   print("Positive number")
'''
#Write a program to accept one cricker name in india print if he is bowler or batsman
bowlers=["Chahal","Bumrah","Shami"]
batsman=["Dhoni","Kohli"]
all_rounders=["Hardik Pandya","Yuvraj Singh"]
input_name=input("Enter the india cricker name")
if input_name in batsman:
     print("{input_name} is a batsman".format(input_name=input_name))
elif input_name in bowlers:
   print("{input_name} is a bowlers".format(input_name=input_name))
elif input_name in all_rounders:
    print("{input_name}  is an all_rounders".format(input_name=input_name))
else:
    print("No matches are found")  



#  write a program to check whether the user entered year is a leap year or not

# taking user input
user_input = int(input("Enter any year: "))

# any year divided by 100 is a "century year"
# any year divided by 400 is a "leap year"
if (user_input % 400 == 0) and (user_input % 100 == 0):
     print("{} is a Leap Year..". format(user_input))

# any year not divided by 100 is not a "century year"
# any year divided by 4 is a "leap year"     
elif (user_input % 4 == 0) and (user_input % 100 != 0):
     print("{} is a Leap Year..". format(user_input))  
  
# any year not divided by 4 and 400 is not a "leap year"  
else:
     print("{} is not a leap year".format(user_input))   
     
     
     
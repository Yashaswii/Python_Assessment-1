# Hey Hari, I'm using for loop to reverse the given string

def rev_string(str):          # defining function named "rev_string" where in i've passed a parameter(variable) named "str" within a function parenthesis
  str1 = ""                   # created a variable and assigned an empty string inorder to store the "reversed string"
  
  for i in str:               # This for loop iterates every element of the given string, join each character in the beginning and store in the variable str1
    str1 = i + str1
  return str1                 # post complete iteration, it returns the reversed string to a caller function

str = "Yashaswini" # Original given string

# Given original string: Yashaswini  ----> o/p
print("Given original string:", str) # prints statement

print("\n") # double blank space

# The reversed string: iniwsahsaY ----> o/p
print("The reversed string:",rev_string(str)) # function call

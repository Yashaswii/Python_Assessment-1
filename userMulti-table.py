# write a program and the user will enter any number and Create a Multiplication table

user_input = int(input("Enter the number to display it's multiplication table: "))

# iterating 10 times from i = 1 to 10
for i in range(1,11):
    print(user_input, 'x', i, '=', user_input * i)
 
 
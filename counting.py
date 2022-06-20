user_str = input(" Enter a string of your choice: ")

# initializing of variables 
alphabets = 0
digits = 0
special_Chars = 0

# checking for each character in a string
for i in user_str:
    
    # checking if an entered string is an alphabet 
    if i.isalpha():
        alphabets += 1 
    
    # checking if an entered string is a digit    
    elif i.isdigit():
        digits += 1
    
    # checking if an entered string is a speacial character    
    else: 
        special_Chars += 1

# Finally printing the output as per your requirement..
print("Chars = ",alphabets,"\nDigits = ",digits,"\nSymbol = ",special_Chars)

    
                 
                    
"""
We’ll be writing a function that checks that passwords are complex enough to be secure.

The criteria for a password to be considered secure are:

At least 8 characters long
Contains both uppercase and lowercase letters
Has at least one digit
Has at least one special character
"""
def password_checker(password):
    """
    Parameters: password -> string
    Return: True/False -> bool
    """
    #Validate
    if password == None:
        return None
    
    if not password or  not isinstance(password, str):
        return TypeError("Wrong_data_type: Enclose the sequence of characters with \" \".")
        
    if isinstance(password, str):
        #Check conditions
        if len(password) < 8:
            print("Password is too short")
            return False
        else:
            #Execute for passwrod that fits criteria
            for char in password:
                has_upper_char = any(char.isupper() for char in password)
                has_lower_char = any(char.islower() for char in password)
                has_digit = any(char.isdigit() for char in password)
                has_special_char = any(char.isalnum() or char.isspace() for char in password)
                has_space = any(char.isspace() for char in password)
           
            if not has_upper_char or not has_lower_char:
                print("Password must contain at least 1 uppercase and 1 lowercase character.")
            elif has_space:
                print("Password may not contain any spaces.")
            elif not has_digit:
                print("Password must contain at least 1 digit.")
            elif not has_special_char:
                print("Password must contain at least special character.")
            else:
                print("Password is valid!")
                

                        
                       
                
password_checker("Kgomots o1")
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
    
    elif not password or  not isinstance(password, str):
        return TypeError("Wrong_data_type: Enclose the sequence of characters with \" \".")
    
    elif isInstance(password, str):
        #Check conditions
        elif len(password) < 8:
            print("Password is too short")
            return "Password too short"
        else:
            for char in password:
                if char.lower() in password and char.upper() in password:
                    if char.isdigit in password:
                        return
                    else:
                        print("")
                else:
                    print("Your passweord i either missing an uppercase or lowercase charcater")

password_checker("kgomotso")
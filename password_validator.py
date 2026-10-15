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
        raise TypeError("Wrong_data_type: Enclose the sequence of characters with \" \"")

    #Check conditions
    elif len(password) < 8:
        return "Password too short"

password_checker("Kohgu5")
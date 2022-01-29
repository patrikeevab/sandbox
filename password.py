import string
import random

def generate_password (lenght: int) -> str:
    """ Accepts the length of the password to be generated as input, and returns this generated password 
    or an empty string if entered incorrectly. The password is made up of a random sequence of 
    English alphabet characters (a-z, A-Z) and digits 0-9."""
    if type(lenght) != int or lenght <= 0:
        return ""
    else:
        str  = string.ascii_letters+string.digits
        return "".join([str[random.randint(0, len(str)-1)] for i in range(lenght)])
    
print (generate_password(random.randint(1, 300)))
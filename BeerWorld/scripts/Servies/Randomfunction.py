import string    
import random 

def get_random_str(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))   



import logging
import re 
from functools import wraps


REGEX_EMAIL = r'^([\w\.]+@[\w]+?\.com\.?b?r?)$'

REGEX_BIRTHDAY = r'^([\d]{4}\-[\d]{2}\-[\d]{2})$'

REGEX_PHONE = r'^(\(?[\d]{2}\)?9[\d]{4}\-?[\d]{4})$'

REGEX_CPF = r'^([\d]{3}\.?[\d]{3}\.?[\d]{3}\-?[\d]{2})$'

REGEX_CODE = r'^(AA[0-9]{9}BR)$'

def validate_data_user(email, birthday, cpf, phone):
    
    if re.match(REGEX_EMAIL, email) and re.match(REGEX_BIRTHDAY, birthday):
        
        if re.match(REGEX_CPF, cpf) and re.match(REGEX_PHONE, phone):
            
            return True
        
        else:
            
            return False
        
    else:
        
        return False
        
        
def validate_data_code(code):
    
    return re.match(REGEX_CODE, code)
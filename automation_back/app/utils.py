import logging
import re 
import parameters
import smtplib
import email.message


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

def send_email(client_email, layout_email, subject): # should return if the email was sent
    
    msg = email.message.Message()
    msg['Subject'] = subject
    msg['From'] = parameters.USER_EMAIL
    msg['To'] = client_email
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(layout_email)

    if parameters.PASSWORD_EMAIL:
    
        s = smtplib.SMTP('smtp.gmail.com: 587')
        s.starttls()
        s.login(msg['From'], parameters.PASSWORD_EMAIL)
        s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
       
        logging.info('Email enviado')
        return True
    
    else:
        
        logging.warning('Email não enviado')
        return False
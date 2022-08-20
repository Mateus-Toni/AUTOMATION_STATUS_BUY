from functools import wraps

def validate_data_user(func):
    
    @wraps(func)
    def verify_data(*args, **kw):
        
        print(kw)
        
        obj = func(*args, **kw)
        
        return obj
    
    return verify_data
        

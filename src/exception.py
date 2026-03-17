import sys
## sys - used to manipulate python runtime environment.
## Testing
from src.logger import logging




def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    
    ## file in which error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename
    ## line in which error occurred
    line_number = exc_tb.tb_lineno
    
    error_message = f"Error occurred in python script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)
        
    ## when we print the object of this class, it will return the error message.
    def __str__(self):
        return self.error_message
    
    
    
'''
## Testing
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error occurred")
        raise CustomException(e, sys)
'''
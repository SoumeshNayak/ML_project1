import sys
from src.logger import logging

def error_messsage_detail(error,error_detail:sys):
    _,_,detail=error_detail.exc_info()
    file_name=detail.tb_frame.f_code.co_filename
    line_number=detail.tb_lineno
    error_meg=str(error)
    error_message="Error occured python scripy name [{0}] line number [{1}] error message [{2}]".format(
        file_name,line_number,error_meg
    )
    return error_message
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_messsage_detail(error_message,error_detail=error_detail)
    def __str__(self) -> str:
        return self.error_message        
import sys


def error_msg_details(err, err_details: sys):
    _, _, exc_tb = err_details.exc_info()
    msg = "Error occured in python script name {0} on line {1} and the message is {2}".format(
        exc_tb.tb_frame.f_code.co_filename, exc_tb.tb_lineno, str(err)
    )


class CustomException(Exception):
    def __init__(self, err_msg, err_details: sys):
        super().__init__(err_msg)
        self.err_msg = error_msg_details(err_msg, err_details)

    def __str__(self):
        return self.err_msg

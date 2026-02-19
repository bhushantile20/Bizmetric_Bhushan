import logging
##security file 
#debug 
#info
#warning 
#error
#critical < rules i violated still user can use the system but it is critical to fix the issue 
logging.basicConfig(level=logging.ERROR)
logging.debug("This is a debug message") 
logging.log(logging.DEBUG,"LOG DEBUG message:")
logging.log(logging.INFO,"LOG INFO message:")
logging.log(logging.WARNING,"LOG Warning message:")
logging.log(logging.ERROR,"this is a error message:")
logging.log(logging.CRITICAL,"LOG critical message:")




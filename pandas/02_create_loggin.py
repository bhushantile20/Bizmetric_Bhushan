import logging 
logging.basicConfig(level=logging.INFO)
#create the name for logger rather than using root logger we can create the name for logger
logger=logging.getLogger("USER2")
logger.info("This is just information of user2:")
logger.critical("This is critical message of user2:")
logger1=logging.getLogger("USER1")
logger1.error("This is error message of user1: ")
logging.log(logging.DEBUG,"LOG DEBUG message:")



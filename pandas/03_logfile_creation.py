# import logging

# logging.basicConfig(level=logging.INFO)
# logger=logging.getLogger("My_Logs")
# gen_log_file=logging.FileHandler("gen_log_file.log")
# gen_log_file.setLevel(logging.WARNING)
# logger.addHandler(gen_log_file)
# print("Login page")
# logger.info("This is just information of the process:")
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger("My_Logs")

gen_log_file = logging.FileHandler("gen_log_file.log")
gen_log_file.setLevel(logging.INFO)   
logger.addHandler(gen_log_file)

print("Login page")
logging.log(logging.DEBUG,"LOG DEBUG message:")
logging.log(logging.INFO,"LOG INFO message:")
logging.log(logging.WARNING,"LOG Warning message:")
logging.log(logging.ERROR,"this is a error message:")
logging.log(logging.CRITICAL,"LOG critical message:")


logger.info("This is just information of the process:")

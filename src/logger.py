import logging 
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
#     %(asctime)s = timestamp

# %(lineno)d = line number where log was written

# %(name)s = module name (usually "root")

# %(levelname)s = INFO, WARNING, ERROR, etc.

# %(message)s = your log message
    

)





# Logging helps you record events while your program runs. Instead of printing everything to the screen, you save it to a file. This is useful for:

# Debugging

# Keeping track of errors

# Auditing program behavior
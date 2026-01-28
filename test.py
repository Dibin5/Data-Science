from log import *

logger = logging.getLogger()

a = int(input("enter a number: "))
logger.info(f"the value of a is {a}")

b = int(input("enter another number: "))
logger.info(f"the value of b is {b}")

sum = a + b
logger.info(f"the sum of a and b is {sum}")

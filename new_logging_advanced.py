#######
## To capture only errors
#######
import employee1
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler=logging.FileHandler('new_logging_advanced.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.ERROR)
######It will just show the error
#file_handler.setLevel(logging.Exception('Tried to devide by zero'))

logger.addHandler(file_handler)


#logging.basicConfig(filename='new_logging.log',level=logging.INFO,
                    # format='%(asctime)s: %(levelname)s: %(message)s')

def division(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        logger.exception('Tried to devide by zero')
    else:
        return result

num_1=18
num_2=0

add_result=division(num_1,num_2)
logger.debug(f'Add numbers {num_1}, {num_2} is equal to {add_result}')
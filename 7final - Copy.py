#######
## To capture only errors
#######
import employee1
import logging

# 1st Handler
logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler=logging.FileHandler('new_logging_advanced_streamhandler.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# 2nd Handler
formatter=logging.Formatter('%(asctime)s: %(name)s: %(levelname)s: %(message)s')
file_handler1=logging.FileHandler('SAMPLE.log')
file_handler1.setFormatter(formatter)


# 3rd handler
stream_handler=logging.StreamHandler()
st_formatter=logging.Formatter('%(levelname)s: %(message)s')
stream_handler.setFormatter(st_formatter)

logger.addHandler(file_handler)
logger.addHandler(file_handler1)
logger.addHandler(stream_handler)




#logging.basicConfig(filename='new_logging.log',level=logging.INFO,
                    # format='%(asctime)s: %(levelname)s: %(message)s')

def addition(x,y):
    return x+y

def division(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        logger.exception('Tried to devide by zero')
    else:
        return result

num_1=18
num_2=4
num_3=0

# div_result=division(num_1,num_2)
# logger.debug(f'Div numbers {num_1}, {num_2} is equal to {div_result}')

div_result=division(num_1,num_3)
logger.debug(f'Div numbers {num_1}, {num_3} is equal to {div_result}')

add_result=addition(num_1,num_2)
logger.debug(f'Adding numbers {num_1}, {num_2} is equal to {add_result}')

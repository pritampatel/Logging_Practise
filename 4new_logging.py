import employee1
import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter=logging.Formatter('%(asctime)s: %(levelname)s: %(name)s:  %(message)s')
file_handler=logging.FileHandler('new_logging.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


#logging.basicConfig(filename='new_logging.log',level=logging.INFO,
                    # format='%(asctime)s: %(levelname)s: %(message)s')

def add(x,y):
    return x+y

num_1=18
num_2=27

add_result=add(18,27)
logger.debug(f'Add numbers {num_1}, {num_2} is equal to {add_result}')
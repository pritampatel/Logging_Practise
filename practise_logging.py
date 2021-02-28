import logging


logging.basicConfig(filename='test.log',level=logging.DEBUG)

def add(x,y):
    return x+y

num_1=18
num_2=27

add_result=add(18,27)
logging.debug(f'Add numbers {num_1}, {num_2} is equal to {add_result}')
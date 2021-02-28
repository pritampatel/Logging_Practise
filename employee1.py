import logging
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter=logging.Formatter('%(levelname)s: %(name)s: %(message)s')
file_handler=logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

#logging.basicConfig(filename='employee_log.log',level=logging.INFO,
                #format='%(levelname)s: %(name)s: %(message)s')    


class Employee:

    def __init__(self,first_name,last_name):

        self.first_name = first_name
        self.last_name= last_name

        logger.info('Created Employee: {} {}'.format(self.full_name,self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first_name,self.last_name)
    
    @property
    def full_name(self):
        return '{} {}'.format(self.first_name,self.last_name)


emp1=Employee('John','Smith')
emp2=Employee('Will','Smith')
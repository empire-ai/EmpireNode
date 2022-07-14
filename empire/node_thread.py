from empire_object import empire_object
import _thread
import time

class node_thread(empire_object):
    """ node_thread
    Queue system to be used in a single thread
    
    ToDo:
    1. limit list length
    2. 
    """
    
    def __init__(self):
        self.task_list = []
        self.current = -1
        
        _thread.start_new_thread(self.run,())
        
    def run(self):
        """
        Thread main function, iterates through tasks
        """
        while True:
            for task in self.task_list:
                task()
                # sleep 1ms for thread switching
                time.sleep(0.001)
        
        
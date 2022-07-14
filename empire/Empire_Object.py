class empire_object:
    """empire_object

    The root node of all the Python objects necessary to describe and
    operate autonomous iot networked system to build complete
    robotic setups  

    The object along with the Node will be used on both python3 and
    micropython 1.18 implementations

    All Empire Objects are iterable, so all process requiring stacks
    will be able to stick with vanilla Python as much as possible.
    
        Example:
        def sw_task(Empire_Node):
            def __init__(self, name, payload):
                self.name =  name
                self.payload = payload
        
            def run(self):
                self.payload()
        
        def update_color(caller):
            white.duty(1023)
            
        def update_fan(caller):
            fan.duty(100)
        
        sw_queue = []
        sw_quque.append(sw_task('set_color', update_color))
        sw_quque.append(sw_task('set_fan', update_fan))
        
        while(True):
            for idx, elem in enumerate(sw_queue):
                elem.run()
                # next_element = sw_queue[(idx+1)%len(sw_queue)]
                time.sleep_ms(1)

    Todo:
        * 

    .. _Google Python Style Guide:
       http://google.github.io/styleguide/pyguide.html

    """
    name = "id_not_set!"
    
    def __init__(self, name_in, max=0):
        self.name = name_in
    
    def copy(self):
        return Empire_Object(self.name)
    
    def __repr__(self):
        return "Empire_Object('"+str(self.name)+"')"
    
    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
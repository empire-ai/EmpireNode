import time
### 60ms
#_t_start = time.ticks_ms()
import machine
#_t_end = time.ticks_ms()

### 581ms
#_t_start = time.ticks_ms()
from Lib.micropython_dotstar import DotStar as apa102
spi = machine.SoftSPI(sck=machine.Pin(26), mosi=machine.Pin(25), miso=machine.Pin(0))
leds = apa102(spi,6)
leds[0] = (0,0,100)
leds[1] = (0,0,100)
leds[4] = (0,0,100)
leds[5] = (0,0,100)
#_t_end = time.ticks_ms()

import _thread
import time

_vector_rgbw = (0,0,0,0)
_current_rgbw = (0,0,0,0)
target_rgbw = (0,0,0,0)
steps = 50
last_render = 0
_exception = None
speed = 1000
delay = 1
shape = "sin"

#enable all
machine.Pin(27, machine.Pin.OUT, value=1)
white = machine.PWM(machine.Pin(4),19000)

def _interpolate_led_channel(c_id):
    '''
    Helper function to *hw_update*, to split the logic per channel
    '''
    
    global target_rgbw, _vector_rgbw, _current_rgbw
    
    # if channel is within 1 codevalue target value is used
    if abs(_current_rgbw[c_id]-target_rgbw[c_id]) > abs(_vector_rgbw[c_id]):
        ch_out = _current_rgbw[c_id]+_vector_rgbw[c_id]
    else:
        ch_out = target_rgbw[c_id]
    
    # clip
    if ch_out > 1023:
        ch_out = 1023
    if ch_out < 0:
        ch_out =0
        
    return ch_out
    

def hw_update(caller):
    '''
    Timer IRQ event to update all HW raleated IOs for properties
    '''
    global target_rgbw, _vector_rgbw, _current_rgbw, last_render, _exception
    #_t_start = time.ticks_us()
    out = []
    for i in range(4):
        out.append(_interpolate_led_channel(i))
    
    try:
        white.duty(out[3])
    except Exception as e:
        #check for an exeption in local variable.
        #Otherwise print is called every 5ms messing up Your REPL promt
        _exception = str(out)+"\n --- Exception --- \n"+str(e) 
        
    _current_rgbw = tuple(out)
    #_t_end = time.ticks_us()
    #last_render = time.ticks_diff(_t_end,_t_start)
     
def target_set(color_in):
    global target_rgbw, _vector_rgbw, _current_rgbw, steps, last_render
    #_t_start = time.ticks_ms()
    target_rgbw = color_in
    out = [] 
    for i in range(4):
        val = int((color_in[i]-_current_rgbw[i])/steps)
        # to accomodate the codevalues that will be rounded close to zero
        if val == 0:
            val = color_in[i]
            
        out.append(val)
        
    _vector_rgbw = tuple(out)
    #_t_end = time.ticks_ms()
    #2ms last_render = time.ticks_diff(_t_start,_t_end)

#step size
#min step size
#within range case

tim = machine.Timer(2)
tim.init(period=5,mode=machine.Timer.PERIODIC,callback=hw_update)

import math    
import _thread

def sin_float():
    global speed, delay, shape
    while(True):
        if speed > 0:
            if shape=="sin":
                float_func = int(math.sin(time.ticks_ms()/speed)*1023+1023) >> 1
            if shape=="square":
                float_func = int(math.sin(time.ticks_ms()/speed)+1)*1023
        
            target_set((float_func,float_func,float_func,float_func))
        else:
            time.sleep_ms(3)
        time.sleep_ms(delay)    
        
_thread.start_new_thread(sin_float, ())


    


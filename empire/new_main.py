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

#enable all
machine.Pin(27, machine.Pin.OUT, value=1)
white = machine.PWM(machine.Pin(4),19000)

def _interpolate_led_channel(c_id):
    global target_rgbw, _vector_rgbw, _current_rgbw
    '''
    Helper function to *hw_update*, to split the logic per channel
    '''
    if abs(_current_rgbw[c_id]-target_rgbw[c_id]) > 1:
        ch_out = _current_rgbw[c_id]+_vector_rgbw[c_id]
    else:
        ch_out = target_rgbw[c_id]
    
    return ch_out
    

def hw_update(caller):
    '''
    Timer IRQ event to update all HW raleated IOs for properties
    '''
    global target_rgbw, _vector_rgbw, _current_rgbw, last_render
    _t_start = time.ticks_ms()
    out = []
    for i in range(4):
        out.append(_interpolate_led_channel(i))
    
    try:
        white.duty(out[3])
    except Exception as e:
        print(str(out))
        print(e)
        
    _current_rgbw = tuple(out)
    time.sleep_ms(2)
    _t_end = time.ticks_ms()
    last_renderder = time.ticks_diff(_t_start,_t_end)
    
def target_set(color_in):
    global target_rgbw, _vector_rgbw, _current_rgbw, steps
    target_rgbw = color_in
    out = [] 
    for i in range(4):
        out.append(int((color_in[i]-_current_rgbw[i])/steps))
        
    _vector_rgbw = tuple(out)

#step size
#min step size
#within range case

tim = machine.Timer(2)
tim.init(period=5,mode=machine.Timer.PERIODIC,callback=hw_update)

    
import uasyncio


    


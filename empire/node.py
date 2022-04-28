'''
Empire Node
is ESP32 micropython software to run Empire Properties multinode hardware automation platform
creates empire_node objects

Apollo0001 = empire.node("Apollo0001")
Apollo0001.hw.buttons.program = hardware.pin(hardware.pin.PIN
Apollo0001.hw.buttons.blackout
Apollo0001.hw.in.vin
Apollo0001.hw.in.fan_tacho

Apollo0001.hw.i2c
Apollo0001.hw.spi = machine.SoftSPI(sck=machine.Pin(X), mosi=machine.Pin(X), miso=machine.Pin(X))

Apollo0001.hw.wifi = network.WLAN(network.STA_IF)
#Apollo0001.hw.BLE
#Apollo0001.hw.lumen_radio

Apollo0001.hw.sockets.artnet = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
Apollo0001.hw.sockets.artnet.bind((server,port))
Apollo0001.hw.sockets.artnet.setblocking(False)
Apollo0001.start() # maybe needs main uasync task stack

# Create Tempreature reading
prop = new()
prop.name = "LED temp"
prop._readonly = True
prop._on_create = 'from empire import tempsensor\nself.storage.append(tempsensor(i2c,79))'
prop._on_update = self.storage[0].read_filtered()*100
prop._converter = print('%i.%i',((i/100),(i-i*100)))
Apollo0001.add_prop(prop)

# create color output
# create intensity with color object, other properties will use the render object asved in this one
prop = new()
prop.name = "Intesity"
prop._on_create = 'from empire import rendrer\nself.storage.append(empire.renderer(Pins,temp=self.find_prop('LED temp'))'
prop._on_update = self.storage[0].set_intensity(val)
prop._on_changed = self._on_update
prop._on_edit = self._on_update
prop._converter = print('%f',(i/2.55))
Apollo0001.add_prop(prop)

# create color temperature
prop = new()
prop.name = "Temperature"
prop._on_create = 'self.storage.append(properties_find('Intensity').storage[0])'
prop._on_update = self.storage[0].set_temp(val)
prop._on_changed = self._on_update
prop._on_edit = self._on_update
prop._converter = print('%iK',(7200/255*i+2800))
Apollo0001.add_prop(prop)




## Computer sim
#how to buffer the last packet so all lamps can process it
Apollo000 = []
Apollo000.append(empire.node("Apollo0001))
Apollo000.append(empire.node("Apollo0002))
Apollo000.append(empire.node("Apollo0003))
while(1):
    for node in Apllo000:
        node.step()
    

timer

spi

__init__
a new node is created

'''
__version__ = 0.001
__author__ = "empire-ai"

class node:
'''
One Emprie Node device, acts as IO interface fro robotics
'''
    _name = "empty"
    _tags = []
    _properties = []
    
    def _update_prop(self,prop_in):
    '''
    Updates specific property
    '''
    prop_in._update_()
    
    def _update_(self):
    '''
    Updates entire Node properties in the node stack
    '''
        for prop in self._properties:
            self._update_prop(prop)
        pass
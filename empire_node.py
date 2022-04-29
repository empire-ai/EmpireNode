'''
Empire Node
is ESP32 micropython software to run Empire Properties multinode hardware automation platform
creates empire_node objects

Apollo = empire.node("Apollo0001")
Apollo.hw.buttons.program = Pin(34, Pin.IN, Pin.PULL_UP)
Apollo.hw.buttons.blackout = Pin(35, Pin.IN, Pin.PULL_UP)
# Communication with LED temp sensor and encoder on P2
Apollo.hw.i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(23))
# One way (ie. miso pin 0) SPI used for the 6 LED APA indicatror
Apollo.hw.spi = machine.SoftSPI(sck=machine.Pin(26), mosi=machine.Pin(25), miso=machine.Pin(0))
Apollo.hw.pwm.fan
Apollo.hw.pwm.red
Apollo.hw.pwm.green
Apollo.hw.pwm.blue
Apollo.hw.pwm.white
Apollo.hw.com.wifi
Apollo.hw.com.ble
Apollo.hw.com.dodc
Apollo.hw.com.lumenradio
Apollo.prop
Apollo.start()


GPIO pins

i2c

prop = new()
prop.name = "LED temp"
prop._readonly = True
prop._on_create = 'from empire import tempsensor\nself.storage.append(tempsensor(i2c,79))'
prop._on_update = self.storage[0].read_filtered()*100
prop._converter = print('%i.%i'%((i/100)(i-i*100))
Apollo0001.add_prop(prop)

# create color output
prop = new()
prop.name = "Intesity"
prop._on_create = 'from empire import rendrer\nself.storage.append(empire.renderer(Pins,temp=self.find_prop('LED temp'))'
prop._on_update = self.storage[0].set_intensity(val)
prop._on_changed = self._on_update
prop._on_edit = self._on_update
prop._converter = print('%f'%(i/2.55))
Apollo0001.add_prop(prop)

# create color output
prop = new()
prop.name = "Temperature"
prop._on_create = 'self.storage.append(Apollo0001.storage[0])'
prop._on_update = self.storage[0].set_intensity(val)
prop._on_changed = self._on_update
prop._on_edit = self._on_update
prop._converter = print('%iK'%(i*28.125+2800))
Apollo0001.add_prop(prop)





spi

__init__
a new node is created

'''
__version__ = 0.001
__author__ = "empire-ai"

def node:
    '''
    Empire node is the base building block for robotic interface. The node is one single addressable
    entety that has at least one or more read-only property.
    
    Empire Node is:
    DS Apollo lamp props = [
                            "Intensity",
                            "Temperature",
                            "Hue",
                            "Satuartion",
                            "Red",
                            "Green",
                            "Blue",
                            "LED Temp",
                            "Input Voltage",
                            "WiFi Mode",
                            "WiFi SSID",
                            "WiFi Password",
                            "Art-Net Uni",
                            "Art-Net Control Offset",
                            "Art-Net FX Offset"
                            ]
    M5 Matrix with battery back used as trigger props = [
                            "Red",
                            "Green",
                            "Blue",
                            "Button Clicked"
                            ]
    Android phone with Monet UI app props = [
                            "UI"
                            ]
    Floor temperature sensor props = [
                            "Temp from Sensor"
                            "Current Power"
                            ]
    
    All the apps use the same 512byte payload communication standard.
    The payload consits of utf-8 python code sent to REPL and ansers.
    *in rare cases where no reasonable Python solution is not avaiable like we have not yet
    found a solution for iOS Python implementaion, so we added miniscript for Unity Props app.
    
    The node is used as genereic template to create specific solutions ie. one of the node
    implementations like Apollo P2
    '''
    _device_id = "undefined"
    _tags = []
    _props = []
'''
Empire Node
is ESP32 micropython software to run Empire Properties multinode hardware automation platform
creates empire_node objects

Apollo0001 = empire.node("Apollo0001",hw_description=apollo_hw.py)
Apollo0001.hw.buttons.program
Apollo0001.hw.buttons.blackout
Apollo0001.hw.i2c
Apollo0001.hw.spi
Apollo0001.hw.gpio
Apollo0001.hw.sockets
Apollo0001.hw.temp = empire.tempsenor(i2c,79)
Apollo0001.properties_add("LED temp", on_update=hw.temp.get(type="filtered"))
renderer = render(GPIOpins, temp_sensor)
Apollo0001.properties_add("Red", on_update=renderer.red)
Apollo0001.properties_add("Tempreature", )

GPIO pins

i2c

prop = new()
prop.name = "LED temp"
prop._readonly = True
prop._on_create = 'from empire import tempsensor\nself.storage.append(tempsensor(i2c,79))'
prop._on_update = self.storage[0].read_filtered()*100
prop._converter = printf('i.i',[i/100,i-i*100])

Apollo0001.add_prop(prop)

# create color output
prop = new()
prop.name = "Intesity"
prop._on_create = 'from empire import rendrer\nself.storage.append(empire.renderer(Pins,temp=self.find_prop('LED temp'))'
prop._on_update = self.storage[0].set_intensity(val)
prop._on_changed = self._on_update
prop._on_edit = self._on_update
prop._converter = print('%f',(i/2.55))





spi

__init__
a new node is created

'''
__version__ = 0.001
__author__ = "empire-ai"

import uasyncio as asyncio

print(1)
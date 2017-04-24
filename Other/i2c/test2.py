import smbus
import time
bus = smbus.SMBus(1)
address = 0x48
SHIFT_BIT_ADDR = 0x35
DISTANCE_ADDR = 0x5E

#SRF08 REQUIRES 5V

def write(value):
        bus.write_byte_data(address, 0, value)
        return -1

def lightlevel():
        light = bus.read_byte_data(address, 1)
        return light

def range():
        range1 = bus.read_byte_data(address, 2)
        range2 = bus.read_byte_data(address, 3)
        range3 = (range1 << 8) + range2
        return range3

while True:
        write(0x51)
        time.sleep(0.7)
        print(chr(bus.read_byte(address)))
        lightlvl = lightlevel()
        rng = range()
        print(lightlevel(),"\t",range())

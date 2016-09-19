#/usr/bin/python
import smbus
import time
bus = smbus.SMBus(2)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)
#adresses
DEVICE_ADDRESS = 0x24
DEVICE_REG1_DIR = 0x00
DEVICE_REG1_IO = 0x13
#values
DIR_VALUE = 0x00
VALUE0 = 0x00
VALUE1 = 0x01
#variables
#initialize output
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG1_DIR, DIR_VALUE)
#temp cycle
temp=34.1
while temp>34.0:
	temp=0
	f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
	for line in f:
		print (line)
		temp = float(line)/1000
		print (temp)
	if temp > 34.0: 
		bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG1_IO, VALUE1)
		time.sleep(5)
	f = open('/sys/class/thermal/thermal_zone0/temp', 'r')
	for line in f:
		print (line)
		temp = float(line)/1000
print ("final temp is ", temp)
bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REG1_IO, VALUE0)

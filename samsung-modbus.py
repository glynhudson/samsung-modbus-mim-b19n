# Example script to read data from a Samsung Heat Pump or HVAC unit using MIM-B19N Modbus module

import minimalmodbus
import serial
import struct
import time
def millis():
    return int(round(time.time() * 1000))

def C(val):
    return struct.pack('!H', val)

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

instrument.serial.port                     # this is the serial port name
instrument.serial.baudrate = 9600          # Baud
instrument.serial.bytesize = 8
instrument.serial.parity   = serial.PARITY_EVEN
instrument.serial.stopbits = 1
instrument.serial.timeout  = 1             # seconds
instrument.debug = False

instrument.address = 1                     # this is the slave address number
instrument.mode = minimalmodbus.MODE_RTU   # rtu or ascii mode


################################################################
# READ COMMANDS
################################################################


################################################################
# HIDDEN REGESITERS
################################################################

# Compresor Frequency - doesnt seem to work
instrument.write_register(6000,0x8238)
# time.sleep(0.5)
compressor_freq = instrument.read_register(4,functioncode=3)
print ("Compressor Freq: " + str(compressor_freq))


# Outdoor temp
instrument.write_register(6001,0x8204)
time.sleep(0.5)
outdoor_temp = round(0.1*(instrument.read_register(5,functioncode=3)),2)
print ("Outdoor temp: " + str(outdoor_temp))
time.sleep(0.5)



# Flow rate in L/min
instrument.write_register(6007,0x42E9)
time.sleep(0.5)
flowrate = round(0.1*(instrument.read_register(11,functioncode=3)),2)
print ("Flow rate: " + str(flowrate))

# compressor_freq_ratio 50%-150%
instrument.write_register(6008,0x42F1)
time.sleep(0.5)
compressor_freq_ratio = round(0.1*(instrument.read_register(12,functioncode=3)),2)
print ("Compressor frequency ratio: " + str(compressor_freq_ratio))


dhw_temp = round(0.1*(instrument.read_register(75,functioncode=3)),2)
time.sleep(0.5)

return_temp = round(0.1*(instrument.read_register(65,functioncode=3)),2)
time.sleep(0.5)

flow_temp = round(0.1*(instrument.read_register(66,functioncode=3)),2)
time.sleep(0.5)

target_flow_temp = round(0.1*(instrument.read_register(68,functioncode=3)),2)
time.sleep(0.5)

dhw_status = instrument.read_register(72,functioncode=3)
time.sleep(0.5)

target_dhw_temp = round(0.1*(instrument.read_register(74,functioncode=3)),2)
time.sleep(0.5)

away_status = instrument.read_register(79,functioncode=3)
time.sleep(0.5)

ch_status = instrument.read_register(52,functioncode=3)
time.sleep(0.5)

indoor_temp = round(0.1*(instrument.read_register(59,functioncode=3)),2)
time.sleep(0.5)

target_indoor_temp  = round(0.1*(instrument.read_register(58,functioncode=3)),2)
time.sleep(0.5)

defrost_status = instrument.read_register(2,functioncode=3)


print ("Central heating status: " + str(ch_status))
print ("Target indoor temp: " + str(target_indoor_temp))
print ("Indoor temp: " + str(indoor_temp))


print ("Target flow temp: " + str(target_flow_temp))
print ("Flow temp: " + str(flow_temp))
print ("Return temp: " + str(return_temp))



print ("DHW status: " + str(dhw_status))
print ("DHW target temp: " + str(target_dhw_temp))
print ("DHW temp: " + str(dhw_temp))


print ("Away mode status: " + str(away_status))
print ("Defrost operation status: " + str(defrost_status))



################################################################
# WrITE COMMANDS (CONTROL)
################################################################

# Switch on DHW
# instrument.write_register(72,1)

# Switch on CH
# instrument.write_register(52,1)


# Set DHW temp to 50 deg C
# instrument.write_register(74,500)

# Set flow temp to 40 deg C - doenst seem to work
# instrument.write_register(68,400)

# Set indoor target temp to 21 deg C
# instrument.write_register(58,210)

# Set away mode on
# instrument.write_register(79,1)
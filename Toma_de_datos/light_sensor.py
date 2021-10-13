#!/bin/python

# Read data from a BH1750 digital light sensor.

import smbus
import time

# Define some constants from the datasheet

DEVICE     = 0x23 # Default device I2C address
POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
HR_MODE_1 = 0x20

bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(addr,HR_MODE_1)
  return convertToNumber(data)

def main():
    while True:
    lightLevel=readLight()
    print("Light Level : " + format(lightLevel,'.2f') + " lx")
    #print("light level: " +str(lightLevel) + " lx")
    time.sleep(2)

if __name__=="__main__":
   main()

# 7/16/2021 Created by Noah Wadsworth
# This function allows a RaspberryPi to pump water to 4 different pumps in 4 garden beds

# Imports
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme

# GPIO Variables

pump1 = 7
pump2 = 11
pump3 = 12
pump4 = 13
pump_time = 10 #pump for 10 seconds at a time
delay = 21600  # 6 hours
#pmax = 10 #max number of pump iteratoions (Prevents, pumping forever with moisture error)

# Function to set up GPIO output

def gpio_set(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)


#water pump function box 1
def water_1():
    now1 = datetime.now()
    gpio_set(pump1)
    GPIO.output(pump1, GPIO.LOW)  # turn on pump 1
    time.sleep(pump_time)  # pump for pump_time seconds
    GPIO.output(pump1, GPIO.HIGH) 
    print('Box 1 was watered at: ', now1)
    
#water pump function box 2
def water_2():
    now2 = datetime.now()
    gpio_set(pump2)
    GPIO.output(pump2, GPIO.LOW)  # turn on pump 2
    time.sleep(pump_time)  # pump for pump_time seconds
    GPIO.output(pump2, GPIO.HIGH)  # turn off pump 2
    print('Box 2 was watered at: ', now2)

#water pump function box 3
def water_3():
    now3 = datetime.now()
    gpio_set(pump3)
    GPIO.output(pump3, GPIO.LOW)  # turn on pump 3
    time.sleep(pump_time)  # pump for pump_time seconds
    GPIO.output(pump3, GPIO.HIGH)  # turn off pump 3
    print('Box 3 was watered at: ', now3)
    
#water pump function box 4
def water_4():
    now4 = datetime.now()
    gpio_set(pump4)
    GPIO.output(pump4, GPIO.LOW)  # turn on pump 4
    time.sleep(pump_time)  # pump for pump_time seconds
    GPIO.output(pump4, GPIO.HIGH)  # turn off pump 4
    print('Box 4 was watered at: ', now4)

# Function to compile everything and call it in time intervals
def auto_water():
    water_1()  
    water_2()
    water_3()
    water_4()
    time.sleep(delay)  # sleep for 6 hours


while True:
    auto_water()  # Run auto_water forever
    
GPIO.cleanup()

# 2/13/2021 Created by Noah Wadsworth
# This function allows a RaspberryPi to get soil moisture info and then pump water to the soil if the soil is dry

# Imports
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme

# GPIO Variables
moist = 7
pump1 = 8
pump2 = 9
pump_time = 10
delay = 21600  # 6 hours
# Function to set up GPIO output


def gpio_set(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)

# Function to get soil status and return it


def soil_status():
    GPIO.setup(moist, GPIO.IN)
    soil = GPIO.input(moist)
    now = datetime.now()
    # print wet if 0 and dry if else
    if soil == 0:
        print("At %s the soil was wet." % (now))
    else:
        print("At %s the soil was dry." % (now))

    return soil


# Function to turn pumps on if dry
def water(soil):
    gpio_set(pump1)
    gpio_set(pump2)

    while True:  # While loop to continue until soil is wet

        soil = soil_status()
        if soil == 0:  # If soil is 0 (wet) do nothing and break the while loop
            break
        else:
            GPIO.output(pump1.LOW)  # turn on pump 1
            GPIO.output(pump2.LOW)  # turn on pump 2
            time.sleep(pump_time)  # pump for pump_time seconds
            GPIO.output(pump1.HIGH)  # turn off pump 1
            GPIO.output(pump2.HIGH)  # turn off pump 2


# Function to compile everything and call it in time intervals
def auto_water():
    water(soil_status)  # not sure if this will work
    time.sleep(delay)  # sleep for 6 hours


while True:
    auto_water()  # Run auto_water forever

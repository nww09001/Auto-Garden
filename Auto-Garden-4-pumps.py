# 2/13/2021 Created by Noah Wadsworth
# This function allows a RaspberryPi to get soil moisture info and then pump water to the soil if the soil is dry

# Imports
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setmode(GPIO.BOARD)  # Broadcom pin-numbering scheme

# GPIO Variables
moist1 = 35
moist2 = 36
moist3 = 37
mosit4 = 38
pump1 = 7
pump2 = 11
pump3 = 12
pump4 = 13
pump_time = 10 #pump for 10 seconds at a time
delay = 21600  # 6 hours
pmax = 10 #max number of pump iteratoions (Prevents, pumping forever with moisture error)

# Function to set up GPIO output

def gpio_set(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    GPIO.output(pin, GPIO.HIGH)



#Code to Check soil in box 1 and water it
#soil function bosx 1
def soil_status1():
    
    GPIO.setup(moist1, GPIO.IN)
    soil1 = GPIO.input(moist1)
    now = datetime.now()
    # print wet if 0 and dry if else
    if soil1 == 0:
        print("At %s the soil in box 1 was wet." % (now))
    else:
        print("At %s the soil in box 1 was dry." % (now))

    return soil1

#water pump function box 1
def water_1():
    gpio_set(pump1)
    
    p = 0 #Counts number of times pumped

    while True:  # While loop to continue until soil is wet

        soil1 = soil_status1()
        if soil1 == 0:  # If soil is 0 (wet) do nothing and break the while loop
            break
        else:
            GPIO.output(pump1, GPIO.LOW)  # turn on pump 1
            time.sleep(pump_time)  # pump for pump_time seconds
            GPIO.output(pump1, GPIO.HIGH)  # turn off pump 1
            p += 1 
            if p < pmax:
                print("p is less than pmax, keep pumping") # I will delete this after I know it works
            else:
                break

#Code to check soil in box 2 and water it

def soil_status2():
    
    GPIO.setup(moist2, GPIO.IN)
    soil2 = GPIO.input(moist2)
    now = datetime.now()
    # print wet if 0 and dry if else
    if soil2 == 0:
        print("At %s the soil in box 2 was wet." % (now))
    else:
        print("At %s the soil in box 2 was dry." % (now))

    return soil2

#water pump function box 2
def water_2():
    gpio_set(pump2)
    
    p = 0 #Counts number of times pumped

    while True:  # While loop to continue until soil is wet

        soil2 = soil_status2()
        if soil2 == 0:  # If soil is 0 (wet) do nothing and break the while loop
            break
        else:
            GPIO.output(pump2, GPIO.LOW)  # turn on pump 1
            time.sleep(pump_time)  # pump for pump_time seconds
            GPIO.output(pump2, GPIO.HIGH)  # turn off pump 1
            p += 1 
            if p < pmax:
                print("p is less than pmax, keep pumping") # I will delete this after I know it works
            else:
                break

#Code to check soil in box 3 and water it

def soil_status3():
    
    GPIO.setup(moist3, GPIO.IN)
    soil3 = GPIO.input(moist3)
    now = datetime.now()
    # print wet if 0 and dry if else
    if soil3 == 0:
        print("At %s the soil in box 3 was wet." % (now))
    else:
        print("At %s the soil in box 3 was dry." % (now))

    return soil3

#water pump function box 3
def water_3():
    gpio_set(pump3)
    
    p = 0 #Counts number of times pumped

    while True:  # While loop to continue until soil is wet

        soil3 = soil_status3()
        if soil3 == 0:  # If soil is 0 (wet) do nothing and break the while loop
            break
        else:
            GPIO.output(pump3, GPIO.LOW)  # turn on pump 1
            time.sleep(pump_time)  # pump for pump_time seconds
            GPIO.output(pump3, GPIO.HIGH)  # turn off pump 1
            p += 1 
            if p < pmax:
                print("p is less than pmax, keep pumping") # I will delete this after I know it works
            else:
                break

#Code to check soil in box 4 and water it
def soil_status4():
    
    GPIO.setup(moist4, GPIO.IN)
    soil4 = GPIO.input(moist4)
    now = datetime.now()
    # print wet if 0 and dry if else
    if soil4 == 0:
        print("At %s the soil in box 4 was wet." % (now))
    else:
        print("At %s the soil in box 4 was dry." % (now))

    return soil4

#water pump function box 3
def water_4():
    gpio_set(pump4)
    
    p = 0 #Counts number of times pumped

    while True:  # While loop to continue until soil is wet

        soil4 = soil_status4()
        if soil4 == 0:  # If soil is 0 (wet) do nothing and break the while loop
            break
        else:
            GPIO.output(pump4, GPIO.LOW)  # turn on pump 1
            time.sleep(pump_time)  # pump for pump_time seconds
            GPIO.output(pump4, GPIO.HIGH)  # turn off pump 1
            p += 1 
            if p < pmax:
                print("p is less than pmax, keep pumping") # I will delete this after I know it works
            else:
                break

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

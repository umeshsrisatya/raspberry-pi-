import RPI.GPIO as GPIO
import time

#set the warnings to false 
GPIO.setwarnings(False)

#select mode(bcm or board)
GPIO.mode(GPIO.BOARD)
#function to take input from file
def read_from_file(filePath):
    with open(file,"r") as file:
        on_time = file.readline()
        off_time = file.readline()
    return on_time, off_time

#decaration of led
led_pin = 12
GPIO.setup(led_pin,GPIO.OUT)

on_time,off_time = read_from_file("time.txt")

#flashing operation
try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(on_time)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(off_time)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()
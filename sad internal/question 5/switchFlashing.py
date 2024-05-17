import RPI.GPIO as GPIO
import time 

# set mode
GPIO.setmode(GPIO.BOARD)

#make warning false to view console clear
GPIO.setwarnings(False)

#pin declaration
switch_pin1=1
switch_pin2=3
led_pin1=2
led_pin2=4

#pin setup
GPIO.setup(switch_pin1,GPIO.IN)
GPIO.setup(switch_pin2,GPIO.IN)
GPIO.setup(led_pin,GPIO.OUT)
GPIO.setup(led_pin2,GPIO.OUT)

#taking input from switches
switch1_state=GPIO.input(switch_pin1)
switch2_state=GPIO.input(switch_pin2)
try:
    while True:
        if(switch1_state == GPIO.HIGH):
            GPIO.output(led_pin1,GPIO.HIGH)
        if(switch2_state == GPIO.HIGH):
            GPIO.output(led_pin2,GPIO.HIGH)
        else:
            GPIO.output(led_pin2,GPIO.LOW)
            GPIO.output(led_pin1,GPIO.LOW)
except keyboardInterrupt:
    GPIO.cleanup() # windows+c to exit from execution
    
GPIO.cleanup()
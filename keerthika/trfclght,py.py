import time
import RPi.GPIO as GPIO       
GPIO.setmode(GPIO.BOARD)      
GPIO.setup(11, GPIO.OUT)      
while True:
	GPIO.output(11,True)  
	time.sleep(1)         
	GPIO.output(11,False) 
	time.sleep(1)
from gpiozero import Button, TrafficLights, Buzzer
buzzer = Buzzer(15)    
button = Button(21)    
lights = TrafficLights(25, 8, 7)    
    
while True:    
           button.wait_for_press()   
           buzzer.on()   
           light.green.on()    
           sleep(1)    
           lights.amber.on()    
           sleep(1)    
           lights.red.on()    
           sleep(1)    
           lights.off()   
           buzzer.off() 

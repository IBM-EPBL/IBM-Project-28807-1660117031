from gpiozero import Button,LED,TrafficLights,Buzzer
from time import sleep

button = Button(21)
lights = TrafficLights(25, 8, 7)
buzzer = Buzzer(15)
while True:
    button.wait_for_press()
    lights.green.on()
    sleep(1)
    lights.amber.on()
    sleep(1)
    lights.red.on()
    sleep(1)
    lights.off()
while True:
    lights.on()
    buzzer.off()
    button.wait_for_press()
    lights.off()
    buzzer.on()
    button.wait_for_release()    
while True:
    lights.blink()
    buzzer.beep()
    button.wait_for_press()
    lights.off()
    buzzer.off()
    button.wait_for_release()

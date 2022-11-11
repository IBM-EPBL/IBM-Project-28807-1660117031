import pyttsx3
from plyer import notification
import time


# Speak method
def Speak(self, audio):
	
	# Calling the initial constructor
	# of pyttsx3
	engine = pyttsx3.init('sapi5')
	
	# Calling the getter method
	voices = engine.getProperty('voices')
	
	# Calling the setter method
	engine.setProperty('voice', voices[1].id)
	
	engine.say(audio)
	engine.runAndWait()
	
	
def Take_break():
	
	Speak("Do you want to start sir?")
	question = input()
	
	if "yes" in question:
		Speak("Starting Sir")
	
	if "no" in question:
		Speak("We will automatically start after 5 Mins Sir.")
		time.sleep(5*60)
		Speak("Starting Sir")
	
	# A notification we will held that
	# Let's Start sir and with a message of
	# will tell you to take a break after 45
	# mins for 10 seconds
	while(True):
		notification.notify(title="Let's Start sir",
		message="will tell you to take a break after 45 mins",
		timeout=10)
		
		# For 45 min the will be no notification but
		# after 45 min a notification will pop up.
		time.sleep(0.5*60)

		Speak("Please Take a break Sir")
		
		notification.notify(title="Break Notification",
		message="Please do use your device after sometime as you have"
		"been continuously using it for 45 mins and it will affect your eyes",
		timeout=10)

		
# Driver's Code		
if __name__ == '__main__':
	Take_break()

import wiotp.sdk.device
import time
import random
myConfig = {
	"identity": {
		"orgId": "gagtey",
		"typeId": "GPS",
		"deviceId":"12345"
	},
	"auth": {
		"token": "12345678"
	}
}

def myCommandCallback (cmd): 
	print ("Message received from IBM IoT Platform: %s" % cmd.data['command']) 
	m=cmd.data['command']

client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

def pub (data): 
	client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
	print ("Published data Successfully: %s", myData)

while True:
	myData={'name': 'Train1', 'lat': 17.6387448, 'lon': 78.4754336}
	pub (myData) 
	time.sleep (3)
	#myData={'name': 'Train2', 'lat': 17.6387448, 'lon': 78.4754336) 
	#pub (myData)
	#time.sleep (3)
	myData={'name': 'Train1', 'lat': 17.6341908, 'lon': 78.4744722}
	pub(myData)
	time.sleep(3)
	myData={'name': 'Train1', 'lat': 17.6340889, 'lon': 78.4745052}
	pub (myData)
	time.sleep (3)
	myData={'name': 'Train1', 'lat': 17.6248626, 'lon': 78.4720259}
	pub (myData)
	time.sleep (3)
	myData={'name': 'Train1', 'lat': 17.6188577, 'lon': 78.4698726}
	pub (myData)
	time.sleep (3)
	myData={'name': 'Train1', 'lat': 17.6132382, 'lon': 78.4707318}
	pub (myData)
	time.sleep (3)
	client.commandCallback = myCommandCallback
client.disconnect ()

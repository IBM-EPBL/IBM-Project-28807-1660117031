from ibmcloudant import CouchDbSessionAuthenticator 
from ibm_cloud_sdk_core.authenticators import BasicAuthenticator

authenticator = BasicAuthenticator('apikey-v2-16u3crmdpkghhxefdi kvpssoh5fwezrmuup5fv5g3ubz', 'b0ab119f45d3e6255eabb978')
service = CloudantV1(authenticator=authenticator)

service.set_service_url('https://apikey-v2-16u3ermdpkghhxefdikvpssoh5fwezrmuup5fv5g3ubz:b0ab119145d3e6255eabb978e7e2f0')

cap= cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

while True:
	_, frame = cap.read()
	decodedObjects = pyzbar.decode (frame)
	for obj in decodedObjects:
		#print ("Data", obj.data)
		a=obj.data.decode('UTF-8')
		cv2.putText(frame, "Ticket", (50, 50), font, 2,	(255, 0, 0), 3)

		#print (a)
		try:
			response = service.get_document(
				db='booking',
				doc_id = a
			).get_result()
			print (response)
			time.sleep(5)
		except Exception as e:
			print ("Not a Valid Ticket")
			time.sleep(5)

	cv2.imshow("Frame",frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
client.disconnect()
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About

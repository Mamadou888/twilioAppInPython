from twilio.rest import TwilioRestClient 
 
# put your own credentials here 
ACCOUNT_SID = "AC3b624087f13a6bb29cc38a1f88a5716b" 
AUTH_TOKEN = "4c436a9e9091e4ecf8853ac3bf66374c" 
 
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
 
client.messages.create( 
	to="+19095393770", 
	from_="+16467986660", 
	body="Give me a kiss!",
)
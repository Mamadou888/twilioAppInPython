import requests

# for x in range(10):
# 	print 

theFact = requests.get('http://bearcatfacts.info/').text

print "Enter a file name:",
userInput = raw_input()

if userInput == "Bear fact" :
    print(theFact)
else:
	print("I dont know what you want")

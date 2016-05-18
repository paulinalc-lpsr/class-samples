# applyCipher.py
# A program to encrypt/decrypt user text
# Using Caesar's Cipher
#
# Author: rc.lopez-castillo.paulina [at] leadps.org


# makes a mapping of encoded alphabet to decoded alphabet
# arguements: key
# returns: dictionary of mapped letters
def createDictionary(key):

	#placeholder
	return{}

# It will give you the encoded message from the user
# arguements: none
# returns: encoded message 
def getMessage():
	pass


#for each letter in message, deocdes and records
#arguements:encoded message, dictionary
#returns: decoded message
def decodedMessage:(message, dictionary)
	pass

#outputs the messgae to the terminal
#arguements: decoded message
#returns:none
def printMessage(message): 	
	pass


#ask user for key
print("What key would you like to use to decode?")
key=raw_input()

dictionary=createDictionary(key)
encodedMessage=getMessage()
decodedMessage=decodeMessage(encodedMessage, dictionary)
printMessage(decodeMessage)

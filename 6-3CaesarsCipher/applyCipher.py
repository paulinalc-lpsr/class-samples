# imports what we need to get
import string

# applyCipher.py
# A program to encrypt/decrypt user text
# using Ceasar's Cipher
#
#Author: rc.lopez-castillo.paulina [at] leadps.org

#makes a mapping of encoded alphabet to decoded alphabet 
#arguments: key
#returns: dictionary of mapped letters
def createDictionary(key):
	lowerAlphabet = string.ascii_lowercase
	upperAlphabet = string.ascii_uppercase
	dictionary = {}
	for a in range(0, len(lowerAlphabet)):
		dictionary[upperAlphabet[(a + key) % 26]] = upperAlphabet[a] 	
	for a in range(0, len(upperAlphabet)):
		dictionary[lowerAlphabet[(a + key) % 26]] = lowerAlphabet[a]
	dictionary[" "] = " "
	return dictionary

#gets the encrypted message from the user
#arguments: none
#returns: encoded message
def getMessage():
	print("What message do you want to encode?")
	message = raw_input()
	return message	


#for each letter in the message; decodes and records
#arguments: decoded message
#returns: none
def decodeMessage(message, dictionary):
	decodedMessage = ""
	for m in message:
		decodedMessage = decodedMessage + dictionary[m] 
		
	return decodedMessage
#outputs the decoded message to the terminal
#arguments: decoded message
#returns: none
def printMessage(message):
	print(message)

#  execution starts here

# ask for the key and message
print("What key would you like to use to decode?")
key = int(raw_input())

dictionary = createDictionary(key)
encodedMessage = getMessage()
decodedMessage = decodeMessage(encodedMessage, dictionary)
print("Okay, here is your secret message.")	
printMessage(decodedMessage)

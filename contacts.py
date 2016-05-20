# will print out the warm welcome
# set up contacts to a list
print("Welcome to Contacts app!")
myChoice=1
myContacts={}

print("What would you like to do?")

# press a number for the option you want
while myChoice != 0:
	print("Press (0) Exit the Contacts app")
	print("Press (1) Add a phone number")
	print("Press (2) Print the full list of contacts")
	print("Press (3) Enter a name to retrieve that contact's phone number")

	myChoice=int(raw_input())
# will let you add a person to your contacts info
	if myChoice == 1:
		print("Whats the name of your contact?")
		name = raw_input()
		print("Whats the phone number of your contact?")
		num= raw_input()	
# this will create a list for the name and phone number
		myContacts[name]= num
# will print out all the contacts
	if myChoice == 2:
		print(myContacts)
# will ask whos number you would like
# if name isnt there then the program will crash whcih is ok
	if myChoice == 3:
		print("Whose number would you like?")
		name= raw_input()
		print("Heres the person you are finding:")
		print(myContacts[name])
	

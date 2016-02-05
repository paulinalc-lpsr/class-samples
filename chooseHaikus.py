# this will open the two haikus about a silly person or about how to write a haiku
fourthHaiku = open(“haiku4.txt” , “r”)
thirdHaiku = open(“haiku4.txt” , “r”)
# let them be able to choose their options
print(“Hi welcome to Haiku Reader!”)
print(“Choose..”)
print”(“(3) For a haiku about a silly person.”)
print(“(4) For a haiku about writing haikus.”)

option = int(raw_input)

if option == 3:
     print(thirdHaiku.read())

if option == 4:
       print(fourthHaiku.read())

fourthHaiku.close()
thirdHaiku.close()

 
# all these lines will be able to write your own haiku by letting the$
print("Welcome to Haiku Generator")
print("Provide the first line of your Haiku:")
lineOne = raw_input()
print("Provide the second line of your Haiku:")
lineTwo = raw_input()
print("Provide the third line of your Haiku:")
lineThree = raw_input()
 
#  will let you be able to store in your haiku in a file
print("What file would you like to tore you Haiku in?")
fileName = raw_input()
 
#makes a list of the users haiku in the same order
userHaiku = [lineOne, lineTwo, lineThree]
 
# makes a file with the name the user put and saves everyting they wr$
myFile = open(fileName, "a")
 
# will prit each line of the haiku in seperate lines
 for lines in userHaiku:
        myFile.write(lines + "/n")
# gives user instructions to find the file
print("When you run cat and the filname in terminal, you should get y$
 
# closes the file
myFile.close()
 

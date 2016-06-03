print("Welcome to the new and improved LPS Soccer!")
class Player(object):
 
        def __init__(self, name, age, goals_shot, jersey, position):
                self.name = name
                self.age = age
                self.goals_shot = goals_shot
                self.jersey = jersey
                self.position = position
 
        # will be able to print the users characters inputted stats
        def printStats(self):
                print(" ")
                print("Name: " + self.name)
                print("Age: " + str(self.age))
                print("Goals: " + str(self.goals_shot))
                print("Jersey : " + str(self.jersey))
                print("Position: " + self.position)
                print(" ")
# uses the player list to the users file name inputted
def saveTeam(playerList, filename):
        # open the file
        myFile = open(filename, "a")
        # will be able to write the file
        for list in playerList:
                myFile.write(list.name + " " + str(list.age) + " " + str(list.goals_shot) + " " +  str(list.jersey) + " " + list.position + "\n")  
        # close the file
                myFile.close()
# be able to return the list of players created
def loadTeam(filename):
        # create empty list
        list = []
        # open the file
        myFile = open(filename, "r")
        # will read each line
        line = myFile.readline()
        # split each line into a list of the variables read each next line
        while line != "":
		stringSplitter = line.split()
                list.append(Player(stringSplitter[0], stringSplitter[1], stringSplitter[2], stringSplitter[3], stringSplitter[4]))
                line = myFile.readline()
 
        myFile.close()
        # will return the completed list
        return list
 
# instructions on what to do now
print("Do you want to start with a new team or existing team?")
print("Enter the letter of your choice and press enter")
print("Press letter x to make your own team!")
print("Press letter y to start with an existing team")
x = raw_input()

# will create a list 
if x == "x":
        myPlayers = []
 
# will show you the players from the existing file
elif x == "y":
        print("Enter the filename for your existing team")
        file_name = raw_input()
        myPlayers = loadTeam(file_name)
        print("Here are the players from the saved file")
 
userInput= 1
# this creates a loop for the instructions
while userInput != "0":
	print("What do you want to do? Enter the number of your choice and press Enter.")
        print("(1) Add a player")
        print("(2) Print all players")
        print("(3) Save your player list to a file")
        print("(0) Leave the program ")
        userInput = raw_input()
 
        # if the user chooses 1, will let the user input there players stats
        if userInput == "1":
                print("Add players name:")
 		name = raw_input()
                print("Add players age:")
                age = raw_input()
                print("Add players number of goals:")
                goals_shot = raw_input()
                print("Add players Jersey Number:")
                jersey = raw_input()
                print("Add players position")
                position = raw_input() 
# this will append the players stats
                myPlayers.append(Player(name, age, goals_shot, jersey, position))
        # if the user choose 2, it will print all the information that they inputed
        elif userInput == "2":
                # this creates a loop to print everything in seperate lines from myPlayers
                for play in myPlayers:
                        print(" ")
                        # this calls the def function that we make earlier
                        play.printStats()
                        print(" ")
# this saves the players list to a file
        elif userInput == "3":
                print("Enter the name of the file you want to add your players to, make sure to add txt")
                newFile = raw_input()
                saveTeam(myPlayers, newFile)
# when the user put in 0, this message will appear
print("Hope you enjoyed making your dream team!")

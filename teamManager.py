# lets make the best dream team in soccer history
class Player(object):
# init function will include name, age and goals shot by the player 
  def __init__(self, name, age, goals_shot):
    self.name = name
    self.age = age
    self.goals_shot = goals_shot
# prints all the data inputted
  def printStats(self):
    print("Name:" + self.name)
    print("Age:" + str(self.age))
    print("Goals:" + str(self.goals_shot))
# makes a list for myPlayer
myPlayer = []

print("Welcome to FIFA 133! Would you like to add a player or would you like to view the players stats? Press 1 to add player or press 2 to view stats.")
option = raw_input()

# press 0 to exit the game
while option != "0":
# will let you add a player and you have to insert all of its stats
  if option == "1":
    print("Lets add a player! please enter the stats below.")
    print("Enter players name:")
    name = raw_input()
    print("Enter players age:")
    age = raw_input()
    print("Number of goals they have scored:")
    goals_shot = raw_input()
    myPlayer.append(Player(name, age, goals_shot))
    print("Okay we are done! Do you want to do option #1,or add another player or do you want option #2, to see the stats?")
    option = raw_input()
  # let you see the list of players that you added
  elif option == "2":
    print("Here are your player stats.")
    for info in myPlayer:
        info.printStats()
    option = raw_input()

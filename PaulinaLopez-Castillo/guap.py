# for every roll of paper towels, you get a $0.25 rebate
# if you buy more than 10 rolls, you get a $0.35 rebat for each one

# but if you're a value club member,
# you get $2 rebate for at least buying one


# find out if user is a vaue club member
print("are you a value club member? respond yes or no")
club = raw_input()
# find out how many rolls of paper towles the user bought
print("how many rolls of paper towels did you buy?")
rolls = int(input())

# if they are in the club, they get an extra $2
if club == "yes":
	print("in the club")
	if rolls > 10:
		rebate = rolls * .35 + 2
	else:
		rebate = rolls * .25 + 2
	   
else:
	if rolls > 10
	rebate = rolls * .25
	
	rebate = rolls * .35
	print("not in the club")
# print rebate
print("Your rebate is $" + str(rebate))
	


#takes myNum, an integer
#returns True if myNum is prime
#returns false if myNum is composite
def isPrime(myNum):
	for num in range(2,myNum):
		if myNum % num == 0:
			return False
	return True
# 11 should be true because it is a prime number 
print("This should be true:")
print(isPrime(11))
# 9 is false because it is a composite number since the factor it has are 1,3 and 9
print("This should be false:")
print(isPrime(9))
# create a list for the numbers to be printed
primeList = []
# will go up to 10000
for n in range(2,10000):
	number = isPrime(n)
	if number == True:
# will append the list
		primeList.append(n)
# open file
myFile = open("primeList", "w")
# will write in the file
myFile.write(str(primeList) + "\n")
# close the file
myFile.close()
# print only odd numbers
print(primeList)

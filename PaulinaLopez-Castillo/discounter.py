# find out pric of the user
print("what is the price?")
price = int(input())


# calculate discount price
discount_price = .9 * price
print(price)


# if user gets a discount, tell them

#if not, tell them.
if price > 1000:
	print("Your price is" + str (discount_price))

else:
	print("Sorry you dont get the discount")

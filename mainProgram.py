import powerFunction

def float_input(question):
	'''makes sure user entered a float'''
	userNumber = raw_input(question)
	
	stopper = 0
	while stopper == 0:
		
		try:
			userNumber = float(userNumber)
			stopper = 1
		except ValueError:
			print("That's not a float, wise guy. Try again.")
			userNumber = raw_input(question)
	return userNumber	

#---------------------------------------------
def int_input(question):
	'''makes sure user entered an int'''
	userNumber = raw_input(question)
	
	stopper = 0
	while stopper == 0:
		
		try:
			userNumber = int(userNumber)
			stopper = 1
		except ValueError:
			print("That's not an integer, wise guy. Try again.")
			userNumber = raw_input(question)
	return userNumber	
#--------------------------------------------

base = float_input("What is the base of your equation? ")
exponent =int_input("What power is that base being raised to? ")
if exponent >= 0:
	answer = powerFunction.power_recursion(base, exponent)
	print("{} to the power of {} is {}".format(base, exponent, answer))
else:
	print("That is trippy. Multiply by itself negative amounts of times?")
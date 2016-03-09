#3/9

'''Fuction raises the users inputted base to the power of the user entered base'''
def power(base, exponent):
	count = 1  #Variable will help indicate when to start and stop while loop
	number = base
	if exponent == 0: #Makes the answer 1 if the base is being raised to the 0th power
		number = 1
	while count < exponent:
		number *= base #Multiplies base by itself
		count += 1
	return number
#---------------------------Program below------------------
	
base = int(raw_input("What is the base of your equation? "))
exponent = int(raw_input("What power is that base being raised to?"))
answer = power(base, exponent)
print("{} to the power of {} is {}".format(base, exponent, answer))
def power_recursion(base, exponent):
	'''Uses recursion to multiply the base times itself exponent amount of times'''
	result = 1
	if exponent == 0:
		return result
		
	result = base * (power_recursion(base, exponent - 1))
	return result

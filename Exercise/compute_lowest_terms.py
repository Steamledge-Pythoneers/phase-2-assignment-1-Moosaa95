## TODO: complete the function "lowest_terms" below
##lowest terms
def lowest_terms(x):
	
x = x.split('/')
	numerator = int(x[0])
	denominator = int(x[1])

	""" check for undefined and zeroError """
	if denominator == 0:
		return "Undefined" 
	elif numerator == 0:
		return "0"
	else:
		return reduceFrac(numerator, denominator)
	
""" using recursion to get the greatest common divisor 
	keeping it simple with Lambda

	this collects integer a and integer b and returns their greatest common divisor
"""
gcd = lambda a,b : a if (b == 0) else gcd(b, a%b)


	
x = x.split('/')
	numerator = int(x[0])
	denominator = int(x[1])

	
	if denominator == 0:
		return "Undefined" 
	elif numerator == 0:
		return "0"
	else:
		return reduceFrac(numerator, denominator)
	
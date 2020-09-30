## TODO: complete the function "lowest_terms" below
##lowest terms
def lowest_terms(x):
	""" 
		compute and return the lowest term of a fraction
		split  (x string) into a list after the / operator 
		
	"""
	x = x.split('/')
	numerator = int(x[0])
	denominator = int(x[1])

	#check for zeros and undefined
	if denominator == 0:
		return "Undefined" 
	elif numerator == 0:
		return "0"
	else:
		return reduceFrac(numerator, denominator)
	

##using recursion to return the greatest common divisor of a and b
gcd = lambda a,b : a if (b == 0) else gcd(b, a%b)


def reduceFrac(num,den):
	""" takes in two numbers and returns the reduce form
	num (int) - numerator
	den (int) - denominator
	call the gcd function
	"""
	x = gcd(num, den)
	num = num // x
	den = den // x

	
	return "{}/{}".format(int(num), int(den))
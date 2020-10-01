## TODO: complete the function "lowest_terms" below
##lowest terms
def lowest_terms(x):
	""" 
		compute and return the lowest term of a fraction of the string x
		split  (x string) into a list after the / operator 
		x contains a fraction 
		takes two integers which are :
		numerator and denominator. example '16/28'
		

		
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
		#calls the reduceFrac function
		return reduceFrac(numerator, denominator)
	

##using recursion to return the greatest common divisor of a and b
gcd = lambda a,b : a if (b == 0) else gcd(b, a%b)


def reduceFrac(num,den):
	""" takes in two fractions and returns string of the reduce form
	
	num (int) - numerator of the fraction
	den (int) - denominator of the fraction
	call the gcd function to get the common divisor of num and den
	

	"""
	x = gcd(num, den)
	num = num // x
	den = den // x

	
	return "{}/{}".format(str(num), str(den))
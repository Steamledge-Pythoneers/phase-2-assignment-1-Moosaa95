## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	return ""

""" using recursion to get the greatest common divisor 
	keeping it simple with Lambda

	this collects integer a and integer b and returns their greatest common divisor
"""
gcd = lambda a,b : a if (b == 0) else gcd(b, a%b)


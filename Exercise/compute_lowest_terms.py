## TODO: complete the function "lowest_terms" below

def lowest_terms(x):
	return ""


##reduceFrac function
## returns the reduce form
def reduceFrac(num,den):
	x = gcd(num, den)
	num = num // x
	den = den // x

	
	return "{}/{}".format(int(num), int(den))
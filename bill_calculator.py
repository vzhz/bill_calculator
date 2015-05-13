def user_input():
	meal = raw_input("What was the cost of your meal?  ")
	meal = int(meal)
	tax = raw_input("What is the tax rate (percent, %) of your state?  ")
	tax = float(tax)/100.0
	tip = raw_input("What (percent, %) tip would you like to leave? ")
	tip = float(tip)/100.0
	sharing = raw_input("How many people shared this meal?  ")
	total = meal*(1+tax+tip)
	each = total/float(sharing)
	if sharing == 1:
		print "Your total is %s" % total
	else: 
		print "Each person's total is %s" % each

def main():
	user_input()
main()

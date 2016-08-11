# I want to be able to call is_sorted from main w/ various lists and get
# returned True or False.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def is_sorted(lists):
	if lists == sorted(lists): #we're checking to see if the sorted list = the list
		return True
	else:
		return False



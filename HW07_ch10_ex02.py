# I want to be able to call capitalize_nested from main w/ various lists
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Verify you've tested w/ various nestings.
# In your final submission:
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(t):
	if isinstance (t, list):
		return [capitalize_nested(s) for s in t]
	else:
		return t.upper()
	return new_list

#favorite_things = ['apple', ['bear'], 'cat']














################################################################################
# def main():

    

# if __name__ == "__main__":
#     main()



# The instructions for this are horrible written, so it took me a long time to solve this because I kept getting errors I shouldn't have

def howManyLightSabersDoYouOwn(name = ''):
	if name == 'Zach':
		return 18
	else:
		return 0

# for one line of code
def howManyLightSabersDoYouOwn(name = ''):
	return (18 if name == 'Zach' else 0)

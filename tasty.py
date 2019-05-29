def istasty(flavour):
	if flavour.lower().startswith('sweet'):
		return "Yes"
	elif flavour == 'salty':
		return 'OK'
	else:
		return 'No'


if __name__ == '__main__':
	print (istasty('Sweet'))
	print (istasty('sweet'))
	print (istasty('SWEET'))
	print (istasty('sour'))


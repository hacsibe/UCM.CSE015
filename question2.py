x = ['a', 'e']
y = [1,3,7,9]

def cartesian_product(x,y):
	result= []
		for n1 in x:
			for n2 in y:
			 result.append((n1, n2))
		return result

print (cartesian_product(x, y))

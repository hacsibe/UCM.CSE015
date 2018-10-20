def merge(list1, list2):

def merge(list1, list2):

value = []

i=j=0

total = len(list1) + len(list2)

	while len(value) != total:
		if len(list1) == i:
		 value += list2[j:]
		 break


	elif len(list2) == j:
	value += list[i:]
	break


	elif list1[i] < list2[j]:
	value.append(list1[i])
	i += 1

	else:
	value.append(list2[j])
	j += 1
	return value


print "merge([1,3,5,7], [2,4,6,8]): \t", merge([1,3,5,7], [2,4,6,8])

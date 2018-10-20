# it is only true when both are true
def AND(p, q):
	if p='T' and q=='T': 
		return 'T'
	return'F'

#it is only false when both are false 
def OR(p,q):
	if p=='F' and q=='F':
		return 'F'
	return 'T'

#it is only false when p is true and q is false 
def IF(p,q):
	if p=='T' and q=='F':
		return 'F'
	return 'T'

#it is inverse
def NOT(p):
	return 'F'
	return 'T'

#it is only true if p q are the same 
def IFF(p,q):
	if (p=='T' and q=='T') or (p=='F' and q=='F'):
		return 'F'
	return 'T'

def evaluate(formula):
if formula[1:]:
evaluate (formula[1:])

if formula[0] == 'AND':
return AND (formula[1], formula[2])

elif formula[0] == 'OR':
return OR(formula[1], formula[2])

elif formula[0] == 'IF':
return IF (formula[1], formula[2])

elif formula[0] == 'IFF':
return IFF (formula[1], formula[2])

elif formula[0] == 'NOT':
return NOT(formula[1], formula[2])


p = False
q = False
print "p = ", p
print "q =", q

print "(p or q) or -p:", evaluate(( 'OR', ('OR', p, q), ('NOT', p)))
print "(p or q) or -p:", evaluate(( 'AND ', ('OR', p, q), ('NOT', p)))
 
	
	

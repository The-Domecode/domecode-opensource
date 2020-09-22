"""
def compare(solution, result):
    is_same = True
    for line1, line2 in zip(str(solution), str(result)):
        if line1 != line2:
            is_same = False
    return is_same

"""
"""
def compare(solution, result):
	f1=open((str(solution)),'r')
	f2=open((str(result)),'r')
	for line1 in f1:
		for line2 in f2:
			if line1==line2:
				return True
			else:
				return False
			break
	f1.close()
	f2.close() 
"""


def compare(solution, result):
    if solution == result:
        return True
    else:
        return False

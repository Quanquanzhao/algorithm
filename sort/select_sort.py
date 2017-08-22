# selection sort
def select_sort(lis):
	if len(lis) == 1:
		return lis
	for i in range(len(lis)-1):
		minum = i
		for j in range(i+1, len(lis), 1):
			if lis[j] < lis[minum]:
				minum = j
		if minum != i:
			lis[i], lis[minum] = lis[minum], lis[i]
	return lis 

if __name__ == '__main__':
	List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
	print(select_sort(List))
		

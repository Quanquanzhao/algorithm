def insertion_sort(lis):
	n = len(lis)
	if n == 1:
		return lis
	for i in range(1, len(lis)):
		curr = lis[i]
		for j in range(i, -1, -1):
		 	if lis[j-1] > curr:
				lis[j] = lis[j-1]
			else:
				break
		lis[j] = curr
	return lis

if __name__ == '__main__':
	List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
	print(insertion_sort(List)) 	
		

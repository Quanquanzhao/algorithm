# bubble sort 
def bubble_sort(lis):
	if len(lis) <= 1:
		return lis

	for i in range(len(lis)):
		for j in range(len(lis)-1, i, -1):
			if lis[j] < lis[j-1]:
				lis[j], lis[j-1] = lis[j-1], lis[j]
	return lis	
	
# bubble sort optimize
def bubble_opt_sort(lis):
	if len(lis) <= 1:
		return lis
	for i in range(len(lis)):
		flag = True
		for j in range(len(lis)-1, i, -1):
			if lis[j] < lis[j-1]:
				lis[j], lis[j-1] = lis[j-1], lis[j]
				flag = False
		if flag == True:
			break
	return lis		

if __name__ == '__main__':
	List1 = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
	print(bubble_sort(List1))
	List2 = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
	print(bubble_opt_sort(List2))	

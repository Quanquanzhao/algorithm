# quick sort 
def quick_sort(lis):
	if len(lis) <= 1:
		return lis

	mid = lis[len(lis) // 2]
	left = [x for x in lis if x < mid]
	right = [x for x in lis if x > mid]
	middle = [x for x in lis if x == mid]

	return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
	List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
	print(quick_sort(List)) 
	

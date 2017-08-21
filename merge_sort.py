# -*- coding: utf-8 -*-
# merge sort
def merge_sort(lis):
    if len(lis) <= 1:
        return lis

    mid = len(lis) // 2
    left = merge_sort(lis[:mid])
    right = merge_sort(lis[mid:])
    
    result = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] <= right[0]):
            result.append(left.pop(0))
        else: 
            result.append(right.pop(0))
    
    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)

    return result

if __name__ == "__main__":
    List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
    print(merge_sort(List))

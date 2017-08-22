# -*- coding: utf-8 -*-
# bucket sort
def bucket_sort(lis, bucketsize):
    if len(lis) <= 1:
        return lis
    min_value = lis[0]
    max_value = lis[0]

    for x in lis:
        if x < min_value:
            min_value = x
        if x > max_value:
            max_value = x
    bucket_count =(max_value - min_value) // bucketsize + 1

    buckets = []
    for i in range(0, bucket_count):
        buckets.append([])
    for i in range(0, len(lis)):
        buckets[(lis[i] - min_value) // bucketsize].append(lis[i])
    k = 0
    for i in range(0, len(buckets)):
        insertion_sort(buckets[i])
        for j in buckets[i]:
            lis[k] = j
            k += 1
    return lis

def insertion_sort(lis):
    n = len(lis)
    if n == 1:
        return lis
    for i in range(1, len(lis)):
        for j in range(i, 0, -1):
            if lis[j] < lis[j-1]:
                lis[j], lis[j-1] = lis[j-1], lis[j]
    return lis

if __name__ == "__main__":
    List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
    print(bucket_sort(List, 3))

# —*— coding:utf-8 -*-

# heap sort
def heap_sort(lis):
    # 最大堆调整
    def heap_modify(start, end):
        root = start

        while True:
            child = root * 2 + 1
            if child > end:
                break
            if child + 1 <= end and lis[child] < lis[child + 1]:
                child += 1
            if lis[root] < lis[child]:
                lis[root], lis[child] = lis[child], lis[root]
                root = child
            else:
                break


    # 创建最大堆
    for start in range(len(lis) // 2, -1, -1):
        heap_modify(start, len(lis)-1)

    # 堆排序
    for end in range(len(lis) - 1, 0, -1):
        lis[0], lis[end] = lis[end], lis[0]
        heap_modify(0, end-1)
        
    return lis

if __name__ == "__main__":
    List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
    print(heap_sort(List))

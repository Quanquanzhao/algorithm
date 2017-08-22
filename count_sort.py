# -*- coding: utf-8 -*-
# counting sort
"""
初始化一个计数数组，大小是输入数组中的最大的数。
遍历输入数组，遇到一个数就在计数数组对应的位置上加一。例如：遇到5，就将计数数组第五个位置的数加一。
把计数数组直接覆盖到输出数组（节约空间）。
"""
def count_sort(lis):
    if len(lis) <= 1:
        return lis

    max_lis = 0
    for x in range(len(lis)):
        if lis[x] > max_lis:
            max_lis = lis[x]
    trans_lis = [0] * (max_lis + 1)

    for y in lis:
        trans_lis[y] += 1

    k = 0
    for i in range(len(trans_lis)):
        for j in range(trans_lis[i]):
            lis[k] = i
            k += 1

    return lis


if __name__ == '__main__':
    List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
    print(count_sort(List))

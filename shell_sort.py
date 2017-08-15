# shell sort 
def shell_sort(lis):
    if len(lis) <= 1:
        return lis

    gap = len(lis) // 2
    while gap > 0:
        for i in range(gap, len(lis), 1):
            temp = lis[i]
            j = i
            while j >= gap:
                if lis[j-gap] > temp:
                    lis[j] = lis[j-gap]
                    j = j - gap
                else:
                    break
            lis[j] =  temp
        gap = gap // 2
    return lis   

if __name__ == "__main__":
    List = [12, 4, 3, 3, 5, 13, 1, 17, 19, 15]
    print(shell_sort(List))

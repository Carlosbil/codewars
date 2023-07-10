def partitions(n):
    '''define a function which returns the number of integer partitions of n'''
    sum = 0
    arr = [n]
    while arr[0] > 1:
        print(arr)
        if arr[len(arr)] > 1:
            sum+=1
            arr.append(arr[len(arr)])
            arr[len(arr)]-=1
    return sum

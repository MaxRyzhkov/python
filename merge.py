def merge(arr0,arr1):
    l0 = len(arr0)
    l1 = len(arr1)

    i = 0
    j = 0
    arr = []

    while (i < l0 and j < l1):
        if arr0[i] < arr1[j]:
            arr.append(arr0[i])
            i += 1
        else:
            arr.append(arr1[j])
            j += 1
    
    if i < l0:
        while (i < l0):
            arr.append(arr0[i])
            i += 1
    else:
        while (j < l1):
            arr.append(arr1[j])
            j += 1

    return arr

def swap(arr, i, j):
    k = arr[i]
    arr[i] = arr[j]
    arr[j] = k

def sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[j] < arr[i]): swap(arr, i, j)

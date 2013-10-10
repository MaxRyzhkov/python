def maximum(arr):
    v = arr[0]
    for a in arr:
        if v < a: v = a
    return v

def minimum(arr):
    v = arr[0]
    for a in arr:
        if v > a: v = a
    return v

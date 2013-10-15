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

def average(arr):
    l = len(arr)
    acc = 0
    for a in arr: acc += a
    avg = float(acc) / l
    return avg

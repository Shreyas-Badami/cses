def numSteps(arr):
    n = len(arr)
    res = 0
    if n != 1:
        for i in range(1,n):
            if arr[i] < arr[i-1]:
                res += arr[i-1]-arr[i]
                arr[i] = arr[i-1]
    return res

n = int(input())
inp = list(map(int,input().split())) 

print(numSteps(inp))
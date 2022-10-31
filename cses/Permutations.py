def Beautify(n):
    os = ""
    es = ""
    s = ""
    if n == 1:
        return n
    if n >= 4:
        for i in range(1, n+1):
            if i%2 == 0:
                es = es + str(i) + " "
            else:
                os = os + str(i) + " "
    s = es + os
    if s == "":
        s = "NO SOLUTION"
    return s

n = int(input())
print(Beautify(n))
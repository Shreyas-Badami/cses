def maximumLengthSubstring(s):
    m = 1
    n = len(s)
    i = 0
    while i < n:
        count = 1
        j = i
        while j < n-1:
            if s[j] == s[j+1]:
                count += 1
                j += 1
            else:
                break
        if count > m:
            m = count    
        i = j+1
    return m

s = str(input())
print(maximumLengthSubstring(s))
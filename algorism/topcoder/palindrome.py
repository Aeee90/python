def checkPalindorme(s):
    l = len(s)
    if s == s[::-1]:
        return l
    for i in range(1,l + 1):
        if s[i:] == s[l:i-1:-1]:
            return 2*l - i + 1


s = "bab"
print(checkPalindorme(s))
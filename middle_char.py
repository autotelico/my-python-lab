def mid(str):
    strLength = len(str)
    if (len(str) % 2 == 0):
        return ""
    else:
        return str[strLength // 2]
        
r = mid('cookies')
print(r)
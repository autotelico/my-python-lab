def count(str):
    counter = 0
    for i in range(len(str)):
        if str[i] == '-':
            counter += 1
    return counter + 1
    
r = count('met-a-phor')
print(r)
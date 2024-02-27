def capital_indexes(str):
    array = []
    for i in range(len(str)):
        if (str[i].upper() == str[i]):
            array.append(i)
    return array
r = capital_indexes('HeLlO')
print(r)
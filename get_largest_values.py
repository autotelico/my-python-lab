def get_largest_values(array, value_count):
    newArray = array.copy()
    newArray.sort()
    resultArray = []
    for i in range(value_count):
        resultArray.append(newArray[i])
    return resultArray

myArr = [1, 3, 5, 6, 2]

result = get_largest_values(myArr, 3)
print(result)
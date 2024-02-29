def get_smallest_value(array, value_count):
    newArray = array.copy()
    newArray.sort()
    resultArray = []
    for i in range(value_count):
        resultArray.append(newArray[i])
    return resultArray

myArr = [3, 34324, 12, 231231, 0.2, 1.32, 78]

result = get_smallest_value(myArr, 1)
print(result)
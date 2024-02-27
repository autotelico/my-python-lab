def add_dots(str):
    newString = ''
    for i in range(len(str)):
        if i != len(str) - 1:
            newString += str[i] + '.'
        else:
            newString += str[i]
    return newString
r = add_dots('xx')
print(r)

# bonus function:
def remove_dots(dotted_str):
    new_string = ''
    for i in range(len(dotted_str)):
        if (dotted_str[i] != '.'):
            new_string += dotted_str[i]
    return new_string

s = remove_dots(add_dots('xx'))
print(s)
